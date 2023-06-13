def solution(m, nums):
    answer = 0
    nums.sort(key = lambda v : v[0])
    #끝 숫자가 큰 것을 찾는다
    '''min_list = []
    for x in nums:
        maxC = 0
        if x[1]>maxC:'''
    i=0
    start, end = 0,0
    while i<len(nums):
        while i<len(nums) and nums[i][0] <= start:
            end = max(end, nums[i][1])
            i += 1
        answer += 1
        if end == m:
            return answer
        start = end     
    return answer 
    #LeetCode 1326 과제
                                           
print(solution(12, [[5, 10], [1, 8], [0, 2], [0, 3], [2, 5], [2, 6], [10, 12], [7, 12]]))
print(solution(15, [[1, 10], [0, 8], [0, 7], [0, 10], [5, 12], [0, 12], [8, 15], [5, 14]]))
print(solution(20, [[3, 7], [5, 8], [15, 20], [0, 5], [7, 14], [3, 10], [0, 8], [13, 18], [5, 9]]))
print(solution(30, [[5, 7], [3, 9], [2, 7], [0, 1], [0, 2], [0, 3], [19, 30], [8, 15], [7, 12], [13, 20]]))
print(solution(25, [[10, 15], [15, 20], [5, 15], [3, 16], [0, 5], [0, 3], [12, 25]]))
