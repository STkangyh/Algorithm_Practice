from collections import deque
q = deque()
q.appendleft(1)
visited = []
def bfs(x):
    cnt = 0
    q.appendleft(x)
    visited[x] = False
    while q:
        k = q.popleft()
        for i in range(1, n+1):
            if arr[k][i] > 0 and visited[i]:
                visited[i] = False
                q.append(i)
                cnt += 1
    return cnt

n = int(input())
m = int(input())
visited = [True for _ in range(n+1)]
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
print(bfs(1))