def solution(board):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    HS_x, HS_y =0,0
    Dog_x, Dog_y = 0,0
    '''HS = [HS_x][HS_y]
    Dog = [Dog_x][Dog_y]'''
    HS_dir = 0
    Dog_dir = 0
    time = 0
    dir = {"N":0, "E":1, "S":2, "W":3}
    for i in range(10):
        for j in range(10):
            if board[i][j]==2:
                HS_x, HS_y = i,j
            if board[i][j]==3:
                Dog_x, Dog_y = i,j
    while time<10000:
        time+=1
        flagHS=True
        flagDog=True
        HS_nx, HS_ny = HS_x + dx[HS_dir], HS_y + dy[HS_dir]
        Dog_nx, Dog_ny = Dog_x + dx[Dog_dir], Dog_y + dy[Dog_dir]
        if HS_nx<0 or HS_nx>=10 or HS_ny<0 or HS_ny>=10 or board[HS_nx][HS_ny]==1:
            HS_dir = (HS_dir+1)%4
            flagHS=False
        if Dog_nx<0 or Dog_nx>=10 or Dog_ny<0 or Dog_ny>=10 or board[Dog_nx][Dog_ny]==1:
            Dog_dir = (Dog_dir+1)%4
            flagDog=False
        if flagHS:
            HS_x, HS_y = HS_nx, HS_ny
        if flagDog:
            Dog_x, Dog_y = Dog_nx, Dog_ny
        if HS_x==Dog_x and HS_y==Dog_y:
            break
    if time>0:
        answer = time
    else:
        answer = 0
        
    return answer


print(solution([[0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
[0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 1, 0, 0, 0, 2, 0, 0], 
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 3, 0, 0, 0, 1], 
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
[0, 1, 0, 1, 0, 0, 0, 0, 0, 0]]))

print(solution([[1, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
[0, 0, 1, 1, 0, 0, 0, 1, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
[1, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 0, 0, 0, 0, 0, 2, 1], 
[0, 0, 0, 1, 0, 1, 0, 0, 0, 1], 
[0, 1, 0, 1, 0, 0, 0, 0, 0, 3] ]))
