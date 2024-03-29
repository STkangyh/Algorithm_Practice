import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(n):
    s = list(input().strip())
    Stack = []

    for i in s:
        if Stack and Stack[-1] == i:
            del Stack[-1]
        else:
            Stack.append(i)
    if Stack:
        continue
    else:
        answer += 1
print(answer)
