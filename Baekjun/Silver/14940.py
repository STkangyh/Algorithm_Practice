import sys
from collections import deque
q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, sys.stdin.readline().strip().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().strip().split()))

def bfs(x, y):
    visited[x][y] = 0
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif arr[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[a][b] + 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()