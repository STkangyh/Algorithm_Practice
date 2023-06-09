from collections import Counter
def solution(nums):
    answer = []
    sH = Counter(nums)
    for key in sH:
        if key==sH[key]:
            answer.append(key)
    answer.sort()
    return -1 if len(answer)<1 else answer[0]
                          
print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
print(solution([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))
print(solution([11, 12, 5, 5, 3, 11, 7, 12, 15, 12, 12, 11, 12, 12, 7, 8, 12, 11, 12, 7, 12, 5, 15, 20, 15, 12, 15, 12, 15, 14, 12]))
