import sys
input = sys.stdin.readline

K = int(input())
S = [0 for _ in range(K)]
idx = 0
for i in range(K):
    k = int(input())
    if k != 0:
        S[idx] = k
        idx += 1
        #print(S, idx)
    else:
        idx -= 1
        S[idx] = 0
        #print(S, idx)
answer = 0
for j in S:
    answer += j
print(answer)