#자바와 다르게 인스턴스 변수를 따로 선언할 필요가없다.
from unittest import result

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result;
    def mul(self):
        result = self.first * self.second
        return result    
    def div(self):
        result = self.first / self.second
        return result    
a = FourCal(1,2);
print(a.first)
print(a.add())

#클래스의 상속

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

#클래스의 상속은 기능 확장을 위해 보통 사용한다.
c = MoreFourCal(1,2);
print(c.add());
print(c.pow());

#오버라이딩
class saeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second


#클래스 변수

class Family:
    lastName = '김'

kim =Family();
kim2 = Family();
print(kim.lastName)
print(kim2.lastName)

Family.lastName = '박';
print(kim.lastName)
print(kim2.lastName)
#Family 클래스에 직접 접근해서 변수를 변경하면 모든 객체에 공유되어버린다.

kim.lastName = '최';
print(kim.lastName)
print(kim2.lastName)

