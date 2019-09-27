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


print("Welcome to organized calculator:")
display_options()
while True:
    print("Enter option:")
    option = input()

    if option == "a":
        print("ADDING")
        (add_var_1, add_var_2) = collect_variables()
        print("Result:")
        print(add_var_1 + add_var_2)

    if option == "s":
        print("SUBTRACT")
        (add_var_1, add_var_2) = collect_variables()
        print("Result:")
        print(add_var_1 - add_var_2)

    if option == "m":
        print("MULTIPLY")
        (add_var_1, add_var_2) = collect_variables()
        print("Result:")
        print(add_var_1 * add_var_2)

    if option == "d":
        print("DIVIDE")
        (add_var_1, add_var_2) = collect_variables()
        print("Result:")
        print(add_var_1 / add_var_2)

    if option == "p":
        print("POWER")
        (add_var_1, add_var_2) = collect_variables()
        print("Result:")
        print(add_var_1 ** add_var_2)

    if option == "h" or option == "?":
        display_options()

    if option == "q":
        print("GOOD BYE")
        break
