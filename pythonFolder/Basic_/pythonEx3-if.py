from cgi import print_form


c = 15
d = 15+15+15

if c > d:
    print("c가크다")
elif c == d:
    print("같다")
else:
    print("d가크다")

a = 48
b = 4
if a % b == 0:
    print(f'{a}는 {b}로 나누어 떨어진다.')
elif a % b != 0:
    print(f'{a}는 {b}로 나누어 떨어지지 않습니다.')

# 문제
sum = 0
while True:
    number = int(input())
    if number < 0:
        break
    else:
        sum += number
        print(sum)
