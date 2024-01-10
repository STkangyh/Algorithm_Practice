n = int(input())
for i in range(n):
    for j in range(n):
        if i < n-j-1:
            print(" ", end="")
        else:
            print("*", end="")
    print() if i<n-1 else 0