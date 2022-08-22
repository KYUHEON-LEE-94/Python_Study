#abs()
#어떤 숫자를 입력받았을때, 그 숫자의 절대값을 반환
from cgitb import reset
import pstats


print(abs(3));
abs(-3)

#all() 반복가능한 자료형을 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
# *반복 가능한 자료형: for문으로 그 값을 출력할 수 있는 것을 의미한다. 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.

all([1,2,3]);
all([1,2,3,0]);

#any(x) 반복 가능한 자료형 x를 입력 인수로 받으며 이 x의 요소 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일때만 False를 돌려준다.
print(any([1,2,3,0]))
print(any([0,""]))

#chr
print(chr(97))
print(chr(44032))

#dir
#객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.

a = [1,2,3,4]
print(dir(a))

#divmod(a,b)
# 2개의 숫자를 입력받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.

print(divmod(7,3))

#enumerate
#순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate객체를 돌려준다.

for i, name in enumerate(['1','2','3']):
    print(i,name)

#eval(expresstion)
#실행 가능한 문자열을 입력받아 문자열을 실행한 결괏값을 돌려주는 함수이다.
print(eval('1+2'))
#문자열로 숫자를 더했음에도 불구하고 실행되는 것을 확인할 수 있다.
print(eval('divmod(7,3)'))

#filter
#첫번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 그리고 두 번쨰 인수인 반복 가능한 자료형 요소가 첫번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서 돌려준다.

def positive(l):
    result = []
    for i in l:
        if i >0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))

#->를 간단하게 filter함수로 가능

def positive2(x):
    return x>0;
print(list(filter(positive2, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x: x>0,  [1, -3, 2, 0, -5, 6])))

#hex    정수값을 입력받아 16진수로 반환
print(hex(123123))

#id 객체를 입력받아 객체의 고유 주소값 반환

a= 3;
print(id(a))

#isinstance(object, class) 첫번째 인수로 인스턴스, 두 번째 인수로 클래스이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.

class Person: pass

a= Person();
print(isinstance(a, Person))

b =3
print(isinstance(b, Person))

#list(s)는 반복 가능한 자료형 s를 받아서 리스트로 만들어 돌려주는 함수

test = list("python")
print(test)

#map(f, iterable)은 함수와 반복가능한 자료형을 입력받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.

# def two_times(numberlist):
#     result = []
#     for number in numberlist:
#         result.append(number*2);
#     return result

# result = two_times([1,23,4]);
# print(result)

# 아래와 같이 변경
def two_times(x):
    return x*2

print(list(map(two_times, [1,2,3,4])))

print(list(map(lambda x: x*2, [1,2,3,4])))

#max()/min() -> int뿐만 아니라 String의 최대값 최소값도 반환해준다.

# oct는 정수 형태의 숫자를 8진수 문자열로 반환

print(oct(34))

#ord(c): 문자의 유니코드 값을 돌려준다.

#pow(x,y): x의 y제곲값을 반환

#range(x,y,z) x값 이상 y값 미만 z값의 차이만큼.

#sorted 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.

print(sorted([3,8,5,1,2]))

#type은 입력값이 어떤 자료형인지 알려줌.

#zip는 동일한 개 수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.

print(list(zip([1,2,3],[4,5,6],[7,8,9])))