n = int(input())
allsu = map(int,input().split())
sosu=0

for i in allsu:
    check=0
    if i >1 :
        for j in range(2,i):
            if i%j == 0:
                check=1
        if check==0: 
            sosu +=1
print(sosu) 