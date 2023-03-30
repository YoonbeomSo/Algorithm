n,m = map(int, input().split())

#방문 체크를 위한 2차원 map
d = [[]* m for _ in range(n)]

#초기 위치 및 방향
x, y , direction = map(int, input().split())

d[x][y] = 1

#게임필드 생성
array =[]
for _ in range(n):
    array.append(list(map(int, input().split)))

#북0 동1 남2 서3
dx = [-1, 0, 1, 0]#행
dy = [0, 1, 0, -1]#열

#왼쪽회전
def left_turn():
    global direction
    direction -= 1
    if (direction < 0 ) :
        direction = 3

count = 0
check = 0
while True:
    left_turn()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[dx][dy] : 
        d[nx][ny] = 1
        x = nx 
        y = ny
        count += 1
        check = 0 
        continue
    else : 
        check += 1 

    if(check == 4):
        check = 0
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
           x = nx
           y = ny 
        else:
            break

#정답 출력
print(count)
