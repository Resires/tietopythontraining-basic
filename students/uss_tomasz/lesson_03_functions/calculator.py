def display_options():
    """This function is needed in order to display which are possible inputs for user.
    """
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def collect_variables():
    """Function is asking user to write two integers.
    Returns:
        Two variables. They are needed to calculate result, for example adding
    """
    var_1 = int(input("Input 1st operand:"))
    var_2 = int(input("Input 2nd operand:"))
    return var_1, var_2


def execute_command(command_name, function_type):
    """
    Param:
        command_name - string. this value will be displayed for user in order to identify which command was performed
        function_type - lambda function. containing two arguments and relations between them. Normally it is adding,
        subtracting, multiplying, dividing or power.
    Returns:
        Value is calculated based on two operands from user input and lambda function.
    """
    print(command_name)
    operand1, operand2 = collect_variables()
    print("Result:")
    print(function_type(operand1, operand2))


print("Welcome to organized calculator:")
display_options()
while True:
    print("Enter option:")
    option = input()

    if option == "a":
        execute_command("ADDING", lambda a, b: a + b)

    if option == "s":
        execute_command("SUBTRACT", lambda a, b: a - b)

    if option == "m":
        execute_command("MULTIPLY", lambda a, b: a * b)

    if option == "d":
        execute_command("DIVIDE", lambda a, b: a / b)

    if option == 'p':
        execute_command("POWER", lambda a, b: a ** b)

    if option == "h" or option == "?":
        display_options()

    if option == "q":
        print("GOOD BYE")
        break
