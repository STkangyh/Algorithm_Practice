N = input()
num = [0 for _ in range(10)]
for i in range(len(N)):
    m = int(N[i])
    if m == 6 or m == 9:
        if num[6] <= num[9]:
            num[6] += 1
        else:
            num[9] += 1
    else:
        num[m] += 1

print(max(num))