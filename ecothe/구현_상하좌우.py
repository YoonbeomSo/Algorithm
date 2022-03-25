n=int(input())
x, y = 1, 1
plans = input().split()

#상하좌우 에 따른 이동 
x_move = [0,0,1,-1]
y_move = [-1,1,0,0]
plans_type=['U','D','L','R']

# 이동 명령을 하나씩 확인
for plan in range(plans):
    # 이동 후 좌표 구하기
    for i in range(len(plans)):
        if plan==plans_type[i]:
            nx = x + x_move[i]
            ny = y - y_move[i]
        #공간을 벗어나는 경우 무시
        if nx<1 or ny<1 or nx>n or ny>y:
            continue
    x, y = nx, ny
print(x,y)