from random import randint
PINS_QUANTITY = 10
BALLS_QUANTITY = 5
PINS_ALL_DOWN = ['.'] * 10
pins = ['I']*PINS_QUANTITY


def throw_ball():
    """Returns randomly positions range. Between them pins will be removed from bowling alley.
    First value is always smaller than a second value
    """
    a = randint(1, 10)
    b = randint(1, 10)
    return min(a, b), max(a, b)


print("Initial pins in the bowling alley =", pins)
for i in range(BALLS_QUANTITY):
    start_position, stop_position = throw_ball()
    if start_position == stop_position:
        print("Your ball hit pin from", start_position, 'position!')
    else:
        print("Your ball hit pins from", start_position, "up to", stop_position, "position!")
    pins = pins[:start_position-1] + ['.']*(stop_position-start_position+1) + pins[stop_position:]
    print("Pins remained: ", pins)
    if pins == PINS_ALL_DOWN:
        print("You won!")
        break
