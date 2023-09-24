N = int(input())

stack=[]
for i in range(N):
    message = input().split()
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