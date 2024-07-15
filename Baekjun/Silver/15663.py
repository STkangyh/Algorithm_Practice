N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []
visited = [False] * N

def dfs():
    if len(s) == M:
        print(*s)
        return
    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != arr[i]:
            visited[i] = True
            s.append(arr[i])
            overlap = arr[i]
            dfs()
            visited[i] = False
            s.pop()

dfs()