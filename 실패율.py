def solution(N, stages):
    answer = []
    stages.sort() #1 2 2 2 3 3 4 4 4 7 8 9 총 12명
    people=len(stages)
    latest=people
    latestIndex=0
    fail={key:0 for key in range(1,N+1)}
    for i in range(1,N+1):
        if i in stages:
            bunmo=people-stages.index(i)
            latest=bunmo
            latestIndex=i
        else:
            bunmo=latest-stages.count(latestIndex)
        bunja=stages.count(i)
        if bunmo==0:fail[i]=0
        else:fail[i]=bunja/bunmo
    answer=[k for k,v in sorted(fail.items(), key=lambda item:item[1],reverse=True)] #dict sort   
    return answer