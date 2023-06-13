def solution(nums):
    answer = []
    binarylist = []
    for i in nums:
        temp = i
        cnt = 0
        while temp>0:
            cnt += (temp%2)
            temp = temp // 2
        binarylist.append([i,cnt])
    
    binarylist.sort(key = lambda v : (v[1], v[0]))
    for i in binarylist:
        answer.append(i[0])
    return answer
    
                                           
print(solution([5, 6, 7, 8, 9]))
print(solution([5, 4, 3, 2, 1]))
print(solution([12, 5, 7, 23, 45, 21, 17]))
