def solution(c, r, k):
    if k>c*r:
        return [0,0]
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = 1
    x,y = 0,0
    cnt = 1
    seats = [[0]*r for _ in range(c)]
    while cnt<k:
        nx, ny = x+dx[dir], y+dy[dir]
        if nx<0 or nx>=c or ny<0 or ny>=r or seats[nx][ny]!=0:
            dir = (dir+1)%4
            continue
        seats[x][y]=cnt
        cnt+=1
        x,y = nx,ny
        
    return [x+1, y+1]


print(solution(6, 5, 12))
print(solution(6, 5, 20))
print(solution(6, 5, 30))
print(solution(6, 5, 31))
