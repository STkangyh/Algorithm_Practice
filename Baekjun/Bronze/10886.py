n = int(input())
cnt = 0
for i in range(n):
    k = int(input())
    if k == 1:
        cnt += 1
if cnt*2 > n:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")