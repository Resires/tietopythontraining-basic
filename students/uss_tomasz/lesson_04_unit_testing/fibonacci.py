def fib(n):
    if n < 1:
        return False
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    variable_for_fibonacci = int(input("Enter variable in order to calculate nth fibonacci number"))
    print(fib(variable_for_fibonacci))
