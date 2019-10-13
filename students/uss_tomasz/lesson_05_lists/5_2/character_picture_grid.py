def make_grid_transpose(grid_from_user):
    column_quantity = len(grid_from_user[0])
    return [[row[i] for row in grid_from_user] for i in range(column_quantity)]


def print_grid(user_grid):
    for row in user_grid:
        for character in row:
            print(character, end='')
        print()


if __name__ == '__main__':
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    print("This is initial picture:")
    print_grid(grid)
    print("This is changed picture:")
    print_grid(make_grid_transpose(grid))
