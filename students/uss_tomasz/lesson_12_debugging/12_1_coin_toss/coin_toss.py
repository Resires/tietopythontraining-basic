import logging
import random
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
numeric_toss = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.log(logging.INFO, "Generated value:")
logging.log(logging.INFO, numeric_toss)
toss_conversion = {0: 'tails', 1: 'heads'}
toss = toss_conversion[numeric_toss]
logging.log(logging.INFO, "Which is:")
logging.log(logging.INFO, toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
