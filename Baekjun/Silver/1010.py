from math import comb
n = int(input())
M = [list(map(int, input().split())) for _ in range(n)]
for i in M:
    print(comb(i[1], i[0]))