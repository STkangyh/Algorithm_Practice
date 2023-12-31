import sys

T = int(input())
N = []
m = [[0],[1],[2,4,8,6],[3,9,7,1],[4,6,4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1,9,1]]
for i in range(T):
    N.append(list(map(int, sys.stdin.readline().split())))
for i in N:
    a,b = i[0]%10, i[1]
    if a==0:
        print(10)
        continue
    elif a==1 or a==5 or a==6:
        print(a)
        continue
    if b==0:
        print(1)
    else:
        print(m[a][b%4-1])