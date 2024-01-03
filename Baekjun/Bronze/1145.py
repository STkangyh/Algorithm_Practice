N = list(map(int, input().split()))
answer = 2
while True:
    cnt = 0
    for i in N:
        if cnt>=3:
            break
        if answer%i==0:
            cnt += 1
    if cnt >= 3:
        break
    else:
        answer += 1
print(answer)