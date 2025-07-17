def solution(lottos, win_nums):
    answer = []
    good=0
    bad=0
    numZero=0
    for l in lottos:
        if l==0:numZero+=1
        if l!=0:
            if l in win_nums:good+=1
    best=good+numZero
    worst=good
    if best<1:best=1
    if worst<2:worst=1
    answer.append(7-best)
    answer.append(7-worst)
            
    return answer