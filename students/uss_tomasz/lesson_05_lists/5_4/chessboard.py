# Problem Chess board
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end='')
        print()


def sign(a, b):
    """Character sign is changing each time row or column increase by one.
    There are two available characters: '.' and '
    """
    if (a + b) % 2 == 0:
        return '.'
    else:
        return '*'


def create_chessboard(rows_quantity, columns_quantity):
    return [[sign(i, j) for j in range(columns_quantity)] for i in range(rows_quantity)]


if __name__ == '__main__':
    chessboard = create_chessboard(5, 7)
    print_matrix(chessboard)
