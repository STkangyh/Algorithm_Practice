N, M = map(int, input().split())
a = set()
b = set()

for _ in range(N):
    a.add(input())
for _ in range(M):
    b.add(input())

result = sorted(list(a & b))
print(len(result))
for s in result:
    print(s)