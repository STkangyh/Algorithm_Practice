def solution(s):
    stack = []
    for i in s:
        if i=='#': #python에서 자료가 있으면 True이기 때문에 stack만 표기 가능
            if stack:
                stack.pop()
        else:
            stack.append(i)
    
    return "".join(stack)
            
          
print(solution("#abc##ec#ab"))
print(solution("kefd#ef##s##"))
print(solution("teac#cher##er"))
print(solution("englitk##shabcde##ff##ef##ashe####"))
print(solution("itistime####gold"))
