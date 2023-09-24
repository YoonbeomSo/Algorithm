N = int(input())

for _ in range(N):
    target = list(input().split())
    result = ''
    for tg in target:    
        result += ''.join(reversed(tg)) + ' '
    print(result)