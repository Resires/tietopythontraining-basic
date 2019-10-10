from random import randint
pins_quantity = 10
balls_quantity = 5
pins = ['I']*pins_quantity


def throw_ball():
    """Returns randomly positions range. Between them pins will be removed from bowling alley.
    First value is always smaller than a second value
    """
    a, b = randint(1, 10), randint(1, 10)
    return min(a, b), max(a, b)


print("Initial pins in the bowling alley =", pins)
for i in range(balls_quantity):
    start_position, stop_position = throw_ball()
    if start_position == stop_position:
        print("Your ball hit pin from", start_position, 'position!')
    else:
        print("Your ball hit pins from", start_position, "up to", stop_position, "position!")
    pins = pins[:start_position-1] + ['.']*(stop_position-start_position+1) + pins[stop_position:]
    print("Pins remained: ", pins)
    if pins == ['.'] * 10:
        print("You won!")
        break
