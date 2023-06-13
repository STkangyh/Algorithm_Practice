from collections import Counter
def solution(board):
    answer=0
    skylineX = [0]*len(board)
    skylineY = [0]*len(board)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]>skylineX[i]:
                skylineX[i] = board[i][j]
            if board[j][i]>skylineY[i]:
                skylineY[i] = board[j][i]
    for i in range(len(board)):
        for j in range(len(board)):
            answer += (min(skylineX[i], skylineY[j])-board[i][j])
    return answer


print(solution([[2, 5, 7, 3], [6, 8, 9, 7], [3, 2, 4, 5], [7, 2, 5, 8]]))
print(solution([[3, 7, 6, 2], [5, 3, 8, 7], [3, 2, 5, 7], [7, 7, 5, 3]]))
print(solution([[2, 5, 7, 3, 5], [6, 8, 9, 7, 3], [3, 2, 4, 5, 7], [7, 2, 5, 8, 6], [1, 2, 3, 4 ,5]]))
print(solution([[10, 11, 12, 11, 15], [15, 12, 13, 23, 11], [11, 13, 23, 25, 1], [11, 2, 3, 11, 13], [5, 7, 9, 10, 12]]))
