from collections import deque
def solution(s,e):
    answer = 0
    ch = [0]*10001
    Q = deque()
    Q.append(s)
    ch[s]=1
    L=0
    while(Q):
        length = len(Q)
        for _ in range(length):
            v = Q.popleft()
            for nv in [v-1, v+1, v+5]:
                Q.append(nv)
                if nv == e:
                    return L+1
                if nv>0 and nv<=10000 and ch[nv]==0:
                    ch[nv]=1
                    Q.append(nv)
        L += 1
    return answer
print(solution(5,14))
print(solution(8,3))