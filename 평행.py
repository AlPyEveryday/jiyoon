def solution(dots):
    answer = 0
    x=[0]*10
    y=[0]*10
    for i in range(1,5):
        x[i]=dots[i-1][0]
        y[i]=dots[i-1][1]
    if (y[2]-y[1])/(x[2]-x[1])==(y[4]-y[3])/(x[4]-x[3]):answer=1
    if (y[3]-y[1])/(x[3]-x[1])==(y[4]-y[2])/(x[4]-x[2]):answer=1
    if (y[4]-y[1])/(x[4]-x[1])==(y[2]-y[3])/(x[2]-x[3]):answer=1
    return answer
#평행과제 