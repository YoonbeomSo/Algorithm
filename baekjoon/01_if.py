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