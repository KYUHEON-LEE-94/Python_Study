# 스택
# 리스트로 구현
stack1 = []
stack1.append(1)
stack1.append(2)
stack1.append(3)
stack1.append(4)
stack1.append(5)
print(stack1)

stack1.pop()  # 맨 마지막에 있는 요소가 삭제됨
print(stack1)

# 함수명 Stack
# 빈리스트 1개 생성: stack
# 리스트에 1부터 3까지 추가후
# (반복문 사용) 반복문 내에서 pop values is 출력 stack에 있는 값들을 하나씩 pop
# 함수 호출로 출력 결과를 확인


def Stack1():
    stack2 = []

    stack2.append(1)
    stack2.append(2)
    stack2.append(3)

    print(stack2)

    while stack2:
        print(" pop values is", stack2.pop())


Stack1()

# 클래스로 구현


class Stack:
    def __init__(self, max=10):  # 초기화 메서드(스택 생성 준비작업)
        self.stk = []  # 실질적으로 데이터가 저장될 공간
        self.max = max  # 스택의 크기를 저장하는 공간

    # show 메서드: 확인용
    def show(self):
        print("----------------------------")
        for element in self.stk:
            print('|', element, end=' ')
        print("\n--------------------------")

    # push(): 데이터 삽입
    def push(self, element):
        if self.max > len(self.stk):
            self.stk.append(element)

    # pop(): 데이터 삭제
    # 스택이 비어있는데 삭제하려고 하는 경우에 오류
    # 스택이 비어있지 않을때만 삭제하기
    # 삭제 + 삭제된 값을 return
    def pop(self):
        if len(self.stk) != 0:
            return self.stk.pop()

    # peek(): top에 있는 값을 엿보기
    # 스택이 비어있지 않을 때만 실행
    def peek(self):
        if len(self.stk) != 0:
            return self.stk[-1]

    # clear(): 스택을 비우기
    def clear(self):
        for i in range(len(self.stk)):
            self.pop()


# stack에 10부터 60까지 넣어서 show로 확인
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.push(60)
s1.show()
print("삭제된 요소: ", s1.pop())
s1.show()
print("삭제된 요소: ", s1.pop())
s1.show()
print(s1.peek())
