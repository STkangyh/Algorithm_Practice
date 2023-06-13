def solution(n):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = 1
    cnt = 1
    x,y = 0,0
    board = [[0]*n for _ in range(n)]
    while cnt<n*n:
        nx, ny = x+dx[dir], y+dy[dir]
        if nx<0 or nx>=n or ny<0 or ny>=n or board[nx][ny]!=0:
            dir = (dir+1)%4
            continue
        board[x][y]=cnt
        cnt+=1
        x,y = nx, ny
    board[x][y]=cnt
    return board