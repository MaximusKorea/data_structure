# 더블 링크드 리스트 : 기종 링크드 리스트는 처음(head)부터 시작해서 한쪽으로만 데이터 검색이 가능한 반면
#                     더블 링크드 리스트는 반대방향으로도 데이터 검색이 가능하다.

class MakeNode:
    def __init__(self,data,prev=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next

class Node:
    def __init__(self,data):
        self.head = MakeNode(data)
        self.tail = self.head
    
    def append(self,data):
        if self.head == None:
            self.head = MakeNode(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new_data = MakeNode(data)
            node.next = new_data
            new_data.prev = node
            self.tail = new_data

    def show(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

DoubleLinkedList = Node(0)
for data in range(1,10):
    DoubleLinkedList.append(data)
DoubleLinkedList.show()
            
