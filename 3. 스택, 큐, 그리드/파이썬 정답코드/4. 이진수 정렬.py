def solution(nums):
    answer = []
    res = []
    for x in nums:
        tmp = x
        cnt = 0
        while tmp > 0:
            cnt += tmp % 2
            tmp //= 2
        res.append([x, cnt])
    res.sort(key = lambda v : (v[1], v[0]))
        
    for x in res:
        answer.append(x[0])
            
    return answer
    
                                           
print(solution([5, 6, 7, 8, 9]))
print(solution([5, 4, 3, 2, 1]))
print(solution([12, 5, 7, 23, 45, 21, 17]))
