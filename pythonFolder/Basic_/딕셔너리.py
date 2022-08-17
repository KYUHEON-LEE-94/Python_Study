from cgi import print_form


x= {"a":10, "b":20};
print(len(x));

#갱신,추가, 삭제
x['a'] = 30;
print(x)

del x['b']
print(x);

#키 확인
print('a' in x)

#딕셔너리 자료형의 반복
#->리스트 자료형처럼 딕셔너리 자료형에 있는 데이터도 for 반복문에 넣을 수 있다. 이 때 딕셔너리 자료형은 내부적으로 자료의 순서를 보장하지 않으므로 특정한 순서로 반복될 것을 기대하면 안된다는 점에 주의

#키 반복
ex = {'a':14, 'b':10, 'c': 12};
for k in ex:
    print(k)
    
print(ex.keys());
for k in ex.keys():
    print(k)

#값 반복
for v in ex.values():
    print(v);

#키와 값의 쌍 반복
for k,v in ex.items():
    print("key: [%s]-> value: [%d]" % (k, v))