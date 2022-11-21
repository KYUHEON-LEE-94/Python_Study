# ------파일 입출력 쓰기-------
f = open('test1.txt', 'w', encoding='utf-8')  # 현재열려잇는 폴더에 생성
# f = open('./test1.txt', 'w', encoding='utf-8') #현대 폴더
# f = open('../test1.txt', 'w', encoding='utf-8')  # 상위 폴더
f.write('12345\n')
f.write('abcde')
f.write('가나다')

f.close()

# f = open('test2.txt', 'w', encoding='utf-8')
# # 덮어쓰는지 확인
# f.write('hello\n')
# f.write('goodbye\n')
# print('두근두근')

# f = open('test2.txt', 'a', encoding='utf-8')
# # 이어쓰기
# f.write('hello\n')
# f.write('goodbye\n')
# f.write('goodbye\n')
# print('두근두근')
# f.close()

# with문
# 마지막에 오는건 변수명
with open('test3.txt', 'wt', encoding='utf-8') as f:
    f.write('아룡하세요?')
    print('test3.txt 생성')
