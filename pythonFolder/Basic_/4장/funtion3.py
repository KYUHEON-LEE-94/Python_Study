#함수의 결과값은 언제나 하나이다.
def add_mul(a,b):
    return a+b, a*b;

result = add_mul(3,4);
print(result)
# -> 값이 튜플로 나온다. 만약 해당 값들을 각각 받고 싶다면?
result1, result2 = add_mul(3,5);
print(result1)
print(result2)

#매개변수애 초기값 미리 설정

def say_myself(name, age, man=True):
    print('나의 이름은 %s' %name);
    print('나이는 %d입니다.' %age);
    if man:
        print('남자');
    else:
        print('여자');

say_myself('나', 12);
say_myself('나2', 12,False);
#매개변수값이 입력되어 있어도 원하는 매개변수를 다시 넣는것이 가능
