import sys
input = sys.stdin.readline

n = int(input())
S = []
L = []
li = 0
answer = []
for i in range(n):
    l = int(input())
    L.append(l)
    S.append(i+1)
    answer.append("+")
    while L[li] <= S[-1]:
        answer.append("-")
        S.pop()
        if li<n:
            li+=1
        if li==n:
            break
        if not S:
            break
if S:
    print("NO")
else:
    for i in range(len(answer)):
        print(answer[i]) 
