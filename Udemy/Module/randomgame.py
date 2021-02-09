import sys
from random import randint
# generate a number 1-10
answer = randint(1, 10)
# for terminal use
# answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# input from user

# check that input is a number 1~10
while True:
    try:
        guess = int(input('guess a number 1~10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('You\'re a genius')
                break

    except ValueError:
        print('Please enter a number')
        continue


# check if number is the right guess. Otherwise ask again