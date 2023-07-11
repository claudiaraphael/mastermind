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