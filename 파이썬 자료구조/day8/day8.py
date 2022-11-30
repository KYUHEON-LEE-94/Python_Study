# 1. 자료구조
# 1-2) 추상 데이터 자료형
# 가방(Bag)의 추상 자료형 정의 및 구현
# data => 지갑, 핸드폰, 거울, 빗, 동전, 빗 등

# 클래스 정의
import time


class Bag:
    def __init__(self):
        self.mybag = []

    def contains(self, bag, e):
        return e in bag

    def insert(self, e):
        self.mybag.append(e)

    def remove(self, e):
        self.mybag.remove(e)

    def count(self, bag):
        return len(bag)


# 클래스 사용
b1 = Bag()
#핸드폰, 지갑,빗,손수건
b1.insert('핸드폰')
b1.insert('빗')
b1.insert('지갑')
b1.insert('손수건')
print(f"가방속의 물건:{b1.mybag}")
# 개수 확인
num = b1.count(b1.mybag)
print(f"가방속의 물건개수:{num}")
# 중복삽입 => 빗
b1.insert('빗')
print(f"빗이 2개일까?: {b1.mybag}")
print(f"가방속의 물건개수:{num}")  # 빗은 2개가 있지만, 개수는 4개로 확인된다.
# 가방속의 지갑이 있는지
print(f"지갑 잇나요?: {b1.contains(b1.mybag,'지갑')}")
# 핸드폰을 꺼내자
b1.remove('핸드폰')
print(f"핸드폰을 꺼내자: {b1.mybag}")

# 알고리즘 성능 분선
start = time.time()


class Bag1:
    def __init__(self):
        self.new_bag = []

    def append(self, e):
        self.new_bag.append(e)  # 리스트 new_bag의 맨 뒤에 항목 e를 추가


b2 = Bag1()
b2.append('축구공')
end = time.time()
print(f'실행시간 Bag1: {end - start}')

# 위는 Append 아래는 Insert 사용

start2 = time.time()


class Bag2:
    def __init__(self):
        self.new_bag = []

    def insert(self, e):
        self.new_bag.insert(0, e)  # 리스트 new_bag의 맨 뒤에 항목 e를 추가


b3 = Bag2()
b3.insert('축구공')
end2 = time.time()
print(f'실행시간 Bag2: {end2 - start2}')


# [시간 복잡도]
# O(1)

def hello_world():
    print("hello world")

# O(n)


def print_each(li):
    for i in li:
        print(i)

# O(n^2)


def print_each2(li):
    for i in li:
        for j in li:
            print(i, j)

# O(log n), O(nlog n): 정렬 알고리즘에서 많이 사용


# -----리스트-----
data = [(10, '짱구', '000-0000-0000'),
        (20, '철수', '111-1111-1111'),
        (30, '맹구', '333-3333-3333'),
        None, None]

print(data)
print(data[0])
print(data.pop(0))
print(data)  # 철수 튜플을 다시 앞으로 통째로 땡겨야 해서 메모리 소모가 됨

# ----연결 리스트 ------


class Node():
    def __init__(self):
        self.data = None
        self.link = None


node1 = Node()
node1.data = "짱구"
print(node1.data)

# 노드 연결
node2 = Node()
node2.data = '철수'
node1.link = node2
print(node1.data)
print(node1.link.data)

# 노드 연결
node3 = Node()
node3.data = '훈이'
node2.link = node3
print(node2.data)
print(node2.link.data)

# 노드 연결
node4 = Node()
node4.data = '맹구'
node3.link = node4
print(node3.data)
print(node3.link.data)

# 노드삭제 node3을 지울때
print(id(node3.link))
print(node2.link.data)
node2.link = node3.link  # node2.link = node3.link (훈이)를 가리키고 있기 때문에 맹구로 변경하면됨
print(node2.link.data)  # 훈이 -> 맹구가됨
print(id(node2.link))
print(node3)
del (node3)  # del을 사용하면 주소값을 삭제된것을 확인할 수 잇음
# print(node3)


# 1. 첫번째 노드를 현재노드로 지정하고, 현재 노드의 데이터 짱구를 출력함
# 2. 현재 노드의 링크가 비어있지 않다면 현재 노드를 현재 노드의 링크가 가리키는 노드로 변경한 후에 현재 노드의 데이터인 철수를 출력함
# 3. 현재 노드의 링크가 비어있으면 종료함

# 1. current 변수에 첫번재 노드를 대입
current = node1
print(current.data)  # 짱구

# 2.반복문(조건) -> while 링크가 비어있지 않다면
while current.link != None:
    current = current.link
    print(current.data, end="->")
