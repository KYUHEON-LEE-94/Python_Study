#abs()
#어떤 숫자를 입력받았을때, 그 숫자의 절대값을 반환
from cgitb import reset


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