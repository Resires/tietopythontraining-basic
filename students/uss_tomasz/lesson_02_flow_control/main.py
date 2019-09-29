"""
Lesson2
https://snakify.org/lessons/if_then_else_conditions/problems/
"""
# Problem Rook move
x_start = int(input("Starting Column of rook movement"))
y_start = int(input("Starting Row of rook movement"))
x_finish = int(input("Finishing Column of rook movement"))
y_finish = int(input("Finishing Row of rook movement"))

if x_start == x_finish or y_start == y_finish:
    print("YES")
else:
    print("NO")

# Problem Chess board - same color
x_start = int(input("Declare first field: Column"))
y_start = int(input("Declare first field: Row"))
x_finish = int(input("Field to check, is it the same color: Column"))
y_finish = int(input("Field to check, is it the same color: Row"))

if (x_start + y_start) % 2 == (x_finish + y_finish) % 2:
    print("YES")
else:
    print("NO")

# Problem King move
x_start = int(input("Starting Column of king movement"))
y_start = int(input("Starting Row of king movement"))
x_finish = int(input("Finishing Column of king movement"))
y_finish = int(input("Finishing Row of king movement"))

if abs(x_start - x_finish) < 2 and abs(y_start - y_finish) < 2:
    print("YES")
else:
    print("NO")

# Problem Bishop moves
x_start = int(input("Starting Column of bishop movement"))
y_start = int(input("Starting Row of bishop movement"))
x_finish = int(input("Finishing Column of bishop movement"))
y_finish = int(input("Finishing Row of bishop movement"))

if abs(x_finish - x_start) == abs(y_finish - y_start):
    print("YES")
else:
    print("NO")

# Problem Queen move
x_start = int(input("Starting Column of queen movement"))
y_start = int(input("Starting Row of queen movement"))
x_finish = int(input("Finishing Column of queen movement"))
y_finish = int(input("Finishing Row of queen movement"))

if abs(x_finish - x_start) == abs(y_finish - y_start) or x_start == x_finish or y_start == y_finish:
    print("YES")
else:
    print("NO")

# Problem Knight move
x_start = int(input("Starting Column of knight movement"))
y_start = int(input("Starting Row of knight movement"))
x_finish = int(input("Finishing Column of knight movement"))
y_finish = int(input("Finishing Row of knight movement"))

if (abs(x_finish - x_start) == 2 and abs(y_finish - y_start) == 1) or \
        (abs(x_finish - x_start) == 1 and abs(y_finish - y_start) == 2):
    print("YES")
else:
    print("NO")

# Problem Chocolate bar
n = int(input("Chocolate bar - Portions height"))
m = int(input("Chocolate bar - Portions length"))
k = int(input("Chocolate bar - Desired squares"))
if n * m < k:
    print("NO")
else:
    if k % n == 0 or k % m == 0:
        print("YES")
    else:
        print("NO")

# Problem Leap year
year = int(input("Year to be checked"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("LEAP")
else:
    print("COMMON")

'''
https://snakify.org/lessons/for_loop_range/problems/
'''
# Problem Factorial
n = int(input("Number for factorial calculation"))
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print("Factorial is ", factorial)

# Problem The number of zeros
quantity = int(input("How many numbers do you want to check?"))
zeros_counter = 0
for i in range(quantity):
    variable = int(input("Number to check (is it 0):"))
    if variable == 0:
        zeros_counter += 1
print("Zero counted: ", zeros_counter)

# Problem Adding factorials
n = int(input("Number to check sum of factorials"))
factorial_sum = n
for i in range(n - 1, 0, -1):
    factorial_sum += 1
    factorial_sum *= i
print("Total sum of following factorials is ", factorial_sum)

# Problem Ladder
ladder_height = int(input("Ladder steps [between 1 and 9] = "))
for row in range(1, ladder_height + 1):
    for column in range(1, row + 1):
        print(column, end='')
    print()

# Problem Lost card
N = int(input("Cards quantity = "))
table = [i+1 for i in range(N)]
while len(table) > 1:
    card = int(input("Enter new card (not present in list of already entered cards)"))
    try:
        table.remove(card)
    except ValueError:
        print("This card was already eliminated. Select another one")
print("Missing card is ", table[0])


'''
https://snakify.org/lessons/while_loop/problems/
'''
# Problem The second maximum
largest = 0
second = 0
while True:
    variable = int(input("Give numbers. 0 will end sequence"))

    if variable > largest:
        second = largest
        largest = variable
    elif variable > second:
        second = variable
    if variable == 0:
        break
print("Second biggest number is ", second)

# Problem The number of elements equal to the maximum
largest = 0
counter = 0
while True:
    variable = int(input("Give numbers. 0 will end sequence"))
    if variable == largest:
        counter += 1
    elif variable > largest:
        largest = variable
        counter = 0
    if variable == 0:
        break
print("Number of elements equal to the maximum is ", counter + 1)
