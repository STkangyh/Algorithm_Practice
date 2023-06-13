def solution(keypad, password):
    answer = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    pad = [[0] * 3 for _ in range(3)]
    dist = [[2] * 10 for _ in range(10)]
    for i in range(3):
        for j in range(3):
            pad[i][j] = keypad[i*3+j]
    
    for i in range(10):
        dist[i][i] = 0

    for i in range(3):
        for j in range(3):
            s = pad[i][j]
            for k in range(8):
                if i + dx[k] >= 0 and i + dx[k] < 3 and j + dy[k] >= 0 and j + dy[k] < 3:
                    e = pad[i + dx[k]][j + dy[k]]
                    dist[s][e] = 1

    for i in range(len(password) - 1):
        a = ord(password[i]) - 48
        b = ord(password[i + 1]) - 48
        answer += dist[a][b]
         
    return answer

print(solution([2, 5, 3, 7, 1, 6, 4, 9, 8], "7596218"))
print(solution([1, 5, 7, 3, 2, 8, 9, 4, 6], "63855526592"))
print(solution([2, 9, 3, 7, 8, 6, 4, 5, 1], "323254677"))
print(solution([1, 6, 7, 3, 8, 9, 4, 5, 2], "3337772122"))

