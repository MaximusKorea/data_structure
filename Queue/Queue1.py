# Queue
# FIFO(First-in, First-out) 방식 , 먼저 들어간 것이 먼저 나온다. 

# 리스트를 이용하여 Queue의 기능 구현

queue1 = list()

def Enqueue(data):
    queue1.append(data)

def Dequeue():
    a = queue1[0]
    del queue1[0]
    return a

for num in range(0,10):
    Enqueue(num)

print(queue1)
print(Dequeue())
print(queue1)

