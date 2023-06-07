def solution(park, routes):
    answer = []
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]
    d={'N':0, 'E':1, 'S':2, 'W':3}
    x,y=0,0
    n=len(park)
    m=len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j]=='S':
                x,y=i,j
    nx,ny=x,y
    for tmp in routes:
        dir, dis = tmp.split(' ')
        flag=True
        for i in range(1, int(dis)+1):
            nx, ny = nx + dx[d[dir]], ny + dy[d[dir]]
            if nx<0 or ny<0 or nx>=n or ny>=m or park[nx][ny]=='X':
                flag=False
                break
        if flag:
            x,y=nx,ny 
    return [x,y]

print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))