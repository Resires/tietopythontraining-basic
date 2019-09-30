def distance(x1, y1, x2, y2):
    return ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5


if __name__ == '__main__':
    first_point_x = int(input("First point, x coordinate = "))
    first_point_y = int(input("First point, y coordinate = "))
    second_point_x = int(input("Second point, x coordinate = "))
    second_point_y = int(input("Second point, y coordinate = "))
    format_args = [
        first_point_x,
        first_point_y,
        second_point_x,
        second_point_y,
        distance(first_point_x,
                 first_point_y,
                 second_point_x,
                 second_point_y)
    ]
    print("Distance between ({},{}) and ({},{}) equals {}".format(*format_args))
