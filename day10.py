# 클래스
class Test:

    def hello(self):
        print("Hello")


# new를 안쓰고 객체 생성을 하네..
t = Test()
t.hello()


#


class Hello:
    def print_hello(self):
        print("안녕하세요")


# self매개변수가 없는 경우 출력됨
# Hello.print_hello()

# Class명 Person, 메소드2개 생성

# class Person:
#     def getName(self):
#         return self.name

#     def getAge(self):
#         return self.age


# pr = Person()
# pr.name = "강아지"
# pr.age = 12
# print(pr.getName())
# print(pr.getAge())

class Person:
    eye = 2
    nose = 1
    mouse = 1
    name = ''
    age = 0

    def __init__(self, name, age=12):  # self는 this
        self.name = name
        self.age = age

    def getName(self):
        print(f'나는 {self.name}입니다.')

    def getAge(self):
        print(f"내 나이는 {self.age}입니다.")


pr1 = Person("이규헌", 23)
pr1.getAge()
pr1.getName()

pr2 = Person("강아지")
pr2.getAge()

# 파이썬은 굳이 변수를 선언해줄 필요가 없음. 객체생성시 넣은 변수이름대로 알아서 생성됨


class Person3:
    def __init__(self, name):
        self.name = name

    def who_am_i(self,  age, address, phone):
        self.age = age
        self.address = address
        self.phone = phone
        print(f'나이{self.age}, 주소: {self.address}, 폰: {self.phone }')


p3 = Person3("뭐냐")
p3.who_am_i(12, "123", "3123")
print(p3.name)


class Test1:
    def __init__(self):
        print("생성자 호출")


test = Test1()
test1 = Test1()


class Candy:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color


satang = Candy("circle", "브라운")
print(satang.color, satang.shape)


# 소멸자


class Sample:
    def __del__(self):
        print("인스턴스가 소멸합니다.")


sample = Sample()
del sample


# 클래스 변수와 인스턴스 변수
print("---------Animal-------------")


class Animal:
    # 클래스 변수
    leg = 4
    eyes = 2
    neck = 1
    head = 1

    def test(self, head):
        self.head = head


ani = Animal()
print(Animal.leg)
print(Animal.eyes)
print(Animal.neck)
print(Animal.head)
print(ani.test(2))
print(ani.head)
print(Animal.head)

# 클래스 메서드와 정적메서드


class Korean:
    country = '한국'

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


man1 = Korean("박지성", 36, "제주도")
print(man1.country)
print(man1.name)
man2 = Korean("손흥민", 30, "런던")
print(man2.country)
print(man2.name)

# 클래스 메서드


class Sample2:
    count = 0

    def __init__(self):
        Sample2.count += 1

    @classmethod
    def counting(cls):
        print(f"{cls.count}개의 객체 생성")


s1 = Sample2()
print(s1.count, Sample2.count)
Sample2.counting()
s1.counting()

s2 = Sample2()
print(s2.count, Sample2.count)
Sample2.counting()
s2.counting()

s3 = Sample2()
print(s3.count, Sample2.count)
Sample2.counting()
s3.counting()
print("최종", s1.count, s2.count, s3.count)

# 정적 메서드
# 1. 인스턴스 똔느 클래스로 호출
# 생성된 인스턴스가 없어도 호출할 수 있따
# @staticmethod 데코레이털르 표시하고 작성한다.
# 반드시 작성해야할 매개변수가 없다.
# 클래스에 소속되어 있지만 인스턴스에는 영향을 주지 않고 인스턴스로부터 영향을 받지 않는다.


class Korean2:
    @staticmethod
    def slogan():
        print("your Korean")


Korean2.slogan()


class Student2:
    def __init__(self, ssn, name, number):
        self.ssn = ssn
        self. name = name
        self.number = number


stu1 = Student2(1, "짱구", 51)
stu2 = Student2(2, "철수", 100)
stu3 = Student2(3, "훈", 58)
stu4 = Student2(4, "맹구", 82)

list = []


class AVGmake:

    @staticmethod
    def calcul(*number):
        sum = 0
        for i in number:
            sum += i.number
        print(f'전체평균: {sum/ len(number)}')


AVGmake.calcul(stu1, stu2, stu3, stu4)
