import sys
import random

def rearange(*argv):
    word_list = list(argv)
    x=0
    while x < 4:
        x += 1
        random_word = random.choice(word_list)
        print(random_word)
        word_list.remove(random_word)
        



if __name__ == '__main__':
    rearange(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    pass