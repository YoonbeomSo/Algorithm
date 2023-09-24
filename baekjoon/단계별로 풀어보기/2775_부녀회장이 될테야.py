n = int(input())
for i in range(n):
    floor = int(input())
    room = int(input())
    f0 = [x for x in range(1,room+1)] #comprehension
    for j in range(floor):
        for k in range(1,room):
            f0[k] += f0[k-1]
    print(f0[-1])