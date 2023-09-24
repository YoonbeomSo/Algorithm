import sys
N = int(sys.stdin.readline())


stack=[]
for i in range(N):
    message = sys.stdin.readline().split()
    #push X
    if message[0] == 'push':
        stack.append(message[1])
    #pop
    elif message[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else :
            print(stack.pop())
    #size
    elif message[0] == 'size':
        print(len(stack))
    #empty
    elif message[0] == 'empty':
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    #top
    elif message[0] == 'top':
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])


#input() 함수를 사용할 경우, 시간초과 에러가 뜨므로 시간단축을 위해 sys.stdin.readline()을 사용한다.
#입출력 속도 비교 : sys.stdin.readline > raw_input() > input()