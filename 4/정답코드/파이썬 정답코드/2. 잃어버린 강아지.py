def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(10):
        for j in range(10):
            if board[i][j] == 2:
                x1 = i
                y1 = j
            if board[i][j] == 3:
                x2 = i
                y2 = j
    count = 0
    d1 = 0
    d2 = 0
    while count < 10000:
        count+=1
        nx1, ny1 = x1 + dx[d1], y1 + dy[d1]
        nx2, ny2 = x2 + dx[d2], y2 + dy[d2]
        flag1 = True
        flag2 = True
        if nx1 < 0 or nx1 >= 10 or ny1 < 0 or ny1 >= 10 or board[nx1][ny1] == 1:
            d1 = (d1 + 1) % 4
            flag1 = False
        if nx2 < 0 or nx2 >= 10 or ny2 < 0 or ny2 >= 10 or board[nx2][ny2] == 1:
            d2 = (d2 + 1) % 4
            flag2 = False

        if flag1:
            x1, y1 = nx1, ny1
        if flag2:
            x2, y2 = nx2, ny2

        if x1 == x2 and y1 == y2:
            break

    if count >= 10000:
        count = 0
        
    return count


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

