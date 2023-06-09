def solution(moves):
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]
    dir=1
    x, y = 0, 0
    for c in moves:
        if c=='G':
            x = x + dx[dir]
            y = y + dy[dir]
        elif c=='R':
            dir = (dir+1) % 4
        elif c=='L':
            dir = (dir+3) % 4 #python에서는 (dir-1)%4 해도 괜찮음
    return [x, y]

print(solution('GGGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))