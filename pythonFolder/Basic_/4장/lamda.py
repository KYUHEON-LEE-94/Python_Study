from ast import Lambda
from functools import reduce
from re import T
from warnings import filterwarnings

#기본 lambda
f= lambda x: 2*x
f(2);

#일반적인 함수
def hap(x, y):
    return x+y

hap(10, 20)


# --> lamda로는 아래와 같다.
(lambda x, y: x+y)(10, 20)


def add (x):
    return x+1;



# map() 과 list()

a = [1.1, 2.1, 3.1, 4.1]
a = list(map(int, a))
# ab = list(map(add,a))
# print(ab)
print(a)

b = "12312432"
b = list(map(int, b))
print(b)

# reduce()


print(reduce(lambda x, y: x+y, [1, 2, 3, 4]))
print(reduce(lambda x, y: y+x, '이거대박이네'))
# reduce는 문자열도 하나하나씩 떼어서 누적 +를 해준다.

# filter()
print(list(filter(lambda x: x < 5, range(10))))

#문제
def read(text):
    ridename, limit = map(str.strip, text.split(':'))
    
    cmmin = cmmax = None
    if '~' in limit:
        cmmin, cmmax = map(lambda x: int(x.replace('cm', '')), limit.split('~'))
    elif "이상" in limit:
        cmmin = int(limit.split("cm")[0])

    return ridename, cmmin, cmmax


if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)