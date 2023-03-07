
import time

def timer(function):
    def wraper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        print(f'Function {function.__name__} take {time.time() - start}')
    return wraper

def Fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('Fibonacci function not defined for n < 0')
    elif n in [0, 1]:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

@timer
def Fibonacci1(n: int) -> int:
    if n < 0:
        raise ValueError('Fibonacci function not defined for n < 0')
    elif n in [0, 1]:
        return n
    else:
        penultimate, last = 0, 1
        for i in range(2, n + 1):
            penultimate, last = last, penultimate + last
        return last

if __name__ == '__main__':
    # for i in range(11):
    #     print(Fibonacci1(i), end= ' ')
    n = 40
    start = time.time()
    Fibonacci(n)
    print(f'Function take {time.time() - start}')

    Fibonacci1(n)