def solution(s, skip, index):
    answer = ''
    for ss in s:
        count=0
        temp=ord(ss)
        while(True):
            temp+=1
            if temp>122:temp-=26
            if chr(temp) not in skip:
                count+=1
            if count==index:break   
        answer+=(chr(temp))
    return answer