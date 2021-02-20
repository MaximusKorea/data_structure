import queue
#LifoQueue()의 경우에는 Lifo(last input first out)으로 일반적인 queue와는 반대이다.
test_queue = queue.LifoQueue()

test_queue.put("elephant")
test_queue.put("special")
test_queue.put("good")

for i in range(test_queue.qsize()):
    print(test_queue.get(),end=" ")