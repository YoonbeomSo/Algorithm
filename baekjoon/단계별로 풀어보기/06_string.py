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