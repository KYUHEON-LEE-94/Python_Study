# 1
import random as r
countTest = 6
list1 = set()
for i in range(0, countTest):
    randomNum = r.randint(1, 45)
    list1.add(randomNum)
    if len(list1) != 6:
        countTest += 1

print(list(list1))
lsit2 = sorted(list1)
print(lsit2)
lsit2.sort(reverse=True)
print(lsit2)

# 2


class Student:
    def __init__(self, name, id, score=0):
        self.id = id
        self.name = name
        self.score = score

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setScore(self, score):
        self.score = score
        return self.score

    def getScore(self):
        return self.score


class CalcScore:
    sum = 0

    def __init__(self):
        self.student = []

    def setStudent(self, student):
        self.student.append(student)

    def getAvg(self):
        sum = 0
        for i in self.student:
            sum += i.getScore()
        return sum/len(self.student)


s1 = Student('영희', 1, 30)
s2 = Student('철수', 2, 40)
s3 = Student('수지', 3, 50)
s4 = Student('맹구', 4, 60)
calcScore = CalcScore()
calcScore.setStudent(s1)
calcScore.setStudent(s2)
calcScore.setStudent(s3)
calcScore.setStudent(s4)

print(f'{len(calcScore.student)}명 학생의 평균은 {calcScore.getAvg()}')

# 3


class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    @classmethod
    def getCount(self):
        return self.count


p1 = Person('김영선', 20)
p2 = Person('kys', 40)


class Custmoer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def setAddress(self, address):
        self.address = address

    def setPhone(self, phone):
        self.phone = phone


p3 = Custmoer("짱구", 5)
p3.setAddress("서울")
p3.setPhone('010-1234-5678')
print(f'{p3.name}은 {p3.age}입니다.')
print(f'사는 지역은{p3.address}이고 전화번호는{p3.phone}입니다.')
print(f'{p1.name}은 {p1.age}입니다.')
print(f'{p2.name}은 {p2.age}입니다.')
print(f'총인원은 {Person.getCount()}')
