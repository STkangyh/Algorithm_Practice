from collections import deque
def solution(n, k):
    answer = 0
    prince = range(1, n+1)
    queue = deque(prince)
    
    while queue:
        for i in range(k-1):
            queue.append(queue.popleft())
        queue.popleft()
        if len(queue) == 1:
            answer = queue.popleft()
                   
    return answer


print(solution(8, 3))
print(solution(20, 3))
print(solution(100, 5))


