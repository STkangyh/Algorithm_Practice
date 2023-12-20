S = [input() for _ in range(1000)]
answer = 0
digits = {
    "one" : 1,
    "two" : 2, 
    "three" : 3,
    "four" : 4, 
    "five" : 5, 
    "six" : 6, 
    "seven" : 7, 
    "eight" : 8, 
    "nine" : 9
    }
for x in S:
    if x == "":
        break
    temp = []
    check = ""
    print(x)
    for i in x:
        if i.isdigit():
            temp.append(int(i))
            print(i)
        else:
            check += i
            for digit, number in digits.items():
                if check.endswith(digit):
                    temp.append(number)
                    print(number)
                    check = check[-1]

    if len(temp) > 1:
        answer += 10*temp[0] + temp[-1]
        print(10*temp[0]+temp[-1])
    if len(temp) == 1:
        answer += 10*temp[0] + temp[0]
        print(10*temp[0]+temp[0])
print(answer)