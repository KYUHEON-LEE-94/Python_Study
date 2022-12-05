# 노드 생성
class Node:
    def __init__(self):
        self.data = None
        self.link = None


node1 = Node()
node1.data = "짱구"
print(node1.data)

# 노드 연결(철수 -> 훈이 -> 맹구)
node2 = Node()
node2.data = "철수"
node1.link = node2

node3 = Node()
node3.data = "훈이"
node2.link = node3

node4 = Node()
node4.data = "맹구"
node3.link = node4

current = node1
while current.link != None:
    current = current.link

# 노드 삽입
newnode = Node()
newnode.data = "유리"
newnode.link = node2.link
# node2철수 node2.link는 node3(훈이)를 가르킴
node2.link = newnode
# 새로운 노드가 들어왔으니 node2.link를 새로운 노드쪽으로 연결

current = node1
while current.link != None:
    current = current.link
    print(current.data, end='->')
print()
# 노드 삭제
print("----노드 삭제----")
print(id(node3.link))
node2.link = node3.link
print(id(node2.link))
# 메모리에서 아예 삭제
del (node3)

current = node1
print(current.data, end='->')
while current.link != None:
    current = current.link
    print(current.data, end='->')

# 연결리스트 ADT


class Linkedlist:
    # date와 pointer를 기억하기 위한 내부 class
    class Node:
        def __init__(self, element=None, node=None):
            self.element = element
            self.next = node

    def __init__(self):
        self.head = None  # Linkedlist의 시작 노드를 알고있는 변수
        self.length = 0  # Linkedlist의 길이 (요소 개수)

    # 확인용 출력메소드

    def show(self):
        curr = self.head
        while curr != None:
            print(curr.element, end='->')
            curr = curr.next
        print()

    # 데이터 삽입
    # 맨앞에 삽입
    def insertfirst(self, element):
        newNode = self.Node(element, self.head)
        self.head = newNode
        self.length += 1

    # 맨뒤에 삽입
    def insertlast(self, element):
        # 리스트에 요소가 하나도 없다면 맨 앞에 삽입이 되도록 설정
        if self.head == None:
            self.insertfirst(element)
            return

        # 그게 아니라면 원래 마지막에 있는 노드를 찾아야함
        curr = self.head  # 첫번째 노드르 curr에 담아줌
        while curr.next != None:
            curr = curr.next

        # 반복문을 다 돌고나며 curr에는 마지막 노드가 담기게 됨
        newNode = self.Node(element)
        curr.next = newNode
        self.length += 1

    # 중간에 삽입
    def insert(self, idx, element):
        # idx 유효성 검사
        if idx < 0 or idx > self.length:
            print("인덱스 범위 벗어남")

        # idx가 0이라면 맨앞에 삽입해줌
        if idx == 0:
            self.insertfirst(element)

        # 위의 상황에 아니라면 삽입할 위치의 이전 노드를 찾기
        curr = self.head
        for i in range(idx-1):
            curr = curr.next
        newNode = self.Node(element, curr.next)
        curr.next = newNode
        self.length += 1

    # 데이터 삭제
    def removefirst(self):
        if self.head == None:
            return
        self.head = self.head.next
        self.length -= 1

    def remove(self, idx):
        # idx 유효성 검사
        if idx < 0 or idx >= self.length:
            raise IndexError("인덱스 벗어남")

        if idx == 0:
            self.removefirst()
            return

        curr = self.head
        for i in range(idx):
            prev = curr  # prev : 삭제할 노드의 이전노드
            curr = curr.next  # curr : 삭제할 노드
        prev.next = curr.next

        for i in range(idx-1):
            curr = curr.next

        curr.next = curr.next.next
        self.length -= 1

    # 조회

    def select(self, idx):
        if idx < 0 or idx >= self.length:
            print('인덱스 오류')
            return

        curr = self.head
        for i in range(idx):
            curr = curr.next

        return curr.element

    # 수정
    def update(self, idx, element):
        if idx < 0 or idx >= self.length:
            return

        curr = self.head
        for i in range(idx):
            curr = curr.next

        curr.element = element


li = Linkedlist()
li.insertfirst(10)
li.show()
li.insertfirst(20)
li.show()
li.insertlast(30)
li.show()
li.insert(2, 50)
li.show()
li.insert(2, 70)
li.show()

li.removefirst()
li.show()
li.remove(1)
li.show()
