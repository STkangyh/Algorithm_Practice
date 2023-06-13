def solution(numbers, hand):
    answer = ''
    xl, yl = 3,0
    xr, yr = 3,2
    for i in numbers:
        if i%3==1:
            answer+="L"
            yl = i//3
        if i%3==0:
            answer+="R"
            yr = i//3
        if i%3==2:
            if abs((i//3)-yl)<abs((i//3)-yr):
                answer += "L"
                xl = 2
                yl = i//3
            elif abs((i//3)-yl)>abs((i//3)-yr):
                answer += "R"
                xr = 2
                yr = i//3
            else:
                if hand=="left":
                    answer += "L"
                    xl = 2
                    yl = i//3
                elif hand=="right":
                    answer += "R"
                    xr = 2
                    yr = i//3
    return answer