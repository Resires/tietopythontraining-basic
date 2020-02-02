def sort_decorator(func):
    def inner_function():
        return sorted(func())
    return inner_function


@sort_decorator
def data_feeder():
    return [4, 2, 1, 3]


print("Sorted feeder = ", data_feeder())
