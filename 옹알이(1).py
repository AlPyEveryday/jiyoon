def solution(babbling):
    answer = 0
    arrlen=len(babbling)
    for i in range(arrlen):
        j=0
        wrong=0
        arrlen2=len(babbling[i])
        while(1):
            if j>=arrlen2:
                break 
            if babbling[i][j]=='a':
                if 'aya' in babbling[i][j:j+3]:
                    j+=3
                else:
                    wrong=1
                    break
            elif babbling[i][j]=='y':
                if 'ye' in babbling[i][j:j+2]:
                    j+=2
                else:
                    wrong=1
                    break
            elif babbling[i][j]=='w':
                if 'woo' in babbling[i][j:j+3]:
                    j+=3
                else:
                    wrong=1
                    break
            elif babbling[i][j]=='m':
                if 'ma' in babbling[i][j:j+2]:
                    j+=2
                else:
                    wrong=1
                    break
            else:
                wrong=1
                break
        if wrong==0:answer+=1
                    
                
    return answer