# 더블 링크드 리스트는 뒤(tail)에서부터 이동이 가능하다.

class MakeNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
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

    def head_search(self,data):
        if self.head == None:
            return False
        
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def tail_search(self,data):
        if self.head == None:
            return False
        
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def append_before(self,data,before_data):
        if self.head == None:
            self.head = MakeNode(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new_data = MakeNode(data)
            before_new_data = node.prev
            before_new_data.next = new_data
            new_data.prev = before_new_data
            new_data.next = node
            node.prev = new_data
            return True

DoubleLinkedList = Node(0)
for idx in range(1,10):
    DoubleLinkedList.append(idx)
#DoubleLinkedList.show()
#print(DoubleLinkedList.tail_search(3).data)
DoubleLinkedList.append_before(2.5,3)
DoubleLinkedList.show()
