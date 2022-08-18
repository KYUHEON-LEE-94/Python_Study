#Q1
# number = input();
# def is_odd(number):
#     if number%2 == 0:
#         print("짝수");
#     else:
#         print("홀수")    

#Q2
# def number_unlimit(*args):
#     sum = 0;
#     for i in args:
#         sum += i;
#     return sum/len(args)

# print(number_unlimit(1,2,3,4))

#Q3

# input1 = int(input("첫번째 숫자를 입력하세요:"))
# input2 = int(input("두번째 숫자를 입력하세요:"))

# total = input1 + input2
# print("두 수의 합은 %s 입니다" % total)

# print("".join(["you", "need", "python"]))
#Strinbuilder?...

# #Q5
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")

# f1  = open("test.txt", 'r')
# print(f1 .read())
# f1 .close()

#Q6
# text = input();
# f1 = open("test.txt", 'a')
# f1.write('\n'+text);
# f1.close()
#Q7

from dataclasses import replace


f1 = open("test.txt", 'r');
body = f1.read()
f1.close()

body = body.replace('java', 'python');

f1 = open("test.txt", 'w');
f1.write(body)
f1.close()
