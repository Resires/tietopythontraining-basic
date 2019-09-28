from math import ceil
'''
https://snakify.org/lessons/print_input_numbers/problems/
'''
# Problem Sum of three numbers
adding_number_1 = int(input("First number for adding = "))
adding_number_2 = int(input("Second number for adding= "))
adding_number_3 = int(input("Third number for adding= "))

print("Sum of them is", adding_number_1 + adding_number_2 + adding_number_3)

# Problem Hi John
name = input("What is your name?")
print("Hi", name)

# Problem Square
variable_before_square = int(input("Input variable which will be squared= "))
print("Squared = ", variable_before_square ** 2)

# Problem Area of right-angled triangle
base_length = float(input("Length of triangle base = "))
height = float(input("Height of triangle = "))
print("Area of triangle is", base_length * height / 2)

# Problem Hello, Harry!
name = input("What is your name?")
print("Hello, " + name)

# Problem Apple sharing
N = int(input("Students quantity = "))
K = int(input("Apples quantity = "))
print("Each students receive", K // N, "apples")
print(K % N, "apples remains in the basket")

# Problem Previous and next
number = int(input("Number = "))
print("The next number for the number", number, "is", number + 1)
print("The previous number for the number", number, "is", number - 1)

# Problem Two timestamps

earlier_h = int(input("starting time, hour = "))
earlier_m = int(input("starting time, minute = "))
earlier_s = int(input("starting time, second = "))
later_h = int(input("finishing time, hour = "))
later_m = int(input("finishing time, minute = "))
later_s = int(input("finishing time, second = "))

later_seconds = 3600 * later_h + 60 * later_m + later_s
earlier_seconds = 3600 * earlier_h + 60 * earlier_m + earlier_s
print("Seconds difference = ", later_seconds - earlier_seconds)

# Problem School desks
students_counts = [
    int(input("Students in first class = ")),
    int(input("Students in second class = ")),
    int(input("Students in third class = ")),
]
print("Desk needed = ", sum([ceil(count / 2) for count in students_counts]))

'''
https://snakify.org/lessons/integer_float_numbers/problems/
'''
# Problem Last digit of integer
variable = int(input("Variable = "))
print("Last digit of ", variable, "is", variable % 10)

# Problem Tens digit
variable = int(input("Variable = "))
print("Digit of tenths of ", variable, "is", variable % 100 // 10)

# Problem Sum of digits
variable = int(input("Variable made of three digits = "))
sum_of_digits = variable % 10
variable = variable // 10
sum_of_digits += variable % 10
variable = variable // 10
sum_of_digits += variable
print("Sum of digits = ", sum_of_digits)

# Problem Fractional part
variable = float(input("Float variable = "))
print("Fractional part of", variable, "is", variable - int(variable))

# Problem First digit after decimal point
variable = float(input("Float variable = "))
print("First digit after decimal point of ", variable, "is")
variable *= 10
variable = variable % 10
print(int(variable))

# Problem Car route

N = float(input("Daily car distance [km] = "))
M = float(input("Total distance to cover [k] ="))
print("Days needed = ", ceil(M / N))

# Problem Digital clock
N = int(input("Minutes since midnight = "))
print("Hour =", N // 60, "Minute =", N % 60)

# Problem Total cost
A = int(input("Dollars cost = "))
B = int(input("Cents cost = "))
N = int(input("Cupcakes quantity = "))
total_cost = (A * 100 + B) * N
print("You will pay", total_cost // 100, "$", total_cost % 100, "c")

# Problem Clock face - 1
h = int(input("Hours = "))
m = int(input("Minutes = "))
s = int(input("Seconds = "))
total_time = 12 * 3600
current_time = h * 3600 + m * 60 + s
angle = current_time / total_time * 360
print("Hour hand will move ", angle, "degrees")
