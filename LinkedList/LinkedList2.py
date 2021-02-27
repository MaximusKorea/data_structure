# LinkedList 데이터 추가 원리
# 중간에 데이터를 삽입하려고 이전의 pointer에 새로운 노드의 주소값을 넣어주고
# 새로운 노드의 포인터에 다음 노드의 주소값을 넣어준다.

class Node:
    def __init__(self, data, pointer=None):
        self.data = data
        self.pointer = pointer

class NodeManage:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.pointer:
                node = node.pointer
            node.pointer = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.pointer

LinkedList1 = NodeManage(0)
LinkedList1.desc()
for new_data in range(1,10):
    LinkedList1.add(new_data)
LinkedList1.desc()