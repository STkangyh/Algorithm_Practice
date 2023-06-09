from collections import Counter
def solution(array):
    answer = 0
    sH = Counter(array)
    maxList=[]
    for key in sH:
        if sH[key]>answer:
            answer = sH[key]
    
    for key in sH:
        if sH[key]==answer:
            maxList.append(key)
            
    return -1 if len(maxList)>1 else maxList[0]

print(solution([1,1,2,2]))
print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1,1]))