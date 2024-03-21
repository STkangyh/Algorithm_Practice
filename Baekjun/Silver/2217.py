import sys
input = sys.stdin.readline
# N은 로프의 개수, K에는 각 로프가 감당할 수 있는 최대의 무게가 저장된다.
N = int(input())
K = [int(input()) for _ in range(N)]
K.sort()
#print(K)
# 로프가 많을수록 각 로프가 감당할 무게가 줄어들기 때문에 유리함.
# 하지만 어떤 로프는 감당할 수 있는 무게가 너무 낮아서 빼는게 유리할 수도 있음.
# 그렇다면 가장 가벼운 로프가 감당할 수 있는 무게 * 로프의 개수가 최선의 결과인가?
# 그렇지 않다면 가장 가벼운 로프는 제외하고 그 다음 가벼운 로프가 감당할 수 있는 무게 * N-1
M = K[0] * N # 현재 최대로 감당할 수 있는 무게를 M으로 설정
n = N # 현재 적용되는 로프의 개수
for i in range(1, N):
    if M <= K[i]*(n-1):
        #print(M, K[i]*(n-1))
        M = K[i]*(n-1)
        n -= 1
    else:
        #print(M, K[i]*(n-1))
        n -= 1
print(M)