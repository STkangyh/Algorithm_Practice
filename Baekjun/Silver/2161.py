from collections import deque

q = deque()
n = int(input())

for i in range(n):
    q.append(i+1)
arr = []

while q:
    arr.append(q.popleft())
    if not q:
        break
    q.append(q.popleft())
    if not q:
        break
print(*arr)