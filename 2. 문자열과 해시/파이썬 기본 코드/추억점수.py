from collections import Counter, defaultdict
def solution(name, yearning, photo):
    answer = []
    sH = defaultdict(int)
    for i in range(len(name)):
        sH[name[i]]=yearning[i]
    for x in photo:
        sum=0
        for person in x:
            sum += sH[person]
        answer.append(sum)
    return answer

