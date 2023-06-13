from collections import Counter
def solution(input_string):
    answer = ''
    hash = []
    hash.append(input_string[0])
    for i in range(1,len(input_string)):
        if input_string[i-1]!=input_string[i]:
            hash.append(input_string[i])
    sH = Counter(sorted(hash))
    for x in sH:
        if sH[x]>1:
            answer+=x
    if answer == "":
        answer = "N"
    return answer

print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))