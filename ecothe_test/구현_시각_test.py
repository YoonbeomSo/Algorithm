h = int(input())

count = 0 

for HH in range(h+1):
    for mm in range(60):
        for ss in range(60):
            if '3' in str(HH)+str(mm)+str(ss):
                count += 1

print(count)