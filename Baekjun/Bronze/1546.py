import sys
input = sys.stdin.readline

n = float(input().strip())
arr = list(map(float, input().split()))
M = max(arr)
new_arr = []
for i in arr:
    new_arr.append((i/M)*100)
answer = 0
for i in new_arr:
    answer += i
print(answer/n)