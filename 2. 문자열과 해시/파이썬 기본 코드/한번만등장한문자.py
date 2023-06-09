from collections import Counter
def solution(s):
    answer = []
    sH = Counter(s)
    for key in sH:
        if sH[key]==1:
            answer.append(key)
    return "".join(sorted(answer))