# 모듈
import math
import random
print('------random 모듈------')

# print(random.random())  # 0이상 1미만의 숫자 중에서 아무 숫자나 하나를 뽑아서 반환
# print(random.randrange(1, 7))

# alph = ['a', 'b', 'c', 'd', 'e']
# random.shuffle(alph)
# print(alph)
# print(random.choice(alph))
# print(random.uniform(3.5, 7.5))  # a<=x <b 실수형 반환
# print(random.randint(5,10)) #정수형 반환


# 1부터45까지 랜검한 6개 숫자를 뽑아 출력하기
list1 = []
for i in range(6):
    list1.append(random.randrange(1, 46))


print(list1)

print('------math 모듈------')
print(math.pi)
print(math.ceil(3.14))
