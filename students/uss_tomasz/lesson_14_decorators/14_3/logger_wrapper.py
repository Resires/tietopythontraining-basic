def logger_wrapper(foo):
    def function_wrapper(*args, **kwargs):
        print("Arguments passed to function {}:".format(foo.__name__))
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
    return function_wrapper


@logger_wrapper
def biggest(arguments):
    top = float('-inf')
    for argument in arguments:
        if argument > top:
            top = argument
    return top


@logger_wrapper
def second_biggest(arguments):
    top = float('-inf')
    second = float('-inf')
    for argument in arguments:
        if argument > top:
            top, second = argument, top
        elif top > argument > second:
            second = argument
    return second


@logger_wrapper
def sorting(arguments):
    arguments.sort()
    return arguments


if __name__ == '__main__':
    print("Biggest value = ", biggest(1, 2, 4, height='3', lenght='5'), "\n")
    print("Second biggest value =", second_biggest(1, 2, 4, height='3', lenght='5'), "\n")
    print("Sorted elements: ", sorting(1, 2, 4, height='3', lenght='5'), "\n")
