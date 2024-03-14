N, K = map(int, input().split())
arr = [[0]*2 for _ in range(6)]

for i in range(N):
    s, y = map(int, input().split())
    arr[y-1][s] += 1

room = 0

for i in range(6):
    for j in range(2):
        if arr[i][j]%K == 0:
            room += arr[i][j] // K
        else:
            room += (arr[i][j] // K) + 1

print(room)