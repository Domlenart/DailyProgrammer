import random


def guess_number(low=0, high=100):
    guess = random.randint(low, high)
    print('Is your number %s' % guess)
    user_input = input('> ')
    if user_input == 'correct':
        pass
    elif user_input == 'higher':
        guess_number(low=guess, high=high)
    elif user_input == 'lower':
        guess_number(low=low, high=guess)
    else:
        print('Incorrect input, accepted commands are: correct, lower, higher.')
        guess_number(low, high)


