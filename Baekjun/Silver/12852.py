N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])

answer = [N]
now = N
temp = dp[N] - 1

for i in range(N, 0, -1):
    if dp[i] == temp and (i+1 == now or i*2 == now or i*3 == now):
        now = i
        answer.append(i)
        temp -= 1

print(*answer)