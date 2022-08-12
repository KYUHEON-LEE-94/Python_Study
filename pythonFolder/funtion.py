def add(x, y, z):
    return x+y+z


print(add(10, 20, 30))

a = "good"
print(a.upper())
print(a.count('o'))
print(a.replace("good", "zood"))
b = "This is sentence"
print(b.swapcase())
aray = b.split()
print(aray)


print(type(str(3)))


def square(x, y):
    return (x*y)/2


print(square(10, 4))

b = int(input())
i = 1
while i <= b:
    print(i)
    i += 1

# 구구단


def gugudan(x):
    for i in range(1, 10):
        print(i, "x", x, "=", i*x)


gugudan(2)
