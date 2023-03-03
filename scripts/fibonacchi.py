
def Fibonacci(n: int) -> int:
    if n in [0, 1]:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

if __name__ == '__main__':
    for i in range(11):
        print(Fibonacci(i), end= ' ')
    print(' ')