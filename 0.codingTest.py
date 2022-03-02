# #입출력과 사칙연산

# print("HelloWorld")

# print("강한친구 대한육군\n강한친구 대한육군")

# print("\\    /\\\n )  ( \')\n(  /  )\n \\(__)|")

# print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")

# A, B = map(int,input().split())
# print(A+B)

# A, B = map(int,input().split())
# print(A-B)

# A, B = map(int,input().split())
# print(A*B)

# A, B = map(float,input().split())
# print(A/B)

# A,B = map(int,input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)

# A, B, C = map(int,input().split())
# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))%C)

# A=int(input())
# B=int(input())

# print(A*(B%10))
# print(A*(B//10%10))
# print(A*(B//100))
# print(A*B)









# #if문

# #1330 두 수 비교하기
# A,B=map(int,input().split())
# if A>B:
#     print(">")
# elif A<B:
#     print("<")
# else:
#     print("==")

# #9498 시험 성적
# A=int(input())

# if 100>=A>=90:
#     print('A')
# elif 90>A>=80:
#     print('B')
# elif 80>A>=70:
#     print('C')
# elif 70>A>=60:
#     print('D')
# else:
#     print("F")


# #2753 윤년
# A=int(input())

# if  A%4==0 and A%100!=0 or A%400==0:
#     print("1")
# else:
#     print("0")


# #14681번 사분면 고르기
# x=int(input())
# y=int(input())

# if x>0 and y>0:
#     print("1")
# elif x<0 and y>0:
#     print("2")
# elif x<0 and y<0:
#     print("3")
# elif x>0 and y<0:
#     print("4")


# #2884 알람시계
# a, b = map(int,input().split())

# if a>0 and b-45 < 0:
#     print(a-1, b-45+60)
# elif a==0 and b-45<0:
#     print(a+23, b-45+60)
# else:
#     print(a, b-45)










# #for문

# #2739번 구구단
# N = int(input())
# for i in range(1,10):
#     print(N,"*",i,"=",N*i)

# #10950번 A+B-3

# N =int(input())

# for i in range(N):
#     a, b = map(int,input().split())
#     print(a+b)

# #8393번 합

# N = int(input())
# sum = 0

# for i in range(1,N+1):
#     sum += i
# print(sum)

# #15552번 빠른A+B
# import sys

# N = int(input())
# for i in range(N):
#     A, B = map(int, sys.stdin.readline().split())
#     print(A+B)

# #2741번 N찍기
# N = int(input())
# for i in range(1,N+1):
#     print(i)
    
# # 2742번 기찍N
# N = int(input())
# for i in range(N,0,-1):
#     print(i)

# # 11021 A+B -7
# N = int(input())
# for i in range(1,N+1):
#     a, b = map(int,input().split())
#     print(f"Case #{i}:", a+b) 
    
# # 11022 A+B -8
# N = int(input())
# for i in range(1,N+1):
#     a, b = map(int, input().split())
#     print(f"Case #{i}: {a} + {b} =",a+b)

# #2438 별찍기 -1
# N = int(input())
# for i in range(1,N+1):
#     print("*"*i)
    
# #2439 별찍기 -2
# N = int(input())
# for i in range(1,N+1):
#     print(" "*(N-i) + "*"*i)


# #10871 x보다 작은 수
# N, X = map(int,input().split())
# A = list(map(int,input().split()))
# for i in range(N):
#     if A[i]<X:
#         print(A[i],end="")







# #while문
# #10952번 A+B -5
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)
    
# #10951번  A+B -4
# while True:
#     try:
#         a, b = map(int, input().split())
#         print (a+b)
#     except:
#         break

# #1110번 더하기 사이클
# n=int(input())
# num=n
# su=0
# while True:
#     a = num//10
#     b = num%10
#     c = (a+b) %10
#     num = b*10 + c 
#     su+=1
#     if n == num:
#         print(su)
#         break








# #1차원 배열

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



#함수

##15596번 정수 N개의 합

# def solve(a):
#     su = 0
#     for i in a:
#         su += i
#     return su

# #4673번 셀프넘버
# numbers = set(range(1,10000))
# remove_set = set()
# for i in numbers:
#     for j in str(i):
#         i += int(j)
#     remove_set.add(i)

# self_numbers = numbers - remove_set
# for i in (sorted(self_numbers)):
#     print(i)

# #1065번 한수
# n = int(input())
# result=[]
# for i in range(1,n+1):
#     li=[]
#     if i<100:
#         result.append(i)
#     else :
#         for j in str(i):
#             li.append(int(j))       
#         a = li[0]-li[1] 
#         b = li[1]-li[2]
#         if a == b :
#             result.append(i)
# print(len(result))



#문자열

# # #11654번 아스키 코드
# n = input()
# print(ord(n)) #chr아스키코드->문자열


# #11720번 숫자의 합
# a = int(input())
# n = input()
# re=0
# for i in n:
#     re += int(i)
# print(re)


# #10809번 알파벳 찾기
# n = input()
# alphabet = list(range(97,123)) #a(97)~z(122)
# for i in alphabet:
    # print(n.find(chr(i)))

# #2675번 문자열 반복
# n = int(input())
# for i in range(n):
#     a, b = input().split()
#     re=""
#     for i in b :
#         re += i*int(a)
#     print(re)

# #1157번 단어 공부
# n = input().upper()
# n2 = list(set(n))

# li=[]
# for i in n2:
#     cnt = n.count(i)
#     li.append(cnt)
# if li.count(max(li)) > 1:
#     print("?")
# else:
#     n_index = li.index(max(li))
#     print(n2[n_index])

# #1152번 단어의 개수
# #정답
# n=input().split()
# print(n)
# print(len(n))
# #오답
# n=input().split(" ")
# print(n)
# print(len(n))

# #2908번 상수
# a, b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])
# if a>b:
#     print(a)
# else :
#     print(b)

# #5622번 다이얼
# alphabet = ["ABC","DEF","GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
# a = input()
# sum=0
# for i in a:
#     for j in alphabet:
#         for k in j:
#             if(i==k):
#                 sum += alphabet.index(j)+3
# print(sum)

# #2741번 크로아티아 알파벳
# cro_alp = ["c=","c-","dz=","d-","lj","nj","s=","z="]
# alp=input()
# for i in cro_alp:
#     alp = alp.replace(i,'x')
# print(len(alp))

# #1316번 그룹 단어 체커
# n=int(input())
# group_word = 0
# for i in range(n):
#     false = 0
#     a = input()
#     for j in range(len(a)-1):
#         if a[j] != a[j+1]:
#             new_a = a[j+1:]
#             if new_a.count(a[j]) > 0:
#                false = 1
#     if false == 0:
#         group_word += 1
# print(group_word)

# #1712번 손익분기점
# a,b,c = map(int,input().split())
# if b >= c:
#     print(-1)
# else:
#     print((a//(c-b))+1)
# #a+b*n = c * n
# #n(c-b)=a
# #n=a//(c-b)

# #2292번 벌집
# n=int(input())
# su=1 #벌집의 개수
# increase=1 #반복 횟수
# while n > su:
#     su += 6 * increase
#     increase += 1
# print(increase)

# #1193번 분수찾기 
# num=int(input())
# line=1
# max_num=1
# while num>max_num:
#     line+=1
#     max_num+=line
# gap=max_num-num
# if line%2==0:
#     top=line-gap
#     low=gap+1
# else :
#     top=gap+1
#     low=line-gap
# print(f'{top}/{low}')


# #2869번 달팽이는 올라가고 싶다
# import math
# A, B, V = map(int,input().split())
# day=math.ceil((V-A)/(A-B))+1
# print(day)

# #10250번  ACM호텔
# a=int(input())
# for i in range(a):
#     H, W, N = map(int,input().split())
#     floor = (N % H)
#     room = (N // H) + 1
#     if N % H == 0:
#         floor = H
#         room = N // H
#     print(f'{floor*100+room}')


# #2775번 부녀회장이 될테야
# n = int(input())
# for i in range(n):
#     floor = int(input())
#     room = int(input())
#     f0 = [x for x in range(1,room+1)] #comprehension
#     for j in range(floor):
#         for k in range(1,room):
#             f0[k] += f0[k-1]
#     print(f0[-1])

# #2839번 설탕 배달
# N = int(input())
# bag = 0
# while N >= 0:
#     if N % 5 == 0:
#         bag += N//5
#         print(bag)
#         break
#     N -= 3
#     bag += 1
# else :
#     print(-1)


#10757번 큰 수 A+B
# a, b = map(int,input().split())
# print(a+b)


#1978번 소수 찾기
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






# print("20220302")

