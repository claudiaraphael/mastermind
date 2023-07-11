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

# compare the guess
# check the code
def check_code(guess, real_code):
    # check colors in correct position
    # check color in incorrect position
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    # put the guess colors in a tuple so you can compare them to the real color in another tuple. 
    # create tuples with zip function.
    for guess_color, real_color in zip(guess, real_code):