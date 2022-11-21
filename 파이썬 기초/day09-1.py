# def print_my_name():
#     print('이규헌')


# print_my_name()


# def sum_num(n1, n2=20):
#     print(f'n1={n1}')
#     print(f'n2={n2}')
#     sum_result = n1 + n2
#     return sum_result


# print(sum_num(3))


# def my_func(n1, n2):
#     return (n1+n2)*2


# print(my_func(7, 9))


# def add_func(*num):
#     result = 0
#     for i in num:
#         result += i
#     return result


# print(add_func(5, 9, 17))


# def calc(a, b):
#     return a+b, a-b, a*b, a/b


# print(calc(3, 1))
# 여러개 값을 반환할때 tuple형식으로 나옴

# 매개변수에 따라 *출력
# def makeStar(number):
#     print('*'*number)


# makeStar(3)
# ---------------------------------------------
# 입력받은 거에 따라서 출력
# string = input("문자열: ")
# numbers = int(input("문자열 개수: "))


# def Copystring(numbers, string='*'):
#     print(string*numbers)


# Copystring(numbers, string)

# 람다 함수
# 함수명 = lambda 매개변수1, 매개변수2..: 반환식


print("-----------람다 함수----------")
# test = lambda x, y:  x+y

# print(test(1,2))

# test2 = lambda x,y=2 : x+y
# print(test2(1))
# print(test2(1,3))

# 다중 입력
# test3 = lambda *x: max(x)*2
# print(test3(1, 2, 3, 4, 5))

# # 다중 반환
# f = [lambda x:x+1, lambda x: x+2, lambda x: x+3]
# print(f[0](1))
# print(f[1](2))
# print(f[2](3))

# # 최대 최소
# list1 = [[9, 1], [8, 2], [7, 3], [6, 4]]
# max1 = max(list1, key=lambda x: x[0])
# max2 = max(list1, key=lambda x: x[1])
# print(max1)
# print(max2)

# min1 = min(list1, key=lambda x: x[0])
# min2 = min(list1, key=lambda x: x[1])
# print(min1)
# print(min2)

# 정렬
# list2 = ['가', '각', '감', '값', '+', '!', '/', '간', '강', ']']
# list2.sort(key=lambda x: x)
# print(list2)

# print([ord(i) for i in list2])

# 복합정렬
# i = [[3, 'd'], [5, 'c'], [1, 'a'], [0, 'b'], [0, 'a']]
# i1 = sorted(i, key=lambda x: -x[0])
# i2 = sorted(i, key=lambda x: x[1])
# i3 = sorted(i, key=lambda x: [x[0], x[1]])

# print(i1)
# print(i2)
# print(i3)

print("-----------맵 함수----------")
# MAP 함수

# def f(x): return x > 0
# def g(x): return x**2


# print(map(f, range(-5, 5)))
# print(list(map(f, range(-5, 5))))
# print(list(map(g, range(5))))

# # 형변환
# data = [-1, 3, 5.5, 5.3]
# f = map(int, data)
# # 두번째 인자를 첫번째 함수에 돌아가면서 넣어서 계산한다.
# print(list(f))

# 특정연산 적용
# def calc(x):
#     return (x/2) + 1


# data = [-1, 3, 5.5, 5.3]
# f = map(calc, data)
# print(list(f))


# 실수가 저장된 리스트가 있을 때 리스트의 모든 요소를 정수로 변환
# a = [1.4, 3.1, 5.9, 6.8]
# f = map(int, a)
# print(list(f))
print("-----------필터 함수----------")
# 필터함수
def f(x): return x > 0


print(list(filter(f, range(-5, 5))))

print("-----------문제 풀기----------")
# 사용자로부터 값을 1개 입력받고, 정수로 입력받은 것을 실수로 변환하기

# 1
# print(list(map(float, input("정수 입력"))))

# 2
names = ["짱구", "철수", "훈이", "맹구"]


def callname(names):
    for i in names:
        print(f"안녕 {i}야")


callname(names)

print("-----------전역 변수와 지역변수----------")
# 전역변수
value = 100


def changeValue():
    value = 20
    print(f'value={value}')


changeValue()


def changeValue2():
    global value
    value = 20


changeValue2()
print(f'value={value}')
