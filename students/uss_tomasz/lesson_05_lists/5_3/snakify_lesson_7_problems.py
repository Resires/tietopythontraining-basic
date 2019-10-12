# https://snakify.org/lessons/lists/problems/
from random import randint, seed
from collections import OrderedDict


def remove_duplicates(list_from_user):
    return list(OrderedDict.fromkeys(list_from_user))


def quantity_of_bigger_than_both_neighbours(list_from_user):
    quantity = 0
    for i in range(1, len(list_from_user) - 1):
        if list_from_user[i] > list_from_user[i-1] and list_from_user[i] > list_from_user[i+1]:
            quantity += 1
    return quantity


seed(1)
list_for_test = remove_duplicates([randint(1, 10) for i in range(10)])
print("Tested list = ", list_for_test)

# Problem Greater than neighbours
print("Number of elements bigger than both neighbours =",
      quantity_of_bigger_than_both_neighbours(list_for_test))

# Problem Swap min and max
max_value_index = list_for_test.index(max(list_for_test))
min_value_index = list_for_test.index(min(list_for_test))

list_for_test[min_value_index], list_for_test[max_value_index] \
    = list_for_test[max_value_index], list_for_test[min_value_index]
print("The same list after swapping max and min value =", list_for_test)
