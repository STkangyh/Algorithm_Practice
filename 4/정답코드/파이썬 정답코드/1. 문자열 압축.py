def solution(s):
    answer=[]
    cnt=1
    n=len(s)
    for i in range(1, n):
        if s[i-1]==s[i]:
            cnt+=1
        else:
            answer.append(s[i-1])
            if cnt>1:
                answer.append(str(cnt))
            cnt=1
    answer.append(s[-1])
    if cnt > 1:
        answer.append(str(cnt))
    return "".join(answer)

print(solution("KKHSSSSSSSE"))
print(solution("AAABCCCDD"))
print(solution("TABCEFGTT"))
print(solution("GGGGGEFFFFFFK"))
print(solution("ABCDEEFGGGHI"))
