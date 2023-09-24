while True:
    triangle_list=list(map(int,input().split()))
    if sum(triangle_list) == 0:
        break
    maxsu=max(triangle_list)
    triangle_list.remove(maxsu)
    if triangle_list[0]**2+triangle_list[1]**2 == maxsu**2:
        print("right")
    else:
        print("wrong")