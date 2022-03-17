# #1. 시간초과 코드
# while True:
#     n = int(input())
#     sosu=[]
#     if n==0:
#         break
#     else:
#         for i in range(n+1,2*n+1):
#             check=0 
#             for j in range(2,i):
#                 if i%j==0:
#                     check=1
#                     break
#             if check==0:
#                 sosu.append(i)
#     print(len(sosu))

#2. 정답 코드
sosu = {x for x in range(2, 246913) if x == 2 or x%2==1}
for odd_num in range(3,int(246912**(0.5)+1),2):
    sosu -= {i for i in range(2*odd_num,246913,odd_num) if i in sosu}
    
while True:
    n = int(input())
    if n == 0 :
        break
    sosu_list=[i for i in range(n+1, 2*n+1) if i in sosu]
    print(len(sosu_list)) 