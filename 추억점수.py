def solution(name, yearning, photo):
    answer = []
    arrlen=len(name)
    arrlen2=len(photo)
    answer=[0]*arrlen2
    j=0
    for photoname in photo:
        for i in range(arrlen):
            if name[i] in photoname:answer[j]+=yearning[i]
        j+=1
           
    return answer