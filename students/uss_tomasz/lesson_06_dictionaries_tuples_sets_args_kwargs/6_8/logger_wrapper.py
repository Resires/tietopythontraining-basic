def logger_wrapper(foo, *args, **kwargs):
    for argument in args:
        print("Argument = ", argument)
    for argument in kwargs:
        print("Argument type", argument, "has value of", kwargs[argument])
    arguments_list = []
    for i in args:
        arguments_list.append(i)
    for i in kwargs:
        arguments_list.append(int(kwargs[i]))
    return foo(arguments_list)


print("Sum result =", logger_wrapper(sum, 1, 2, length='3', height='4'))
print("Max result =", logger_wrapper(max, 1, 2, length='3', height='4'))
