# fruits = ['사과', '바나나', '망고', '배', '복숭아', '감']
# if '배' in fruits:
#     fruits.remove('배')
# else:
#     print("배는 fruits안에 없습니다.")
# print(fruits)

# for i in range(1, 101):
#     if (i % 2 != 0):
#         print(f'{i}', end=' ')


# sum = 0
# for i in range(0, 5):
#     number = int(input("정수 입력: "))
#     if (number < 0):
#         number = int(input("다시 입력해주세요: "))
#     sum += number
# print(sum)

# month = int(input("몇개월 할부?: "))
# print(f'매달 내는돈: {500000/month}')


# i = 0
# while i < 10:
#     i += 1
#     j = 2
#     while j < 10:
#         print(f'{j}X{i}={i*j}', end='\t')
#         j += 1
#     print()


# chance = 0
# while chance < 3:
#     passwd = input("비밀번호는? ")
#     if (passwd == 'qwerty'):
#         break
#     chance += 1


for i in range(4):
    for j in range(4):
        print(i+j, end=' ')
    print()


# list2 = ["Life is too short"]
# list3 = ["exit "]
# print(list2+list3)

# list4 = []
# for z in range(5):
#     number2 = int(input("숫자 입력"))
#     list4.append(number2)
# list4.reverse()
# print(list4)

# numbers = [-9, -11, 0, 2, 9, 10, -36, 47]
# print(max(numbers))
# print(min(numbers))
# numbers.sort()
# print(numbers)
