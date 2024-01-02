S = input().split(" ")
if S[0]=="":
    S.remove("")
if S[-1]=="":
    S.remove("")
print(len(S))