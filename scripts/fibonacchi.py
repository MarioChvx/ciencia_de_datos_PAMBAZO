
def Fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('Fibonacci function not defined for n < 0')
    elif n in [0, 1]:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

if __name__ == '__main__':
    for i in range(11):
        print(Fibonacci(i), end= ' ')
    print(' ')
    print(Fibonacci(-22))