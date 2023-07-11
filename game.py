import random

COLORS = ['R','G','B','Y','W', 'O']
TRIES = 10
CODE_LENGTH = 4

# generate a 4 color random code
def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

code = generate_code()

# make the user guess the code
def guess_code():

    while True:
        guess = input('Guess: ').upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f'You must guess {CODE_LENGTH} colors.')
            continue
        for color in guess:
            if color not in COLORS:
                print(f'Invalid color: {color}. Try again.')
                break
            # if all the colors in the guess list are valid, break the while loop
            else:
                break
    return guess

