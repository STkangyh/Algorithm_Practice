from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    sH_reported = defaultdict(int)
    sH_reporter = defaultdict(int)
    report = list(set(report))
    for temp in report:
        reporter, reported = temp.split(' ')
        sH_reported[reported]+=1
        if k<=sH_reported[reported]:
            sH_reporter[reporter]+=1
    '''report = list(set(report))
    reportHash = defaultdict(set) #set형인 dictionary
    stoped = defaultdict(int)
    for x in report:
        a,b = x.split(' ')
        reportHash[a].add(b)
        stoped[b]+=1
    for name in id_list:
        mail=0
        for user in reportHash[name]:
            if stoped[user]>=k:
                mail+=1
        answer.append(mail)'''
    return answer
