import sys
input = sys.stdin.readline
from collections import deque

q = deque()

n = int(input())
for i in range(n):
    m = input().strip()
    if "push" in m:
        x, y = m.split()
        q.append(int(y))
    elif "pop" in m:
        if len(q)>0:
            print(q.popleft())
        else:
            print(-1)
    elif "size" in m:
        print(len(q))
    elif "empty" in m:
        if len(q)>0:
            print(0)
        else:
            print(1)
    elif "front" in m:
        if len(q)>0:
            temp = q.popleft()
            print(temp)
            q.appendleft(temp)
        else:
            print(-1)
    elif "back" in m:
        if len(q)>0:
            temp = q.pop()
            print(temp)
            q.append(temp)
        else:
            print(-1)