# def f1(x):
#     a = 3
#     b = 5
#     y = a*b+x
#     return y


# print(f1(3))

# 문제 숫자를 입력받으면 한글로 반환
# number = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십']

# z = 1
# while z < 10:
#     i = int(input())
#     print(number[i])
#     z += 1

# 문제 triple 함수 완성
def tripe(x):
    return x*3


print(tripe(2))
print(tripe("x"))

#여러개의 매개변수 받기
#->*args는 튜플인점 기억하기!
def add_many(*what):
    result = 0
    for i in what:
        result += i;
    return result

print(add_many(1,2,3,4,5));
print(add_many(5,6,7))

#다른 방법

def add_other(text, *what):
    if text == 1:
        sum = 0;
        for i in what:
            sum += i;

    elif text == '2':
        sum = 1;
        for i in what:
            sum *= i;
    return sum

something = add_other(1, 1,2,3,4)
print(something);

# *kwargs
# **이 두개!
def print_kwargs(**kwargs):
    print(kwargs);

print_kwargs(a=1);
print_kwargs(name ="name", age=10);
