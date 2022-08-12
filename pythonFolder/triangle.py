user = {};
user['age'] = 25;
print(user);
user = {'key': 'value'};
print(user);
print(user.get('key'));
print(user.get('value'));

if 2>0:
    print('true');

sum =0;
for i in range(10):
    sum += i;
    print(sum);

for i in range(20):
    if i%2 == 1:
        print(i);