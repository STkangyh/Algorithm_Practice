def solution(s):
    stack = []
    for x in s:
        if stack and stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)
            
    return "".join(stack)

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))
