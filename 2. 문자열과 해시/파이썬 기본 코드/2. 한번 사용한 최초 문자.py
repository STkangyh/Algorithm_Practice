from collections import Counter
def solution(s):
    '''answer = 0
    sH = defaultdict(int)
    for x in s:
        sH[x] += 1
    for key in sH:
        if sH[key]==1:
            index = list(sH).index(key)
            answer = index+1
            break
        else:
            answer = -1'''
    answer = -1
    sH = Counter(s)
    for i in range(len(s)):
        if sH[s[i]]==1:
            return i+1
    return answer


print(solution("statitsics"))
print(solution("aabb"))
print(solution("stringshowtime"))
print(solution("abcdeabcdfg"))


