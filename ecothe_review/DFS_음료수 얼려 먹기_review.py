n,m=map(int,input().split())
graph=[]

# 2차원 리스트의 맵 정보 입력받기
for _ in range(n):
    graph.append(list(map(int,input())))


def dfs(x, y) :

    if x<0 or y < 0 or x>=n or y >=m:
        return false
    
    if graph[x][y] ==  0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return true
    else return false
        

# DFS로 측정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
result = 0
for i in range(n):
    for j in range(m):
        if def dfs(0,0) == True:
            result += 1
        

print(result)
