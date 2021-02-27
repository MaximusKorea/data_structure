# LinkedList의 삭제원리
# 1. 삭제 대상이 되는 값이 head(맨처음 node)의 값인경우
#    -> 해당 노드의 포인터값(다음 노드의 주소)을 변수 head에 저장해준다.
# 2. 삭제 대상이 가운데에 있는 경우
#       .... A - B - C .......
#    -> A의 pointer에 C의 주소값을 저장하고 B를 삭제해준다.
# 3. 삭제 대상이 마지막에 있는 경우
#       ..........B - C
#    -> B의 pointer에 none을 저장하고 C를 삭제한다.

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

    def show(self):
        node = self.head
        while node:
            print(node.data)
            node = node.pointer

    def delete(self,data):
        if self.head == '':
            print("노드가 존재하지 않습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.pointer
            del temp
        
        else:
            node = self.head
            while node.pointer:
                if node.pointer.data == data:
                    temp = node.pointer
                    node.pointer = node.pointer.pointer
                    del temp
                    return
                else:
                    node = node.pointer

    def search_node(self,data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.pointer


LinkedList1 = NodeManage(0)
for new_data in range(1,10):
    LinkedList1.add(new_data)
LinkedList1.show()

LinkedList1.delete(3)
print("------------------------------")
LinkedList1.show()
LinkedList1.delete(9)
print("------------------------------")
LinkedList1.show()