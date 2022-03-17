a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = []
for i in range(0,2):
    d.append(a[i])
    if a[i]==b[i]:
        d[i]=c[i]
    elif a[i]==c[i]:
        d[i]=b[i]
print(d[0],d[1])