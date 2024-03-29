import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    stack = []
    s = list(input().strip())

    for j in s:
        if stack and stack[-1]!=j:
            if stack[-1] == "(" and j == ")":
                del stack[-1]
        else:
            stack.append(j)
    if stack:
        print("NO")
    else:
        print("YES")
    