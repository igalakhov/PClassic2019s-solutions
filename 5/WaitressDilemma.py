from itertools import *

def minBridges(n, xs, ys, xd, yd):
    c = set([i for i in range(1, n + 1)])

    def get_neighbors(t):
        ret = set()
        x, y = t
        for dx, dy in [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, -1), (-2, 1), (2, -1)]:
            if x + dx in c and y + dy in c:
                ret.add((x + dx, y + dy))
        return ret

    frontier = []
    explored = set()

    # ((coords), length)

    start = (xs, ys)
    end = (xd, yd)

    def optimistic_estimate(n1, n2):
        return (((n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2) ** 1/2)/(5 ** 1/2)

    frontier.append(((xs, ys), 0, optimistic_estimate(start, end)))

    f = None

    while len(frontier):
        frontier.sort(key=lambda x: x[1] + x[2])

        cur = frontier.pop(0)

        if cur[0] == end:
            f = cur
            break

        if cur[0] in explored:
            continue

        explored.add(cur[0])

        for n in get_neighbors(cur[0]):
            if n in explored:
                continue
            frontier.append((n, cur[1] + 1, optimistic_estimate(n, end)))

    return f[1]


if __name__ == '__main__':
    with open('WaitressDilemmaIN.txt', 'r') as f:
        num_test_cases = int(f.readline().strip())
        for i in range(num_test_cases):
          n = f.readline().strip()
          s = f.readline().strip().split()
          xs, ys = s[0], s[1]
          d = f.readline().strip().split()
          xd, yd = d[0], d[1]
          print(minBridges(int(n), int(xs), int(ys), int(xd), int(yd)))