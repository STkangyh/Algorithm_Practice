from collections import defaultdict
def solution(s):
    answer = []
    sH = {'a':0,'b':0,'c':0,'d':0,'e':0}
    for x in s:
        sH[x] += 1
    maxC = float('-inf')
    for key in sH:
        if sH[key]>maxC:
            maxC = sH[key]
    for key in sH:
        answer.append(maxC-sH[key])
    '''sH = Counter(s)
    for x in tmp:
        if sH[x]>maxC:
            maxC=sH[x]
    for x in 'abcde'
        answer.append(maxC-sH[x])
        '''
    return answer


print(solution("aaabc"))
print(solution("aabb"))
print(solution("abcde"))
print(solution("abcdeabc"))
print(solution("abbccddee"))
