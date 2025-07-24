def solution(keymap, targets):
    answer = []
    #print(ord("A")):65
    #print(ord("Z")):90
    dict={}
    for i in range(65,91):
        dict[chr(i)]=0
        
    keylen=len(keymap)
    for i in range(keylen):
        maplen=len(keymap[i])
        for j in range(maplen):
            if dict[keymap[i][j]]==0 or dict[keymap[i][j]]>j+1:
                dict[keymap[i][j]]=j+1
    
     
    for target in targets:
        count=0
        no=0
        for t in target:
            if int(dict[t])==0:
                no=1
            count+=int(dict[t])
        if no==1:answer.append(-1)
        else:answer.append(count)
               
    return answer