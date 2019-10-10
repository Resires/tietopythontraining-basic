# https://snakify.org/lessons/two_dimensional_lists_arrays/problems/
from random import randint
# Problem Maximum
rows_quantity = 6
columns_quantity = 4
array = [[randint(1, 30) for i in range(columns_quantity)] for j in range(rows_quantity)]
print("Tested array:")
for row in array:
    print(row)
x_index_of_maximum = 0
y_index_of_maximum = 0
maximum = 0
for i in range(rows_quantity):
    for j in range(columns_quantity):
        if array[i][j] > maximum:
            maximum = array[i][j]
            x_index_of_maximum = i
            y_index_of_maximum = j
print('Maximum of this array is {}, '
      'and it is in {} row, {} column'.format(maximum,
                                              x_index_of_maximum,
                                              y_index_of_maximum))


# Problem Swap the columns
def swap_columns(matrix_from_user, i, j):
    for row in matrix_from_user:
        row[i], row[j] = row[j], row[i]
    return matrix_from_user


def print_matrix(matrix_from_user):
    for row in matrix_from_user:
        for element in row:
            print(element, end=' ')
        print()


rows_quantity = 4
columns_quantity = 6
A = [[i * 10 + j for i in range(rows_quantity)] for j in range(columns_quantity)]
print("New task - Replace column. Original matrix:")
print_matrix(A)
print("Replaced:")
print_matrix(swap_columns(A, 1, 3))
# Problem The diagonal parallel to the main
print("New task - Two-dimensional array of size (n×n) \nMain diagonal = 0 . \nDiagonals adjacent to the main = 1 . "
      "\nNext adjacent diagonals write = 2 and so forth.")
n = 5
array = [[abs(i-j) for i in range(n)] for j in range(n)]
print_matrix(array)
