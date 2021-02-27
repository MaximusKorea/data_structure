# LinkedList : 연결리스트라고도 한다.
# 배열과 링크드 리스트의 차이점
# 배열 : 데이터가 들어갈 배열의 크기를 미리 정해두어야 한다.

# 링크드 리스트 : 필요할 때마다 데이터를 추가할 수 있다.
# 링크드 리스트는 노드(Node)라는 기본단위로 이루어져 있다.

# 노드 : 데이터저장공간 + 다음 노드의 데이터 저장공간(pointer)
# 링크드 리스트의 기본단위 = 노드 = data + pointer

class MakeNode:
    def __init__(self,data,pointer=None):
        self.data = data
        self.pointer = pointer
def add(new_data): #새로운 값을 추가함
    node = head 
    while node.pointer: #해당 node의 pointer에 값이 존재하면 그 다음 node의 주소를 해당 node로 가져온다 
        node = node.pointer # 즉 다음 노드로 계속해서 넘어가게 된다.
    node.pointer = MakeNode(new_data) # 마지막 노드로 왔을 때는 해당 노드의 pointer값(다음 노드의 주소값)이 존재하지 않기 때문에 while문이 끝이난다.
    #이 때 마지막 노드의 pointer 값에 새로운 선언된 노드의 주소값을 넣어준다.
node1 = MakeNode(1)
head = node1
for new_data in range(2,10):
    add(new_data)

node = head
while node.pointer:
    print(node.data)
    node = node.pointer
print(node.data)