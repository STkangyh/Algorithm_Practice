from collections import defaultdict
S = defaultdict(int)
X = input()
answer = []
for i in X.lower():
    S[i] += 1
max_value = max(S.values())
for key in S:
    if S.get(key) == max_value:
        answer.append(key)
if len(answer)<2:
    print(answer.pop().upper())
else:
    print("?")