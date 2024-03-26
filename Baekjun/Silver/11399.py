n = int(input())
arr = list(map(int, input().split()))
answer = 0
arr.sort(reverse=True)

for i in range(len(arr)):
    for j in range(len(arr)-1, i-1, -1):
        answer += arr[j]
print(answer)