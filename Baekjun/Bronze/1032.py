n = int(input())
S = [list(input()) for _ in range(n)]
A = ["" for _ in range(len(S[0]))]
if n==1:
    print(''.join(S[0]))
for i in range(n-1):
    for j in range(len(S[0])):
        if A[j]!='?':
            A[j]=S[i][j] if S[i][j]==S[i+1][j] else '?'
print(''.join(A))