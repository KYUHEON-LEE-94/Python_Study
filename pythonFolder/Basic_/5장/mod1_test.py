def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print(__name__)

if __name__ == "__main__":  #해당 파일을 자체실행하는경우.
    print(add(1,4))
    print(sub(4,2))