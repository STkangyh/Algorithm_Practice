n = int(input())
check = n
cnt = 1
while True:
    i = n % 10
    j = (n // 10) % 10
    k = (i+j)%10
    temp = (i*10) + k
    if temp != check:
        cnt += 1
        n = temp
        temp = 0
    else:
        break
print(cnt)