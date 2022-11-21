# 복습
class Test:
    def __init__(self, color):
        self.color = color

# test = Test('red')
# print(test.color)


# 예외처리
# 1) 고전적인 예외처리


def div(x):
    return 10/x


# result = div(0)
# print(result)

# 2) if~else로 예외처리
# num1 =3
# num2 = 0
# if num2 == 0:
#     print("0으로 나누는 것은 불가능")
# else:
#     print(num1/num2)

# 2) 예외처리 구문 활용

# try:
#     num1 = int(input("제수를 입력해주세요: "))
#     num2 = int(input("피제수를 입력해주세요: "))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("0으로 나눌수 없어")
# except ValueError:
#     print('정수만 입력가능합니다.')
# except Exception:
#     print("알수없는 예외가 발생했습니다.")

# --다른 예시--
# print("프로그램 시작")
# try:
#     arr = ['h', 'e', 'l', 'l', 'o']
#     print(arr[0])
#     print('try문 실행')
# except IndexError:
#     print('except문 실행')
# else:
#     print('else문 실행')
# finally:
#     print('finally실행')
# print('프로그램 종료')


# ---예외 강제 발생---

# num = int(input("1~5까지 숫자입력: "))
# if num < 1 or num > 5:
#     raise
# print(f'입력한 값은: {num}입니다.')

# ----존재하는 exception 발생----

# num = int(input("1~5까지 숫자입력: "))
# if num < 1 or num > 5:
#     raise ValueError
# print(f'입력한 값은: {num}입니다.')

# ----내가 원하는 문장 넣기----

# num = int(input("1~5까지 숫자입력: "))
# if num < 1 or num > 5:
#     raise Exception("에러라고 에러라고")
# print(f'입력한 값은: {num}입니다.')


# try~except
# try:
#     num = int(input("1~5까지 숫자입력: "))
#     if num < 1 or num > 5:
#         raise
#     print(f'입력한 값은: {num}입니다.')
# except:
#     print(f'1~5값만 입력하세요')
