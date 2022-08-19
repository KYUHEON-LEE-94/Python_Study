from asyncio.windows_events import NULL
from pickle import NONE


try:
    4/0
except ZeroDivisionError as e:
    print(e)

#finally 구문 사용

# try:
#     f = open('없는 파일', 'r')
# except FileNotFoundError:
#     print('bad')
# finally:
#     f.close()

#else 구문 
# try:
#     age=int(input('나이를 입력하세요: '))
# except:
#     print('입력이 정확하지 않습니다.')
# else:
#     if age <= 18:
#         print('미성년자는 출입금지입니다.')
#     else:
#         print('환영합니다.')
#에러가 없을 경우만 else 구문이 실행됨


#오류 강제 발생 Java에서는 throw

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

# eagle = Eagle();
# eagle.fly()
#오버라이딩 하지 않았으니까 오류가 강제발생함

class Eagle(Bird):
    def fly(self):
        print("날았다")

eagle = Eagle();
eagle.fly()

#내가 만든 예외

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)