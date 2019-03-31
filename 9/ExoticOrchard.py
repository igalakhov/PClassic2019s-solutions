from ast import literal_eval


class ConvexHull():

    def right_turn(self, p1, p2, p3):
        return ((p2[0]*p3[1] + p1[0]*p2[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])) < 0

    def in_hull(self, point):
        #print(point)
        #print(self.pts)

        for i in range(len(self.pts) - 1):
            p1 = self.pts[i]
            p2 = self.pts[i + 1]

            if self.right_turn(p1, p2, new_point):
                return False

        return True

    def __init__(self, points):
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


def in_perimeter(points, new_point):
    h = ConvexHull(points.copy())

    return h.in_hull(new_point)


# Do not modify below this line
if __name__ == '__main__':
    with open('ExoticOrchardIN.txt', 'r') as f:
        T = int(f.readline().strip())
        for t in range(T):
            new_point = literal_eval(f.readline().strip())
            num_points = int(f.readline().strip())
            existing_points = []
            for i in range(num_points):
                existing_points.append(literal_eval(f.readline().strip()))
            print('1' if in_perimeter(existing_points, new_point) else '0')


h = ConvexHull([(1, 1), (1, 3), (2, 3), (3, 4), (5, 7), (6, 9), (0, 0), (4, 0)])