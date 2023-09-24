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