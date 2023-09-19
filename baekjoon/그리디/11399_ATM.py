N = int(input())
members = list(map(int, input().split()))

answer = 0
members.sort()

for i in range(1, N+1):
    answer += sum(members[0:i])
    
print(answer)
