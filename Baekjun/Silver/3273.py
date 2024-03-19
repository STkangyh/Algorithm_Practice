import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = 0
arr.sort()
L, R = 0, n-1
while L<R:
    temp = arr[L] + arr[R]
    if temp == x:
        cnt += 1
        L += 1
    elif temp > x:
        R -= 1
    else:
        L += 1
    
print(cnt)