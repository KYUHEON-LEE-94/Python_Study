from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

# 한글을 위한 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

#figure = plt.figure()
#axes = figure.add_subplot(1, 1, 1)
# 1행 1열 1번째 subplot

# 전체 영역 만들기
#figure = plt.figure()

# 1행 2열 1번째
#aexs1 = figure.add_subplot(1, 2, 1)

# 1행 2열 2번째
#aexs2 = figure.add_subplot(1, 2, 2)

# 쉼표 생략가능(단, 2자리는 인식 불가)
#figure = plt.figure()
#axes = figure.add_subplot(111)

# plot(): 꺽은 선형 그래프
#figure = plt.figure()
#axes = figure.add_subplot(111)

# x축과 y축을 리스트 형태로 생성
# 그래프가 1개 일때

#x = [0, 1, 2, 3, 4]
#y = [2, 5, 3, 1, 5]
#axes.plot(x, y)
# plt.show()

# 그래프가 여러개일때
#figure = plt.figure()
#axes = figure.add_subplot(111)
#x1 = [0, 1, 2, 3, 4]
#y1 = [2, 6, 5, 1, 3]

#x2 = [0, 1, 2, 3, 4]
#y2 = [2, 5, 3, 5, 1]
#axes.plot(x1, y1)
#axes.plot(x2, y2)
#axes.plot(x1, y1, x2, y2)
# plt.show()

# 굵기와 선모양, 색상, 점 표시 등 변경 가능
# figure = plt.figure()
# axes = figure.add_subplot(111)

# x1 = ['1월', '2월', '3월', '4월', '5월']
# y1 = [2, 5, 1, 7, 2]

# x2 = ['1월', '2월', '3월', '4월', '5월']
# y2 = [2, 5, 5, 1, 7]
# axes.plot(x1, y1, linestyle='dashed', linewidth='5.0')
# axes.plot(x2, y2, color='r', marker='.', linewidth='2.5')

# 6월부터 12월까지 => 그래프 2개 생성
# 과자 판매량을 본인이 맘에 드는 만큼 설정
# figure = plt.figure()
# axes = figure.add_subplot(111)

# x1 = ['6월', '7월', '8월', '9월', '10월', '11월', '12월']
# y1 = [1, 4, 2, 3, 5, 7, 6]

# x2 = ['6월', '7월', '8월', '9월', '10월', '11월', '12월']
# y2 = [1, 2, 3, 5, 6, 1, 7]

# axes.plot(x1, y1, color='r', linestyle='dashed', marker='*')
# axes.plot(x2, y2, color='black', marker='|')

# plt.show()

# 그리드 옵션 추가기능
# plt.grid()

# 3 bar(): 막대그래프
# figure = plt.figure()
# axes = figure.add_subplot(111)
# x = ['봄', '여름', '가을', '겨울']
# y = [250, 100, 230, 300]
# axes.bar(x, y)
# plt.title("계절별 통계")
# plt.xlabel("계절")
# plt.ylabel("매출액")
# plt.show()

# scatter(): 산포그래프
# figure = plt.figure()
# axes = figure.add_subplot(111)
# x1 = ['봄', '여름', '가을', '겨울']
# y1 = [250, 100, 230, 300]
# axes.scatter(x1, y1, s=100, c='red')
# plt.show()

# pie(): 원형그래프
figure = plt.figure()
axes = figure.add_subplot(111)
labels = ['봄', '여름', '가을', '겨울']
ratio = [25, 10, 23, 30]  # 100을 기준으로 %계산
axes.pie(ratio, labels=labels, autopct="%.1f%%")
# autopct는 부채꼴 안에 표시될 숫자의 형태를 지정할 수 있는 옵션
# %.1f 소수점 한자리까지 출력 , %% => %를 표시, %를 아예 안쓰고 싶다면 맨 뒤에 %를 작성하지 않는다.
plt.show()
