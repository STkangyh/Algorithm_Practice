import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = []

def finding(x, y, N):
    temp = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if arr[i][j] != temp:
                finding(x, y, N//2)
                finding(x, y+N//2, N//2)
                finding(x+N//2, y, N//2)
                finding(x+N//2, y+N//2, N//2)
                return
    if temp == 0:
        answer.append(0)
    else:
        answer.append(1)

finding(0,0,N)
print(answer.count(0))
print(answer.count(1))