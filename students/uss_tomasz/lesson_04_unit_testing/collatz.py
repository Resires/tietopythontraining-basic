# The Collatz Sequence
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


if __name__ == '__main__':
    try:
        variable = int(input("Enter number for collatz sequence:"))
        while variable != 1:
            variable = collatz(variable)
            print(variable)
    except ValueError:
        print('Error - not a number')
