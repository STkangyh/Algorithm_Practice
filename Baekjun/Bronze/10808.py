S = input()
arr = [int(0) for _ in range(26)]
for x in S:
    idx = ord(x) - ord("a")
    arr[idx] += 1
print(" ".join(str(x) for x in arr))