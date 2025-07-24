def solution(today, terms, privacies):
    answer = []
    dict={}
    for t in terms:
        first,last=t.split()
        dict[first]=last
    
    todayYear=int(today[:4])
    todayMonth=int(today[5:7])
    todayDay=int(today[8:10])
    number=1
    for p in privacies:
        year=int(p[:4])
        month=int(p[5:7])
        day=int(p[8:10])
        year+=(int(dict[p[11]]))//12
        month+=(int(dict[p[11]]))%12
        if month>12:
            month-=12
            year+=1
        if day==1:
            day=28
            month-=1
        else:
            day-=1
        plag=0
        if year<todayYear:plag+=1
        if year==todayYear and month<todayMonth:plag+=1
        if year==todayYear and month==todayMonth and day<todayDay:plag+=1
        if plag!=0:answer.append(number)
        number+=1
        
    return answer