n, k = list(map(int, input().split())) # n은 입력받을 코인의 개수, k는 동전 가치의 합
coin = [int(input()) for _ in range(n)] # 한 줄에 코인의 입력 가치 하나씩 입력 받음
# 피보나치 수열을 트리로 나타낸 것처럼 표현하면 모든 가짓수를 찾을 수 있음
# 모든 값은 작은 수의 덧셈으로 이루어져 있음
dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in coin:
    for j in range(i, k+1):
        if j-i>=0:
            dp[j] += dp[j-i]
#print(dp)
print(dp[k])