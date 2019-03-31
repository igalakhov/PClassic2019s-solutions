def minDishes(num_islands, bridges):
    global m
    data = {}
    for a, b in bridges:
        if a in data:
            data[a].append(b)
        else:
            data[a] = [b]
        if b in data:
            data[b].append(a)
        else:
            data[b] = [a]

    m = 0
    explored = set()
    start = bridges[0][0]
    explored.add(start)

    def fill_kids(p, c, n):
        global m
        i = 0
        for x in data[n]:
            if x in explored: continue
            while (i == p or i == c): i += 1
            explored.add(x)
            fill_kids(c, i, x)
            i += 1
        m = max(m, i)

    fill_kids(0, 0, start)

    return m

#Do not modify below this line
if __name__ == '__main__':
    with open('PicnicDayIN.txt', 'r') as f:
        cases = int(f.readline().strip())
        for case in range(cases):
            num_islands = int(f.readline().strip())
            bridges = []
            for i in range(num_islands - 1):
                bridges.append(f.readline().strip().split())
            bridges = [[int(a), int(b)] for [a,b] in bridges]
            print(minDishes(num_islands, bridges))
