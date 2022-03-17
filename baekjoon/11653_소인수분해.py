N=(input())
while True:
    if N <= 1:
        break
    check=0
    for i in range(2,N+1):
        if N%i==0:
            print(i)
            N//=i
            check=1
            break
    if check==0:
        break