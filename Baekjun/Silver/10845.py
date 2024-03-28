import sys
input = sys.stdin.readline

N = int(input())
Q = []
M = []
s, e = 0, 0

for i in range(N):
    m = input().strip()
    M.append(m)

for x in M:
    if "push" in x:
        n, i = x.split()
        Q.append(int(i))
        e += 1
    elif "pop" in x:
        if Q:
            print(Q[s])
            Q.remove(Q[s])
            e -= 1
        else:
            print(-1)
            s, e = 0,0
    elif "size" in x:
        print(e-s)
    elif "empty" in x:
        if Q:
            print(0)
        else:
            print(1)
    elif "front" in x:
        print(Q[s]) if Q else print(-1)
    elif "back" in x:
        print(Q[e-1]) if Q else print(-1)