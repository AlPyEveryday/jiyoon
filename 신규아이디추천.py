def solution(new_id):
    answer = ''
    #print(ord("a")):97
    #print(ord("z")):122
    #print(ord("A")):65
    #print(ord("Z")):90
    #print(ord("0")):48
    #print(ord("9")):57
    arr1=[]
    for n in new_id:
        if 65<=ord(n)<=90:
            arr1.append(chr(ord(n)+32))
        else:
            arr1.append(n)
    arr2=[]        
    for n in arr1:
        if n=="-" or n=="_" or n=="." or 48<=ord(n)<=57 or 97<=ord(n)<=122:
            arr2.append(n)
    arr3=[]
    i=0
    arr2.append("x")
    while(i<len(arr2)-1):
        arr3.append(arr2[i])
        if arr2[i]==".":
            while(True):
                if arr2[i+1]==".":i+=1
                else:break
        i+=1
    #while '..' in answer:
     #   answer = answer.replace('..', '.')
        #너무 좋은 거 같아 적어봅니다..
    if arr3!=[] and arr3[0]==".":
        arr3.pop(0)
    if arr3!=[] and arr3[-1]==".":
        arr3.pop(-1)
    arr4=arr3[:]
    
    if arr4==[]:arr4.append("a")
    arr5=arr4[:]
    
    arr6=[]
    if len(arr5)>=16:
        arr6=arr5[:15]
    else:
        arr6=arr5[:]
    if arr6[-1]==".":
        arr6.pop(-1)
    
    arr7=[]
    if len(arr6)<=2:
        for i in range(3-len(arr6)):
            arr6.append(arr6[-1])
    arr7=arr6[:]
    
    for a in arr7:
        answer+=str(a)
            
    return answer