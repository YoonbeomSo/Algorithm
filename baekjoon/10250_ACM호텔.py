a=int(input())
for i in range(a):
    H, W, N = map(int,input().split())
    floor = (N % H)
    room = (N // H) + 1
    if N % H == 0:
        floor = H
        room = N // H
    print(f'{floor*100+room}')