import sys
input = sys.stdin.readline

n = int(input())
T = list(map(int, input().split()))
stack = []
answer = [0 for _ in range(n)]

for i in range(n):
    while stack:
        if T[stack[-1][0]] < T[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0] + 1
            break
    stack.append((i, T[i]))

print(*answer)