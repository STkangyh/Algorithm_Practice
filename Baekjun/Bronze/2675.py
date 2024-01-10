T = int(input())
for i in range(T):
    n, S = input().split()
    for j in S:
        print(j*int(n), end="")
    print()