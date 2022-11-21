cities = {"korea": "서울", "japna": "도쿄", "china": "베이징"}
print(cities, type(cities))
# 키 값 중복은 불가능하다
print(cities['korea'], type(cities['korea']))
print(cities.keys(), type(cities.keys()))
print(cities.values(), type(cities.values()))
print(cities.items(), type(cities.items()))

# DICT 추가
cities['germany'] = '베를린'
print(cities)

# DICT 변경
cities['korea'] = '부산'
print(cities)

# 문자열 내장 함수
print('----문자열 내장 함수---------')

print('\n----chr()---------')  # 유니코드 값을 찾는 함수
print(chr(48), type(chr(48)))
print(chr(49), type(chr(49)))
print(chr(65), type(chr(65)))

print('\n----eval()---------')
print(eval('100+200'), type(eval('100+200')))  # 문자열임에도 불구하고 자동 형변환함
num = 50
print(eval('num*3'), type(eval('num*3')))

print('\n----format()---------')
print(format(10000), type(format(10000)))  # str로 나옴
print(format(10000, ','), type(format(10000, ',')))
print(format(10000, '_'), type(format(10000, '_')))

print('\n----str()---------')
print(str(100), type(str(100)))
print(str(1.5), type(str(1.5)))
print(str(True), type(str(True)))

# 숫자 내장 함수
print('----숫자 내장 함수---------')

print('\n----abs()---------')  # 절대값 반환
print(abs(10), type(abs(10)))
print(abs(-10), type(abs(-10)))

print('\n----divmod()---------')  # 몫과 나머지를 한쌍의 결과로 반환
print(divmod(10, 3), type(divmod(10, 3)))  # (3, 1) 튜플 형태로 반환

print('\n----float()---------')
print(float(3), type(float(3)))

print('\n----max()---------')
list1 = [1, 5, 8, 0, 4]
print(max(list1))

print('\n----min()---------')
print(min(list1))

print('\n----pow()---------')
print(pow(10, 2))
print(10**2)  # 위와 아래는 동일

print('\n----round()---------')  # 오사오입
print(round(1.5))  # 앞자리가 홀수일때는 올림
print(round(2.5))  # 앞자리가 짝수일때는 버림

print('\n----sum()---------')
list3 = [1, 2, 3, 4, 5]
print(sum(list3))

print('\n----enumerate()---------')
# 리스트가 있을 때 (idx, 값)
for item in enumerate(['가위', '바위', '보']):
    print(item)

for idx, item in enumerate(['가위', '바위', '보']):
    print(item)

print('\n----range()---------')
print(range(10), type(range(10)))
print(list(range(10)), type(list(range(10))))
print(tuple(range(10)), type(tuple(range(10))))

print('\n----len()---------')
list4 = ['a', 'b', 'c', 'd']
print(len(list4))
dict1 = {'a': 'apple', 'b': 'banana'}
print(len(dict1))

print('\n----sorted()---------')  # 오름차순 정렬
list5 = [6, 3, 7, 1, 5, 9]
print(list5)
list5_copy = sorted(list5)
print(list5_copy)  # 오름차순

list5_copy2 = sorted(list5_copy, reverse=True)
print(list5_copy2)  # 내림차순

print('\n----zip()---------')
names = ['kys', 'james', 'sunny']
scores = [60, 70, 40]
for student in zip(names, scores):
    print(student, type(student))

for name, score in zip(names, scores):
    print(f'{name}의 점수는 {score}입니다.')

# 리스트에 월별 일수 저장하고 1월부터 12월까지 월별 일수를 출력하는 프로그램
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for idx, item in enumerate(month):
    print(f'{idx+1}월은 {item}일까지')
