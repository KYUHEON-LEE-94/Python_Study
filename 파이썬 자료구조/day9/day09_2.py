# 원형 연결리스트
# 1) 노드 생성 및 노드 연결
class Node():
    def __init__(self):
        self.data = None
        self.link = None


# 객체화(짱구 -> 철수 -> 훈이 -> 맹구)
node1 = Node()
node1.data = "짱구"
node1.link = node1

node2 = Node()
node2.data = "철수"
node1.link = node2
node2.link = node1

node3 = Node()
node3.data = "훈이"
node2.link = node3
node3.link = node1

node4 = Node()
node4.data = "맹구"
node3.link = node4
node4.link = node1

current = node1
print(current.data, end='->')
print(current.link.data, end='->')
print(current.link.link.data, end='->')
print(current.link.link.link.data, end='->')
print(current.link.link.link.link.data, end='->')

while current.link != node1:  # 한바퀴를 모두 도는 동안 반복하겠습니다.
    current = current.link  # 다음노드를 현재노드로 지정
    print(current.data, end='->')

# 2) 노드 삭제
# 1 단순 연결리스트와 동일, 마지막 노드가 처음 노드를 가리키는 것만 주의!!
# 훈이만 삭제

node2.link = node3.link
del (node3)
current = node1
print(current.data, end='->')
while current.link != node1:
    current = current.link
    print(current.data, end='->')


# 유리를 철수와 맹구 노드 사이에 삽입
newNode = Node()
newNode.data = '유리'
newNode.link = node2.link
node2.link = newNode

current = node1
print(current.data, end='->')
while current.link != node1:
    current = current.link
    print(current.data, end='->')
