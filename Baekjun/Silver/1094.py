X = int(input())
S = [0 for _ in range(10)]
L = 0
S[L] = 64
while True:
    '''
    1. 갖고 있는 모든 막대 길이 더해서 X와 비교
    2. X보다 클 때는
    2-1. 갖고 있는 막대 중 가장 작은 막대를 반으로 자르고
    2-2. 자른 막대의 반을 버리고 나머지 막대들의 합이 X보다 크거나 같으면 자른 막대의 반을 버린다.
    3. 모든 막대를 붙여 X를 만든다.
    '''
    temp1 = 0
    for i in S:
        temp1 += i
    '''print(temp1, "1번 과정")'''
    if temp1 > X:
        S[L], S[L+1] = S[L]//2, S[L]//2
        L += 1
        '''print(L, S, "2-1번 과정")'''
        temp2 = 0
        for j in range(L):
            temp2 += S[j]
            '''print(temp2, "2-2번 과정")'''
        if temp2 >= X:
            S[L] = 0
            L -= 1
    temp3 = 0
    for k in S:
        temp3 += k
    if temp3 == X:
        break
    else:
        '''print(S, "3번 과정")'''
cnt = 0
for i in S:
    if i>0:
        cnt += 1
print(cnt)