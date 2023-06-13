def solution(s):
    answer=[]
    s = s + " "
    cnt = 1
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            cnt+=1
        else:
            answer.append(s[i-1])
            if cnt>1:
                answer.append(str(cnt))
            cnt = 1  
    
    return "".join(answer)

print(solution("KKHSSSSSSSE"))
print(solution("AAABCCCDD"))
print(solution("TABCEFGTT"))
print(solution("GGGGGEFFFFFFK"))
print(solution("ABCDEEFGGGHI"))
