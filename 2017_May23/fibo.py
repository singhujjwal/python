from time import sleep

def fibo(x):
    a, b = 0, 1
    for i in range(x):
        print(a, end=" ")
        a, b = b, a + b

def fibo_list(x):
    series = [0, 1]
    for i in range(x-2):
        sleep(1)
        series.append(series[-1] + series[-2])
    return series

def fibo_gen(x):
    a, b = 0, 1
    for i in range(x):
        sleep(1)
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    for i in fibo_gen(10):
        print(i, i*i)

