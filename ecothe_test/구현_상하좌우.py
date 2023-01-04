n = int(input())
x, y = 1, 1
plans = input().split() #공백을 입력 받기 때문 

list_vactor =['U','D','L','R']
fx = [-1, 1, 0, 0]#행
fy = [0, 0, -1, 1]#열


for plan in plans:
    for i in range(len(list_vactor)):
        if plan == list_vactor[i]:
            target_x = x + fx[i]
            target_y = y + fy[i]
    if target_x >= 1 and target_x <= n and target_y >=1 and target_y <= n:
        x = target_x
        y = target_y
    
print(x, y)