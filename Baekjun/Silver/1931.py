import sys
input = sys.stdin.readline

N = int(input())
T = [[0]*2 for _ in range(N)]

for i in range(N):
    S, E = map(int, input().split())
    T[i][0] = S
    T[i][1] = E

T.sort(key=lambda x : x[1]) # 시작 시간을 기준으로 정렬 -> 일찍 끝나야지 다음 회의 진행하니까 끝나는 시간으로 배열 정렬
# 다른 코드를 보면 시작하는 시간도 오름차순으로 정리하는데 굳이 왜 해야함?
# 1. 회의실 사용 시간은 가능한 짧을것
# 2. 선택된 시간이 종료되기 전에 시작되는 회의는 무시
# 3. 첫번째 회의 끝나는 시간 <= 두번째 회의 시작
F = 0 # 첫번째 회의 초기값 설정
answer = 0
for s,e in T:
    if F <= s:
        answer += 1
        F = e

print(answer)