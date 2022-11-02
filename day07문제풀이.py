# month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# for idx, item in enumerate(month):
#     print(f'{idx+1}월은 {item}일까지')

# getlist = []
# while len(getlist) < 3:
#     fruit = input("원하는 과일: ")
#     if fruit in getlist:
#         print("동일한 과일이 있습니다.")
#         continue
#     getlist.append(fruit)
#     print(f'입력이 {3-len(getlist)}번남았습니다.')
# print(tuple(getlist))

# print(getlist)


# capital = []
# while len(capital) < 5:
#     cap = input("수도")
#     capital.append(cap)
# print(tuple(capital))

# 4. 학생 수와 학생별 파이썬, 자바, C언어 점수를 입력받고, 학생별 평균 점수를 구하는 프로그램

# 조건1. 평균 점수는 소수점 셋째 자리에서 반올림하여 계산
# 조건2. 학생의 이름과 평균점수는 딕셔너리 형태로 생성하고, 학생수는 입력받아 작성할 수 있도록 할 것
# 조건3. 점수는 0~100사이의 양의 정수만 입력받도록 조건 설정할 것
# 조건4. 0~100 사이의 양의 정수가 아니라면 '잘못된 입력입니다' 출력

student_dict = {}
num = int(input("학생수 입력: "))

for count in range(num):
    score = 0
    step = len(student_dict)+1
    name = input(f'{step}번째 학생 이름 입력: ')

    while True:
        p = int(input(f"{step}번째 학생 점수 입력: "))
        if 0 <= p <= 100:
            score += p
            break
        else:
            print("잘못된 입력입니다.")
    student_dict[name] = round(float(score/3), 2)
print(student_dict)
