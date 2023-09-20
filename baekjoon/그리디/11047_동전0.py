# 동전개수, 목표금액
N, K = map(int, input().split())

# 동전 종류 리스트
coins = []
for _ in range(N):
    coins.append(int(input()))

# 결과값
count = 0

#큰수 동전부터 비교
coins.sort(reverse=True)
for c in coins:
    #나누어진 횟수
    count += K // c
    #큰수로 나누고 남은 금액
    K %= c
    #동전을 모두 확인하기 전에 목표금액 달성
    if K == 0:
        break

#결과값 출력
print(count)