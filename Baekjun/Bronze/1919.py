import sys
input = sys.stdin.readline

A = input()
B = input()
arrA = [int(0) for _ in range(26)]
arrB = [int(0) for _ in range(26)]
for a in A:
    if a!="\n":
        idx = ord(a) - ord("a")
        arrA[idx] += 1

for b in B:
    if b!="\n":
        idx = ord(b) - ord("a")
        arrB[idx] += 1

cnt = 0
for i in range(len(arrA)):
    if arrA[i] != arrB[i]:
        cnt += abs(arrA[i]-arrB[i])
print(cnt)