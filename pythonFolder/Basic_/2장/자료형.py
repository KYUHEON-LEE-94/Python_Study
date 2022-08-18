#변수의 메모리 크기를 알기 위해서는 sys패키지의 getsizeof 명령을 사용한다.

from sys import getsizeof 

a= 1;
print(getsizeof(a));

b= 'b';
print(getsizeof(b));

#파이썬의 자료형
# NoneType bool int float complex str tuple list dict function

#자료형을 알아보려면 type()을 사용
print(type(True));

#자료형과 클래스
#클래스를 알고 싶다면 __class__사용

print(a.__class__)

class C(object):
    pass #아무런 일도 하지않는 들여쓰기 블럭을 만들기 위한것!

c = C();
print(c)

#불변형 자료형과 변형 자료형
#정수, 실수, 문자열, 튜플은 불변형 자료형
#리스트, 딕셔너리는 변형 자료형

x =1
print(id(x))

x =2;
print(id(x));

#불변형 자료형은 해당 주소에서 값이 바뀌는 것이 아니라 전혀 새로운 주소에 값이 씌여지고 x는 새로운 위치를 가리키게 됨

z = [1];
print(id(z))

print(id(z[0]))
# z는 리스트 변형 자료형을 가리키고, 리스트 변형 자료형의 첫번째 원소는 불변형 자료형인 정수 1을 가르킨다.
#z -> 리스트 변형 자료형 -> 불변형 자료형

z[0] =3;
print(id(z))
print(id(z[0]))

#z가 가르키는 리스트 변형 자료형의 주소는 변하지 않고, 리스트 변형 자료형이 가르키는 불변형 자료형의 주소값이 변한다.