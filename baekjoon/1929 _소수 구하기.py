def isPrime(i):
    if i>1:
        for j in range(2,int(i**(0.5))+1):
            if i%j==0:
                 return False
        return True
    else:
        return False

M,N =map(int,input().split())
for i in range(M,N+1):
    if isPrime(i):
        print(i)   