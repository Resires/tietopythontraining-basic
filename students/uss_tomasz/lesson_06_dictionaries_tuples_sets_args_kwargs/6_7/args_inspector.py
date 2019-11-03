def inspect_args(*args, **kwargs):
    for argument in args:
        print("Argument = ", argument)
    for argument in kwargs:
        print("Argument type", argument, "has value of", kwargs[argument])


inspect_args(1, 2, 3, length="4", width="5")
