A,B,C = map(int, input().split())

def sol(a,b,c):
    if b==0:
        return 1
    if b==1:
        return a%c
    if b%2==0:
        return (sol(a,b//2,c) ** 2) % c
    else:
        return ((sol(a,b//2,c) ** 2) * a) % c
 
print(sol(A,B,C))