def solution(nums, k):
    total = sum(nums)
    m = len(nums) - k
    score = 0
    for i in range(m):
        score += nums[i]
    minS = score
    left = 0
    for right in range(m, len(nums)):
        score += (nums[right] - nums[left])
        left += 1
        minS = min(minS, score)

    return total - minS
        
                                         
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))
