import math
n=int(input())
for _ in range(n):
    a,b,r1,x,y,r2=map(int,input().split())
    r = math.sqrt((x-a)**2 + (y-b)**2)
    if r==0 and r1==r2:
        print(-1)
    elif abs(r1-r2) < r < r1+r2:
        print(2)
    elif r1+r2 == r or abs(r1-r2)==r:
        print(1)
    else:
        print(0)