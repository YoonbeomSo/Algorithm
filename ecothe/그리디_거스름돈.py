#거스름돈
n=int(input())
count=0

# 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500,100,50,10]

for coin in coin_types:
    count += n // coin
    n %= coin
print(count)

#시간 복잡도: O(K) / 화폐의 종류 : K
# 화폐의 단위가 배수관계이기 때문에 성립 