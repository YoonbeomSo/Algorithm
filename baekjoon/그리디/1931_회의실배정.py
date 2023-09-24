#회의 수
N = int(input())

#회의 시간
time=[]
for _ in range(N):
    start, end = map(int,input().split())
    time.append([start, end])


#시작시간 오름차순 정렬, #시작시간이 같다면 끝시작 오름차순 정렬
time.sort(key=lambda a: a[0])
time.sort(key=lambda a: a[1])

#회의가 끝나는 시간
last = 0
#회의 수
count = 0

#가장 많은 회의를 하기 위해서는 시작시간이 가장 빠른 시간부터 끝시작이 가장 늦은시간으로 순서대로 확인해야한다.
for i, j in time:
    if i >= last:
        count += 1
        last = j
    

print(count)