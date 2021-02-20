# 파이썬의 라이브러리를 사용가능
import queue

test_queue = queue.Queue()
test_queue.put("apple")
test_queue.put(1)
test_queue.put("computer")
test_queue.put("science")

for i in range(test_queue.qsize()):
    print(test_queue.get(),end=" ")