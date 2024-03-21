# 투자 원칙
# 1. 갖고 있는 주식이 없을 때
# 2. 갖고 있는 주식이 있을 때
# 1-1 지금의 주가보다 더 높은 날이 없어 -> 응 안사
# 1-2 지금의 주가보다 더 높은 날이 있어 -> 사고 존버
# 2-1 가장 주가가 높은 날에만 팔아

T = int(input())
L = [[] for _ in range(T)]
S = [[] for _ in range(T)] # 매도하는 날

for i in range(T):
    N = int(input())
    L[i] = list(map(int, input().split()))
    S[i] = sorted(L[i], reverse=True)

for i in range(T):
    answer = 0
    SI = 0 # 매도 날짜 인덱스
    for j in range(len(L[i])):
        if L[i][j] >= S[i][SI]:
            SI += 1
            #print("SI=" + f'{SI}')
            continue
        else:
            answer += S[i][SI] - L[i][j]
            #print('S'+f'{S[i][SI]}'+'-'+'L'+f'{L[i][j]}')
    print(answer)