import sys
input = sys.stdin.readline

Stack = []
M = []
idx = 0
N = int(input())
for i in range(N):
    M.append(input().strip())

for m in M:
    if "push" in m:
        s, i = m.split()
        Stack.append(int(i))
        idx += 1
    elif "pop" in m:
        if Stack:
            print(Stack.pop())
            idx -= 1
        else:
            print(-1)  
    elif "top" in m:
        if idx > 0:
            print(Stack[idx-1])
        else:
            print(-1)
    elif "size" in m:
        print(len(Stack))
    elif "empty" in m:
        if not Stack:
            print(1)
        else:
            print(0)