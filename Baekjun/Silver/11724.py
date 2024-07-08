import sys
sys.setrecursionlimit(100000)
N, M = map(int, sys.stdin.readline().strip().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = 0

def dfs(v):
    #print("dfs 실행")
    visited[v] = True
    #print(arr[v])
    #print(visited)
    for i in arr[v]:
        #print(f'{v}의 {i} 확인중')
        if not visited[i]:
            #print(f'{v}의 {i} 미확인')
            dfs(i)
                
for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)