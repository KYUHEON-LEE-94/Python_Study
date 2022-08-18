class word(object):
    def __init__(self, txt):
        self.txt =txt

word1 = word('orange');
word2 = word('apple');
print(word1);
print(word2);
#현재 참조하고 있는 객체의 레퍼런스를 출력한다.  

class wordClass(object):
    def __init__(self, txt):
        self.txt =txt
    def __repr__(self):
        return str(self.txt)

word3 = wordClass('orange');
word4 = wordClass('apple');
print(word3);
print(word4);
#Java기준으로보면 상위 클래스의 메서드를 오버라이딩 해서 사용하는것과 동일해 보임. _str_() == toString(); 문자열로 형변환
#_repr_() 은 인스턴스 출력
#-> 즉 현재 있는 메서드를 자신이 원하는 대로 오버라이딩해서 사용

#다른 예시 add() 기능 확장

class Sum:
    def __init__(self, num):
        self.num =num;

# num1 = Sum(20)
# num2 = Sum(30);

# print(num1 +num2);
# -> add() = + 연산자. -> 클래스끼리 더하는 기능은 없음
# 따라서 해당 기능을 확장

class SumClass:
    def __init__(self, num):
        self.num =num
    def __add__(self,other):
        return self.num + other.num;
#self는 자기 자신, other는 다른 객체

num3 = SumClass(20)
num4 = SumClass(30);
print(num3+num4)
print(3+4)
#-> add기능을 확장해서 사용함.

class Complex(object):

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def __repr__(self):
        return "Complex: real = %f imag = %f" % (self.r, self.i)

    def __str__(self):
        return "[for str]" + self.__repr__()

    def __getitem__(self, key):
        if key == "r":
            return self.r
        if key == "i":
            return self.i
# 마치 리스트나 사전처럼 [] 기호를 사용한 인덱싱을 할 수 있다

a = Complex(1,2);

print(a.__repr__())
print(a);
print(a['i'])

#연습문제 2.12.6

class Student:
    def __init__(self, hakbun,name,math,eng):
        self.hakbun = hakbun;
        self.name = name;
        self.math = math;
        self.eng = eng;
    
    def __repr__(self):
        return "이름: %s 학번 %d"  %(self.name, self.hakbun)

    def __str__(self):
        return"[정보]" + self.__repr__()

    def __getitem__(self, key):
        if key == "math":
            return self.math;
        if key == "eng":
            return self.eng ;

s = Student(2013,'나',30,40);
print(s)
print(s["math"])            

