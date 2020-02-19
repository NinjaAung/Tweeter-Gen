import random


with open('words.txt','r+') as f:
    read_data = f.read()

x = ""


def random_words(num):
    x = ""
    for i in range(num):
        x += f'{random.choice(read_data.split())} '
    return x

