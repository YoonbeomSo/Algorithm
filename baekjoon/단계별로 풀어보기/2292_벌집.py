n=int(input())
su=1 #벌집의 개수
increase=1 #반복 횟수
while n > su:
    su += 6 * increase
    increase += 1
print(increase)