# # 10818번 최소, 최대
# N=int(input())
# numbers = list(map(int,input().split()))
# maxa=numbers[0]
# mina=numbers[0]
# for i in numbers :
#     if i > maxa :
#         maxa = i
#     elif i < mina:
#         mina = i
# print(mina, maxa)

# # 2562번 최대값
# su=[]
# for i in range(0,9):
#     su.append(int(input()))
# maxa=su[0]
# for i in su:
#     if i > maxa:
#         maxa = i
# #maxa=max(su)
# print(maxa)
# print(su.index(maxa)+1)

# #2577번 숫자의 개수
# A = int(input())
# B = int(input())
# C = int(input())
# result=list(str(A*B*C))
# for i in range(10):
#     print(result.count(str(i)))

# #3052번 나머지
# li=[]
# for i in range(10):
#     li.append((int(input()))%42)
# sli = set(li)
# print(len(sli))

# #1546번 평균
# ea = int(input())
# li = list(map(int,input().split()))
# li2 =[]
# maxa=li[0]
# for i in li:
#     if i > maxa:
#         maxa=i      
# for i in li:
#     li2.append(((i/maxa)*100))
# print(int(sum(li2))/ea)  

# #8958번 OX퀴즈
# ea = int(input())
# for i in range(ea):
#     data = input()
#     score = 0
#     point = 1
#     for i in data:
#         if i == "O":
#             score+=point
#             point+=1
#         else:
#             point = 1
#     print(score)


# #4344번 평균은 넘겠지
# nea = int(input())
# for i in range(nea):
#     score = list(map(int,input().split()))
#     average = sum(score[1:])/score[0]
#     su = 0
#     for j in score[1:]:
#         if j > average:
#             su += 1
#     re = su/score[0]*100
#     print(f"{re:.3f}%")