def solve(mesg1, mesg2):
    mesg1 = ' ' + mesg1
    mesg2 = ' ' + mesg2

    diff = {}  # for the d[i, j] trick

    for i in range(len(mesg1)):
        diff[i, 0] = i
    for j in range(len(mesg2)):
        diff[0, j] = j

    # I REMEMBER THIS FROM SCHOOL
    for j in range(1, len(mesg2)):
        for i in range(1, len(mesg1)):
            if mesg1[i] == mesg2[j]:
                diff[i, j] = diff[i-1, j-1]
            else:
                diff[i, j] = min(diff[i-1, j], diff[i, j-1], diff[i-1, j-1]) + 1

    return diff[len(mesg1)-1, len(mesg2)-1]


#Do not modify below this line
if __name__ == '__main__':
    with open('CupcakeClubIN.txt', 'r') as f:
        while True:
            s = f.readline().strip()
            if s == '':
                break
            for i in range(int(s)):
                sa = f.readline().strip().split(" ")
                print(solve(sa[0], sa[1]))
