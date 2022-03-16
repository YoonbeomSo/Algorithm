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