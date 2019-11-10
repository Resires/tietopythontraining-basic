def print_table(table):
    columns_quantity = len(table)
    rows_quantity = len(table[0])
    column_widths = [len(max(column, key=len)) for column in table]
    for row in range(rows_quantity):
        for column in range(columns_quantity):
            print(table[column][row].rjust(column_widths[column]), end=' ')
        print()


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'thisWordIsVeryLongForTestingPurposes', 'goose']]


print_table(table_data)
