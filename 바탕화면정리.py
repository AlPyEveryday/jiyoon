def solution(wallpaper):
    answer = []
    sero=len(wallpaper)
    garo=len(wallpaper[0])
    
    smallX=-1
    smallY=-1
    bigX=-1
    bigY=-1
    
    for i in range(sero):
        for j in range(garo):
            if wallpaper[i][j]=="#":
                if smallX==-1 or i<smallX:smallX=i
                if bigX==-1 or i>bigX:bigX=i
                if smallY==-1 or j<smallY:smallY=j
                if bigY==-1 or j>bigY:bigY=j
    
    bigX+=1
    bigY+=1
    answer.append(smallX)
    answer.append(smallY)
    answer.append(bigX)
    answer.append(bigY)
    
    return answer