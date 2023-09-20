N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

count = 0
coins.sort(reverse=True)
for c in coins:
    count += K // c
    K %= c
    if K == 0:
        break

print(count)