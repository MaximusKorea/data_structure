# Stack은 나중에 들어간 것이 먼저 나온다. 
# push : 데이터 스택에 쌓임, pop : 데이터 스택에서 꺼냄
# 스택은 최대로 쌓을 수 있는 공간을 정해두어야 하기 때문에 공간의 낭비가 발생할 수 있다.

# list로 stack 구현해보기(원래 list에는 append와 pop 메서드가 있어 그것을 통해서 stack을 구현할 수 있다.)

test_stack = list()

def push(num):
    test_stack.append(num)

def pop():
    num = test_stack[-1]
    del test_stack[-1]
    return num
for i in range(5):
    push(i)

for i in range(len(test_stack)):
    print(test_stack.pop(),end=" ")