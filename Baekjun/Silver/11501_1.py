import sys
input = sys.stdin.readline

T = int(input())
L = [[] for _ in range(T)]

for i in range(T):
    N = int(input())
    L[i] = list(map(int, input().split()))
    M = 0
    answer = 0
    for j in range(N-1, -1, -1):
        if L[i][j] <= M:
            answer += M - L[i][j]
        else:
            M = L[i][j]
    print(answer)