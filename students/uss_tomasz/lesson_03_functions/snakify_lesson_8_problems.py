"""
https://snakify.org/lessons/functions/problems/
"""


# Problem The length of the segment
def distance(x1, y1, x2, y2):
    return ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5


first_point_x = int(input("First point, x coordinate = "))
first_point_y = int(input("First point, y coordinate = "))
second_point_x = int(input("Second point, x coordinate = "))
second_point_y = int(input("Second point, y coordinate = "))
print("Distance between ({0},{1}) and ({2},{3}) equals {4}".format(first_point_x,
                                                                   first_point_y,
                                                                   second_point_x,
                                                                   second_point_y,
                                                                   distance(first_point_x,
                                                                            first_point_y,
                                                                            second_point_x,
                                                                            second_point_y)))


# Problem Negative exponent
def power(a, n):
    if n < 0:
        a = 1 / a
        n *= -1

    result = 1
    for i in range(n):
        result *= a
    return result


base = float(input("Power with loops: Base = "))
exponent = int(input("Power with loops: Exponent [integer]"))
print(power(base, exponent))


# Problem Exponentiation
def power_without_loops(a, n):
    if n == 1:
        return a
    else:
        return a * power_without_loops(a, n-1)


base = float(input("Power without loops:Base = "))
exponent = int(input("Power without loops: Exponent [integer]"))
print(power_without_loops(base, exponent))


# Problem Fibonacci numbers
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


variable_for_fibonacci = int(input("Enter variable in order to calculate nth fibonacci number"))
print(fib(variable_for_fibonacci))
