N=int(input())
Ai=list(map(int,input().split()))
B,C=map(int,input().split())
result=0
for i in Ai:
    i-=B
    su=1
    if i>0:
        su += i//C
        if i%C !=0:
            su+=1
    result+=su
print(result)