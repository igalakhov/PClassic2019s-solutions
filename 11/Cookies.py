from collections import *

def solve(expr):

    vals = []
    ops = ['(']

    def ev(token):
        if token.isdigit():

            if len(ops) > 0 and ops[-1] == '+':
                ops.pop()
                vals.append(vals.pop()+int(token))

            else:
                vals.append(int(token))

        elif token in 'TF':
            if token == 'T': vals.append(True)
            else: vals.append(False)

        else:
            if token == ')': casc(ops, vals)
            else: ops.append(token)

    def casc(ops, vals):

        p = len(ops)-ops[::-1].index('(')
        new_ops = ops[p:]
        for _ in range(len(ops)-p+1):
            ops.pop()

        v_i = 0
        new_vals = deque()
        for _ in range(len(new_ops)+1):
            new_vals.appendleft(vals.pop())

        ops_s = []
        vals_s = []
        vals_s.append(new_vals.popleft())

        for op in new_ops:
            vals_s.append(new_vals.popleft())
            if op == '<':
                vals_s.append(vals_s.pop() > vals_s.pop())
            elif op == '>':
                vals_s.append(vals_s.pop() < vals_s.pop())
            elif op == '=':
                vals_s.append(vals_s.pop() == vals_s.pop())

            elif op == '?':
                pass
            elif op == ':':
                c = vals_s.pop()
                b = vals_s.pop()
                a = vals_s.pop()
                vals_s.append(b if a else c)

        vals.append(vals_s.pop())
        if len(ops) > 0 and ops[-1] == '+':
            ops.pop()
            vals.append(vals.pop()+vals.pop())

    token = ''
    for ch in expr:
        if len(token) > 0 and not (token.isdigit() and ch.isdigit()):
            ev(token)
            token = ''

        token += ch

    ev(token)
    casc(ops, vals)

    return vals[0]

# Do not modify below this line
if __name__ == '__main__':
    with open('CookiesIN.txt', 'r') as f:
        T = int(f.readline().strip())
        for t in range(T):
            print(solve(f.readline().strip()))