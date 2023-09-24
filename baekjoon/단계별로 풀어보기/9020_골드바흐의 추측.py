# #1. 시간초과 코드
# sosu = {x for x in range(2, 10001) if x ==2 or x%2==1}
# for odd_num in range(3, int(10001**(0.5)+1),2):
#     sosu -= {i for i in range(2*odd_num, 10001, odd_num) if i in sosu}
# n=int(input())
# for _ in range(n):
#     x = int(input())
#     sosu_x = [i for i in sosu if i<=x]
#     check=0
#     for i in range(0,len(sosu_x)-1):
#         for j in range(0,i+1):
#             if(sosu_x[i] + sosu_x[j] == x):
#                 if(sosu_x[i]>sosu_x[j]):
#                     print(sosu_x[j], sosu_x[i])
#                     check=1
#                     break
#                 print(sosu_x[i], sosu_x[j])
#                 check=1
#                 break
#         if check==1:
#             break
        
#2. 정답 코드
sosu = {x for x in range(2, 10001) if x==2 or x%2==1}
for odd_num in range(3, int(10000**(0.5)+1),2):
    sosu -= {i for i in range(2*odd_num, 10001, odd_num) if i in sosu}
n=int(input())
for _ in range(n):
    x = int(input())
    a = x//2
    for k in range(a, 1, -1):
        if (k in sosu) and (x-k in sosu):
            print(k,x-k)
            # break