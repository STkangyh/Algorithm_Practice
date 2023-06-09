def solution(board):
    answer=0
    n = len(board)
    answer=n*n
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(n):
        for j in range(n):
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx>=0 and nx<n and ny>=0 and ny<n and board[nx][ny]==1 or board[i][j]==1: 
                    answer-=1
                    print(nx, ny)
                    break
    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))