# 현재 나이트의 위치 입력받기
n = input()
row = int(n[1])
colum = int(ord(n[0]))-int(ord('a')) + 1 

# 나이트가 이동할 수 있는 8가지 경우의 수 정의
move_type=[(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)]

# 8가지 경우의 수에 대하여 각위치로 이동이 가능한지 확인
count=0
for move in move_type:
    # 이동하고자 하는 위치 확인
    nextrow = row+move[1]
    nextcolum = colum+move[0]

    # 해당 위치로 이동이 가능하지 않다면 해당 반복 종료
    if nextrow<1 or nextcolum<1 or nextrow>8 or nextcolum>8:
        continue
    # 해당 반복이 종료 되지 않았다면 카운트 증가
    count+=1
    
print(count)