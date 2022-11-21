# 1
# print("갈비탕 {:>10d}원".format(12000))
# print("소불고기 {:>10d}원".format(9000))
# print("김치찌개 {:>10d}원".format(7000))
# print("된장찌개 {:>10d}원".format(7000))
# print("떡볶이 {:>10d}원".format(4000))

# # 2
# records = {'짱구': 72, '철수': 100, '맹구': 82, '훈이': 63, '유리': 91}

# total = 0
# for i in records:
#     total += records[i]
#     avg = total/len(records)
# print(f'총점{total}')
# print(f'평균점수{avg}')
# for i in records:
#     print("{:<7s} {:>4d} {:>4.1f}".format(i, records[i], records[i] - avg))

# # 3-1
# string = 'abc14536qaaawer2po4ai5aua6'
# print(string.replace('a', 'A'))

# # 3-2
# num = [1, 2, 3, 4, 5]
# print(sorted(num, reverse=True))

# # 3-3
# company = "카카오, NAVER, 삼성전자, LG전자"
# print(company.split(','))

# 3-4
# list2 = []
# for i in range(0, 100, 2):
#     list2.append(i)
# print(tuple(list2))

# # 3-5
# apart = [[101, 102], [201, 202], [301, 302]]
# apart.reverse()
# for i in range(0, len(apart)):
#     for j in range(0, len(apart[i])):
#         print(apart[i][j], '호')

# # 3-6
# fruit = ("apple", " peach", "banana", "melon")
# price = (4000, 5000, 1500, 8000)

# result = zip(fruit, price)
# print(dict(result))

# # 4
# number = '032-691-0123'
# list3 = number.split('-')
# print(list3[1])

# # 5
cafe = {'아메리카노': 4100, "카페라떼": 4600, "카푸치노": 5000}
order = input("커피이름: ")
money = int(input("투입금액: "))


def test():
    print(f"{money}원에 {order}를 선택하셨습니다.")
    print(f"잔돈{money}원. 없는 메뉴입니다.")


def test2():
    print(f'{i}는 {cafe[i]}입니다.')
    print(f'잔돈{money}. 커피금액 부족')


def test3():
    print(f"{money}원에 {order}를 선택하셨습니다.")
    print(f'잔돈{money - cafe[i]}원. {i}')


for i in cafe:
    if order != i:
        test()
        break
    elif cafe[i] > money:
        test2()
        break
    else:
        test3()
        break


# # 6

# def find_max(args):
#     print(f'{max(args)}, {min(args)}')


# find_max([5, 3, 2, 6, 8, 10, 9, 1])
