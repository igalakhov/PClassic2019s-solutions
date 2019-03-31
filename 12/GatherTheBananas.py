from random import random

import math

def solve_linear(a, b, c, d, e, f):
    x_sol = (b*c - d*e + f - a)/(b - d)
    y_sol = b*(x_sol - c) + a


    print(a, b, c, d, e, f)
    return (x_sol, y_sol)

class ConvexHull():

    def right_turn(self, p1, p2, p3):
        return ((p2[0]*p3[1] + p1[0]*p2[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])) < 0

    def __init__(self, points):
        if len(points) == 1:
            self.pts = points
            return

        points.sort()
        #print(points)

        # build the upper and lower parts of the hull separately
        up = [points[0], points[1]] # p1 and p2 will always be in the hull

        for point in points[2:]: # start with the second one
            up.append(point)
            while len(up) > 2 and self.right_turn(up[-3], up[-2], up[-1]): # we need the first one because we're deleting the second to last
                del up[-2]

        points.reverse()
        lo = [points[0], points[1]]

        for point in points[2:]: # start with the second one
            lo.append(point)
            while len(lo) > 2 and self.right_turn(lo[-3], lo[-2], lo[-1]): # we need the first one because we're deleting the second to last
                del lo[-2]

        del lo[0]
        del lo[-1]

        self.pts = up + lo


def makeCircle(points):
    h = ConvexHull(points)

    p = h.pts

    ax = sum([i[0] for i in p])/len(p)
    ay = sum([i[1] for i in p])/len(p)

    # find the points that are the furthest away
    p.sort(key=lambda x: (x[0] - ax)**2 + (x[1] - ay) ** 2, reverse=True)

    p = p[:3]

    r = 0

    if len(p) == 1:
        return (ax, ay, 0)

    if len(p) == 2:
        avg = ((p[0][0] + p[1][0])/2, (p[0][1] + p[1][1]))

        r = ((avg[0] - p[0][0]) ** 2 + (avg[1] - p[1][0]) ** 2) ** 1/2

        return (avg[0], avg[1], r)

    # last case

    p1 = p[0]
    p2 = p[1]
    p3 = p[2]

    while p2[1] == p1[1] or p2[1] == p3[1]:
        if random() > 0.5:
            p1, p2 = p2, p1
        else:
            p3, p2 = p2, p3


    print((p1[0] + p2[0] + p3[0])/3)
x

#Do not modify below this line
if __name__ == '__main__':
    with open('GatherTheBananasIN.txt', 'r') as f:
        while True:
            s = f.readline().strip()
            if s == '':
                break
            A = []
            for i in range(int(s)):
                t = f.readline().strip()
                x, y = t.strip('()').split(',')
                A.append((float(x), float(y)))
            l = makeCircle(A)
            cNew = (round(l[0], 3), round(l[1], 3), round(l[2], 3))
            print(cNew)
