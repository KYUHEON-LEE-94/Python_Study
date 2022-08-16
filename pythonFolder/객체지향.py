
class Rectangle(object):

    def __init__(self, b, v):
        self.b = b
        self.v = v

    def area(self):
        return self.b * self.v

# test = Rectangle(10,20);
# print(test.area());

#캐릭터 만들어보기

class Character(object):

    def __init__(self) -> None:
        self.life = 1000;

    def attacked(self):
        self.life -= 10
        print("공격받음! 생명력 = ", self.life)

a = Character();
b = Character();
print(a.life);
print(a.attacked());

#https://datascienceschool.net/01%20python/02.12%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D.html