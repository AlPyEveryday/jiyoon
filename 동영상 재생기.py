def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    for c in commands:
        if int(op_start[:2]+op_start[3:5])<=int(pos[:2]+pos[3:5])<int(op_end[:2]+op_end[3:5]):
            pos=op_end[:2]+":"+op_end[3:5]
        overall=int(pos[:2])*60+int(pos[3:5])
        if c=="prev":
            if overall-10<0:
                pos="00:00"
            else:
                if len(str((overall-10)//60))==1: 
                    first="0"+str((overall-10)//60)
                else:
                    first=str((overall-10)//60)
                if len(str((overall-10)%60))==1:
                    last="0"+str((overall-10)%60)
                else:
                    last=str((overall-10)%60)
                pos=first+":"+last
        elif c=="next":
            if overall+10>int(video_len[:2])*60+int(video_len[3:5]):
                pos=video_len[:]
            else:
                if len(str((overall+10)//60))==1: 
                    first="0"+str((overall+10)//60)
                else:
                    first=str((overall+10)//60)
                if len(str((overall+10)%60))==1:
                    last="0"+str((overall+10)%60)
                else:
                    last=str((overall+10)%60)
                pos=first+":"+last 
    if int(op_start[:2]+op_start[3:5])<=int(pos[:2]+pos[3:5])<int(op_end[:2]+op_end[3:5]):
            pos=op_end[:2]+":"+op_end[3:5]
    answer=pos[:]                
    return answer