# 1. 단순하게 푸는 답안 예시
# n, m, k = map(int, input().split())
# data = list(map(int,input().split()))
# data.sort(reverse=True)
# first = data[0]
# second = data[1]

# result=0
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
# print(result)

#2. Solution
n, m, k = map(int, input().split())
data = list(map(int,input().split()))
data.sort(reverse=True)
first = data[0]
second = data[1]

#가장 큰 수가 더해지는 횟수 계산
count = int(m/k+1)*k
count += m % (k+1)

result=0
result += count * first
result +=(m-count) * second

print(result)

