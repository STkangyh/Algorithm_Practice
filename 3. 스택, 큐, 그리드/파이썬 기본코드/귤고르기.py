from collections import Counter
def solution(k, tangerine):
    answer = 0
    sH = Counter(tangerine)
    list = []
    
    for x in sH:
        list.append([x,sH[x]])
    list.sort(key = lambda v : -v[1])
    '''
    for x in sorted(sH.value(), reverse=True):
        if k>0:
            k -= x
            answer += 1
        else:
            break
    '''
    num = 0
    for x in list:
        num += x[1]
        answer += 1
        if num>=k:
            break
    return answer
print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))