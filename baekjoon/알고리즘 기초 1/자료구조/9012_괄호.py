N = int(input())
for _ in range(N):
    stack = []
    x_list = input()
    for x in x_list:
        if x == '(':    #여는 괄호는 stack에 쌓는다.
            stack.append(x)
        elif x == ')':
            if stack:       
                stack.pop()
            else:
                print("NO") #stack이 비어있다면 여는 괄호가 없는 상태에서 닫는 괄호가 있는 것이기 때문에 "NO" 이다
                break
    else : #for else 문 for문에서 break 기록이 없다면 else 실행.
        if not stack:
            print("YES")
        else :
            print("NO")
    
