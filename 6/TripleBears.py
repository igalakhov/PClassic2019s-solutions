from itertools import *
def tripleBears(arr):
    s = 0
    for i, e in enumerate(arr):
        if e % 9 != 0: continue
        x, y = e/3, e/9
        a, b = 0, 0
        for j in range(i):
            if arr[j] == x: a += 1
            if arr[j] == y: b += 1
        s += a*b

    return s

#Do not modify below this line
if __name__ == '__main__':
    with open('TripleBearsIN.txt', 'r') as f:
        cases = int(f.readline().strip())
        for case in range(cases):
            arr = [int(i) for i in f.readline().strip().split()]
            print(tripleBears(arr))