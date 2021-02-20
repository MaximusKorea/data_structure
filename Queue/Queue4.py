import queue
test_queue = queue.PriorityQueue()

test_queue.put((1,"Republic of KOREA"))
test_queue.put((2,"United States"))
test_queue.put((3,"japan"))
test_queue.put((4,"china"))

for i in range(test_queue.qsize()):
    print(test_queue.get(),end=" ")