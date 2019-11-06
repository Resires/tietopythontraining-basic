def print_table(table):
    columns_quantity = len(table)
    rows_quantity = len(table[0])
    column_widths = [0] * columns_quantity
    for column in range(columns_quantity):
        column_widths[column] = len(max(table[column], key=len))
    for row in range(rows_quantity):
        for column in range(columns_quantity):
            print(table[column][row].rjust(column_widths[column]), end=' ')
        print()


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'thisWordIsVeryLongForTestingPurposes', 'goose']]


print_table(table_data)
