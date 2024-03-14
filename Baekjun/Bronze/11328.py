N = int(input())

for i in range(N):
    a, b = map(str, input().split())
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    if len(a) != len(b):
        print("Impossible")
        continue
    for j in range(len(b)):
        if a[j] != b[j]:
            flag = False
            break
        else:
            flag = True
    if flag:
        print("Possible")
    else:
        print("Impossible")