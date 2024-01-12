S = [int(input()) for _ in range(3)]
N = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
s = S[0]*S[1]*S[2]
while s>0:
    temp = 0
    temp = s%10
    N[temp] += 1
    s = s//10
for i in N.values():
    print(i)