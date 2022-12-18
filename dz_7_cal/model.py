x = None
y = None  # пустой объект

def init(a,b):
    global x
    global y
    x = int(a)
    y = int(b)

def summa():
    return x + y

def raznica():
    return x - y