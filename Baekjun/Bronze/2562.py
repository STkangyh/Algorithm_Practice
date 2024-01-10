L = [int(input()) for _ in range(9)]
max_value = 0
for i in L:
    if i>max_value:
        max_value = i
print(max_value)
print(L.index(max_value)+1)