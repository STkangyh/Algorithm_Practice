def solution(board, moves):
    answer = 0
    stack = []
    for x in moves:
        for i in range(len(board[0])):
            if board[i][x-1]!=0: #뽑은 자리에 값이 있을 때
                if stack and stack[-1]==board[i][x-1]: #board[i][x-1]을 저장할 변수를 생성하고 board를 삭제할 것인가, 동일 코드를 두 번 쓸 것인가
                    stack.pop()
                    board[i][x-1]=0
                    answer+=2
                else:
                    stack.append(board[i][x-1])
                    board[i][x-1]=0
                break
    return answer
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))