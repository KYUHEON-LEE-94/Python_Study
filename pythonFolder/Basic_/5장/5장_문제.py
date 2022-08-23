#Q1

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
# #위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자. 즉 다음과 같이 동작하는 클래스를 만들어야 한다.

# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val

# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)

#Q2
#객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자. 즉 다음과 같이 동작해야 한다.

class MaxLimitCalculator(Calculator):
        def add(self, val):
            self.value += val
            if self.value >100:
                self.value = 100;


cal = MaxLimitCalculator()
cal.add(50)
cal.add(80) 

print(cal.value) # 100 출력
 
#Q4 filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.

print(list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3])))

#Q5
#234라는 10진수의 16진수는 다음과 같이 구할 수 있다.

hex(234)
#이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해 보자.

print(int('0xea', 16))

#Q6 map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.

print(list(map(lambda x: x*3, [1, 2, 3, 4])))

#Q7 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
print(max([-8, 2, 7, 5, -3, 5, 0, 1]) + min([-8, 2, 7, 5, -3, 5, 0, 1]))

#Q8
print(round( 17 / 3, 4))

import time

print(time.strftime('%Y/%m/%d/%A', time.localtime(time.time())))