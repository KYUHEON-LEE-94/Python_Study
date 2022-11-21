# format()
print("------------format()-------------")
print("10자리 왼쪽정렬 '{:<10d}'".format(123))
print("10자리 오른쪽정렬 '{:>10d}'".format(123))
print("10자리 중앙정렬 '{:^10d}'".format(123))

# 공백으로 비워진 자리에 *를 채움
print("10자리 왼쪽정렬 '{:*<10d}'".format(123))
print("10자리 오른쪽정렬 '{:*>10d}'".format(123))
print("10자리 중앙정렬 '{:*^10d}'".format(123))

print("------------count()-------------")
# count()
string = "내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다."
print(string.count("기린"))

string1 = 'best of best'
print(string1.count('best'))
print(string1.count('best', 5))  # 인덱스로도 확인가능
print(string1.count('best', -7))

# find()
# 해당 문자열의 index를 찾아옿
print("------------find()-------------")
a = 'apple'
print(a.find('p'))
print(a.find('z'))

string1 = 'best of best'
print(a.find('best'))
print(a.find('best', 5))
print(a.rfind('best'))

# index()
print("------------index()-------------")
print(a.index('p'))
print(a.index('l'))
# print(a.index('d')) 에러발생

# join
# 반복가능 객체
# 딕셔너리는 키만 이용해서 가능
print("------------join()-------------")
print('+'.join(['p', 'y', 't', 'h', 'o', 'n']))
print('-'.join(('x', 'y', 'z')))
print(','.join({'x': 10, 'e': 10, 'e': 10}))

# split()
print("------------split()-------------")
string2 = 'Life is too short'
print(string2.split())

number = '010.12-34.12-34'
print(number.split('.'))
print(number.split('-'))

# replace()
print("------------replace()-------------")
print(string2)
print(string2.replace('short', 'long'))
print(number.replace('-', ''))

# 불필요한 문자열 제거메서드
print("------------strip()-------------")
a = '123         '
ac = '123**********'
b = '           123'
c = '   123    '
print("길이>: ", len(a), "메서드사용>: ", a.rstrip())
print("길이>: ", len(ac), "메서드사용>: ", ac.rstrip('*'))
print("길이>: ", len(b), "메서드사용>: ", b.lstrip())


# 사용자 정의 함수
print("------------함수()-------------")


def welcome():
    print("hello world")
    print('Pyton')


welcome()

# default 매개변수


def greet(message='hello'):
    print(message)


greet("안녕하세요")
greet()

# 가변 매개변수


def show(*args):
    print(*args)


show("안녕", "넌 누구냐")
