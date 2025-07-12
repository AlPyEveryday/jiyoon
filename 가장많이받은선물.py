def solution(friends, gifts):
    answer = 0
    sunmul={}
    for f in friends:
        sunmul[f]={}
        for ff in friends:
            sunmul[f][ff]=0
            
    juda={key:0 for key in friends}
    badda={key:0 for key in friends}
    for g in gifts:
        first,last=g.split()
        sunmul[first][last]+=1
        juda[first]+=1
        badda[last]+=1
     
    jisoo={}
    for f in friends:
        jisoo[f]=juda[f]-badda[f]
        
    for f in friends:
        count=0
        for ff in friends:
            if f==ff:continue
            if sunmul[f][ff]<sunmul[ff][f]:continue
            elif sunmul[f][ff]>sunmul[ff][f]:count+=1
            else:
                if jisoo[f]>jisoo[ff]:count+=1
        if count>answer:answer=count
                    
    return answer