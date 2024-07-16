a,b,c = map(int, input().split())

if b >= c:
    print(-1)
else:
    c -= b
    answer = a // c
    print(answer + 1)