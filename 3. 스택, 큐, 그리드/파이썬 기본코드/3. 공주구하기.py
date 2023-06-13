from collections import deque
def solution(n, k):
    answer = 0
    prince = range(1, n+1) #1부터 n+1개 까지
    queue = deque(prince)
    while queue:
        for i in range(k-1):
            queue.append(queue.popleft()) #앞에서부터 k-1개까지 pop하고 뒤로 append
        queue.popleft() #다음 pop할 대상은 k번째
        if len(queue)==1: #pop하다 1개만 남으면 answer 확보
            answer = queue.popleft()
    return answer


print(solution(8, 3))
print(solution(20, 3))
print(solution(100, 5))


