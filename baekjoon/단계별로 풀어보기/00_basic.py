# print("HelloWorld")
#
# print("강한친구 대한육군\n강한친구 대한육군")
#
# print("\\    /\\\n )  ( \')\n(  /  )\n \\(__)|")
#
# print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")
#
# A, B = map(int, input().split())
# print(A+B)
#
# A, B = map(int,input().split())
# print(A-B)
#
# A, B = map(int,input().split())
# print(A*B)
#
# A, B = map(float,input().split())
# print(A/B)
#
# A,B = map(int,input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)
#
# A, B, C = map(int,input().split())
# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))%C)
#
# A=int(input())
# B=int(input())
#
# print(A*(B%10))
# print(A*(B//10%10))
# print(A*(B//100))
# print(A*B)

##18108번
# print(int(input()) - (2541-1998))

##3003번
# a,b,c,d,e,f = map(int, input().split())
# print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)

##25083
# print("         ,r'\"7\nr`-_   ,'  ,/\n \\. \". L_r'\n   `~\\/\n      |\n      |")


#리스트 컴프리핸션 -> 2차원 리스트 초기화시 반드시 리스트 컴프리헨션 사용
array = [i for i in range(20) if i % 2 == 1]
print(array)


# N X M 크기의 2차원 리스트 초기화
print("옳은 방법")
n=3
m=4
array = [[0] * m for _ in range(n)]
print(array)
array[0][1] = 5
print(array)
# N X M 크기의 2차원 리스트 초기화 잘못된 방법
print("잘못된 방법")
array = [[0] * m] * n
print(array)
array[0][1] = 5
print(array)