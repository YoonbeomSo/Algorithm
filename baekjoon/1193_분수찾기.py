num=int(input())
line=1
max_num=1
while num>max_num:
    line+=1
    max_num+=line
gap=max_num-num
if line%2==0:
    top=line-gap
    low=gap+1
else :
    top=gap+1
    low=line-gap
print(f'{top}/{low}')