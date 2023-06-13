def solution(rank, attendance):
    answer = 0
    res = []
    for x in range(len(rank)):
        if attendance[x]:
            res.append([rank[x],x])
    print(res)
    res.sort(key = lambda v : v[0])
    print(res)
    answer += res[0][1]*10000
    answer += res[1][1]*100
    answer += res[2][1]
    return answer
print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))