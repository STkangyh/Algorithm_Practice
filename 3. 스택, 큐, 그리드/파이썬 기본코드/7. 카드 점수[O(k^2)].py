def solution(nums, k):
    answer = 0
    first, last=0, len(nums)-1
    
    #그리드 알고리즘으로하면 정확한 값이 나오지 않음.
    #그리드에 예외 케이스를 추가한다.
    #first+k or last-k 번째까지 first, last에서 더해가면서 두 값 중 큰 것을 선택.
    for i in range(k):
        num1, num2 = 0, 0
        for j in range(first+1):
            num1 += nums[first+j]
        for j in range(len(nums)-last):
            num2 += nums[last]
        if num1 >= num2:
            last -= 1
        elif num2 > num1:
            first += 1
    answer = num1 + num2
    
    return answer
                           
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))
