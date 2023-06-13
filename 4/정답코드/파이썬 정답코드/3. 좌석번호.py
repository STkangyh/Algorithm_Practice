def solution(c, r, k):
    if k > c * r:
        return [0, 0]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    seat = [[0]*r for _ in range(c)] 
    d = 1
    count = 1
    x, y = 0, 0
    while count < k:
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= c or ny < 0 or ny >= r or seat[nx][ny] != 0:
            d = (d + 1) % 4
            continue
        seat[x][y] = count
        count += 1
        x, y = nx, ny  
    return [x+1, y+1]


print(solution(6, 5, 12))
print(solution(6, 5, 20))
print(solution(6, 5, 30))
print(solution(6, 5, 31))
