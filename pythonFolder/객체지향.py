
class Rectangle(object):

    def __init__(self, b, v):
        self.b = b
        self.v = v

    def area(self):
        return self.b * self.v

# test = Rectangle(10,20);
# print(test.area());

#생성자
class classname(object):
    def __init__(self,v1,v2) -> None:
        self.v1 = v1;
        self.v2 = v2;

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

# https://datascienceschool.net/01%20python/02.12%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D.html

#클래스 상속(class inheritance)

class Worrior(Character):

    def __init__(self):
        super(Worrior, self).__init__()
        self.strength = 15;
        self.intelligence = 5;

class Citizen(Character):
    
    def __init__(self):
        super(Citizen, self).__init__()
        self.strength = 5;
        self.intelligence = 5;

worrior1 = Worrior();
citizen2 = Citizen();

print(worrior1.life, citizen2.life);

#메서드 오버라이딩

class Worrior(Character):

    def __init__(self):
        super(Worrior, self).__init__()
        self.strength = 15;
        self.intelligence = 5;

    def attacked(self):
        print("검 공격!")
    

class Citizen(Character):
    
    def __init__(self):
        super(Citizen, self).__init__()
        self.strength = 5;
        self.intelligence = 5;

    def attacked(self):
        print("마법 공격!")


