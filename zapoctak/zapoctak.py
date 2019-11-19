import random


def napis_zapoctak(jazyk='python', zajimavost=0):
    return ''.join((random.choice(jazyk) for _ in range(zajimavost)))
