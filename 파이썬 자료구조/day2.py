# 1. 모듈
# 1) 표준 모듈
import matplotlib as plt
import time
import random as r
from random import randint, randrange
import random

print(random.randint(1, 10))  # 입력된 숫자사이에서 랜덤한 숫자 return

random.randrange(10)  # 0~입력값 사이의 랜덤 숫자 출력
print(random.randrange(2, 10, 3))  # randrange(a,b,c) a~b까지 c 스텝씩 뛰면서 랜덤 출력
# choice(시퀀스 자료형) * 순서가 있는 자료형(list,tuple, 문자열, range())
print(random.choice('안녕하세요'))

print(random.sample(['봄', '여름', '가을', '겨울'], 2))  # sampe(a,b) 몇개를 뽑을 건지?


# 모듈에서 특정함수만 import하기
print(randint(1, 6))
# print(choice('안녕')) 안됨


# 모듈에서 별칭부여
# import 모듈명 as 별칭
print(r.randint(1, 6))


# print('안녕하세요')
# time.sleep(5)
# print('반갑')


# 입력받은 값까지 더해서 전체합 구하기
# number = int(input("입력: "))


# def getSum(num):
#     return num*(num+1)/2


# print(getSum(number))

# 클래스


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Person2:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


b1 = Person("이규헌")
print(b1.getName())
b2 = Person("조규헌", 12)
print(b2.getAge())

# 필수적으로 받아야하는건 생성자로 받아주고, 그 이외의 것은 defalut 인수로 받던가 그냥 메서드로 따로 받아도 될듯?..
b3 = Person2("와우")
b3.age = 23
print(b3.getAge())


# 클래스 구현
class Cal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second


cal = Cal()
cal.setdata(10, 5)
print(cal.add())
print(cal.mul())

# 생성자


class SomeClass:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def introduece(self):
        print(self.name)
        print(self.age)
        print(self.job)


user1 = SomeClass("박지성", 23, "축구선수")
user2 = SomeClass("류현진", 35, "야구선수")

# 상속


class Person3:  # 부모클래스
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name}이 {food}를 먹는다.")

# 서브클래스


class Student(Person3):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def studty(self):
        print(f"{self.name}은 {self.school}에서 공부한다.")


stu1 = Student("이구헌", "좋은 학교")
stu1.eat("당근")
stu1.studty()

st2 = Person3("조구헌")
st2.eat("삥")

print(isinstance(stu1, Person3))
print(isinstance(st2, Student))
