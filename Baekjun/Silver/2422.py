N, M = map(int, input().split())
A = [[0 for _ in range(N+1)] for _ in range(N+1)]
T = 0
for _ in range(M):
    a, b = map(int, input().split())
    A[a+1][b+1] = 1
    A[b+1][a+1] = 1
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if(A[i][j]==0):
            for k in range(j+1, N+1):
                if(A[j][k]==0 and A[i][k]==0):
                    T += 1
print(T)