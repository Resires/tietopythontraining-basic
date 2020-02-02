CONFIRMED_PASSWORDS = ['user', 'admin']


def access_required(func):
    def function_wrapper(*args, **kwargs):
        if kwargs['password'] in CONFIRMED_PASSWORDS:
            func(*args, **kwargs)
    return function_wrapper


@access_required
def restricted_print(*args, **kwargs):
    print(*args)


if __name__ == '__main__':
    restricted_print('Message to print from user', password='user')
    restricted_print('Message to print from admin', password='admin')
    restricted_print('Message to print from operator', password='operator')  # should not be printed
