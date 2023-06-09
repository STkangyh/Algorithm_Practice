from collections import defaultdict, Counter
def solution(s):
    answer = ""
    sH = defaultdict(int)
    #sH = Counter(s)
    for x in s:
        sH[x] += 1
    maxC = float('-inf')
    for key in sH:
        if sH[key]>maxC:
            maxC = sH[key]
            answer = key
    return answer


print(solution("BACBACCACCBDEDE"))
print(solution("AAAAABBCCDDDD"))
print(solution("AABBCCDDEEABCB"))


