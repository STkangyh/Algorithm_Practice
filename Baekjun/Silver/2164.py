import sys
input = sys.stdin.readline
from collections import deque

q = deque()

n = int(input())
for i in range(n):
    q.append(i+1)
while len(q)>1:
    q.popleft()
    q.append(q.popleft())
print(q.pop())