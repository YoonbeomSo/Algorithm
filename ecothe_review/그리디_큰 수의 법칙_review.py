# n, m ,k = map(int, input().split())
# data = list(map(int,input().split()))

# data.sort(reverse = True)

# first = data[0]
# second = data[1]
# result = 0

# while True:
#     for _ in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

# print(result)    


#2차 솔루션

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수
# k + 1 : 수열의 길이
# m / (k + 1) : 수열이 반복되는 횟수(완벽히 나누어 떨어지는 경우)
# int(m / (k + 1)) : 수열이 반복되는 횟수(완벽히 나누어 떨어지지 않는 경우 고려)
# int(m / (k + 1)) * k : 가장 큰 수가 반복되는 횟수
count = int(m / (k + 1)) * k
# m% (k + 1) : 수열의 횟수가 완벽히 나누어 떨어지지 않는 경우 가장 큰수가 곱해져야하는 나머지 횟수를 더해줘야한다.
count += m % (k + 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기

print(result)

