n=int(input())
group_word = 0
for i in range(n):
    false = 0
    a = input()
    for j in range(len(a)-1):
        if a[j] != a[j+1]:
            new_a = a[j+1:]
            if new_a.count(a[j]) > 0:
               false = 1
    if false == 0:
        group_word += 1