def solution(s):
    answer = ""
    stack = []
    for i in s:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
        
    return "".join(stack)

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))
