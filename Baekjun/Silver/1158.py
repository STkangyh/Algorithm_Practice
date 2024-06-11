import sys
input = sys.stdin.readline
from collections import deque

deq = deque()

n, k = map(int, input().split())
answer = []
for i in range(1, n+1):
    deq.append(i)

for i in range(n):
    for j in range(k-1):
        deq.append(deq.popleft())
    answer.append(deq.popleft())
print('<'+', '.join(map(str, answer)) + '>')