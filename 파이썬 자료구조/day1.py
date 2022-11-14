# 기초 총 복습
# name = "이규헌"

# habbit = input("취미:")
# age = int(input("나이:"))
# print("취미: %s 나이: %d" % (habbit,  age))
# print(f'취미: {habbit}, 나이: {age}')
# print("취미: {}나이: {}".format(habbit, age))

# ------------------------------------------------

# string = 'string python'
# print(f'{string[0]}')
# print(f'{string[2:6],string[6:]}')

# print(f'{string*2}')
# print(f'{string}TEST')

# ---------------------------------------------

# age2 = int(input("나이"))

# if age2 >= 100:
#     print("초고령")
# elif age2 >= 65:
#     print("고령")
# elif age2 >= 40:
#     print("중년")
# elif age2 >= 20:
#     print("청년")
# else:
#     print("미성년")


# score = int(input("점수"))
# if score == 100:
#     print("만점으로 합격")
# elif score >= 80:
#     print("합격")

# ---------------------------------------------
# number = 0
# while number <= 10:
#     print(number)
#     number += 1

# list1 = []
# for i in range(1, 11):
#     list1.append(i)
# print(list1)

# num2 = [i for i in range(1, 31) if i % 2 == 1]
# print(num2)

# -----------------


def getsum(a):
    sum = 0
    for i in range(1, a+1):
        sum += i
    return sum


print(getsum(3))
