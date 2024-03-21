import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [0 for _ in range(N)]
cnt = 0
for i in range(N):
    A[i] = int(input())

for i in range(len(A)):
    if A[i] <= K:
        idx = i
    else:
        break

while K > 0 or idx >= 0:
    if K < A[idx]:
        idx -= 1
    elif K >= A[idx]:
        cnt += K // A[idx]
        K %= A[idx]
    if K == 0:
        break

print(cnt)