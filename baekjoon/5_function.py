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