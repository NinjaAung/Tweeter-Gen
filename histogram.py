import os
import random

test = "one fish two fish red fish blue fish"

def histogram(source_text):
    token = 0
    dic = {}
    words = source_text
    if os.path.isfile(words):
        with open(f'{words}', 'r+') as f:
            words = f.read()
    
    for word in words.split():
        token += 1
        dic[word] = dic.get(word, 0) + 1
    return dic, token 

def unique_words(histogram):
    return len(histogram)
    

def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return False

def random_frequency_choice(source_text):
    dic,token = histogram(source_text)
    dart = random.randint(0, token)
    num = 0

    for key, value in dic.items():
        num += value
        if  dart <= num :
            return key         

def test_dic(histogram):
    test_dic = {}
    for _ in range(10000):
        word = random_frequency_choice(histogram)
        test_dic[word] = test_dic.get(word, 0) + 1
    return print(test_dic)

test_dic(test)






