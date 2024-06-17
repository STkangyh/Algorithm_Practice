n = int(input())
a, b = map(int, input().split()) #찾아야 하는 case
m = int(input()) # 그래프 간선 개수
G = [[]*(n) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

def bfs(v):
    Q = []
    Q.append(v)
    while Q:
        start = Q.pop()
        for i in G[start]:
            if visited[i] == 0: # 방문하지 않은 노드에 방문했을 때
                visited[i] = visited[start] + 1
                Q.append(i)

bfs(a)
print(visited[b] if visited[b] else -1)