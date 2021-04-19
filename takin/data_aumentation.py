# -*- encoding: utf-8 -*-
'''
@File   :   data_aumentation.py
@Time   :   2021/04/19 16:19:12
@Author :   Jun Quan, Qian Cao
@Email  :   terryqj0107@gmail.com, caoqian0905@gmail.com
@Desc   :   一些简单的数据增强函数集
'''

import random

#seed = 2021
#random.seed(seed)

def random_swap(sentence, n=1):
    '''
    uasge: Random swap two words in sentence n times
    args: sentence -> str, string split by space
          n -> int, swapped times and default is 1
    return: swapped_sentence -> str
    '''
    swapped_sentence = sentence.strip().split(" ")
    for _ in range(n):
        swapped_sentence = swap_words(swapped_sentence)
    swapped_sentence = " ".join(swapped_sentence)
    return swapped_sentence

def swap_words(sentence):
    '''
    usage: Random swap two words in sentence 1 time
    '''
    if len(sentence) <= 1:
        return sentence
    swap_idx_1 = random.randint(0, len(sentence)-1)
    swap_idx_2 = random.choice([i for i in range(len(sentence)) if i not in [swap_idx_1]])
    sentence[swap_idx_1], sentence[swap_idx_2] = sentence[swap_idx_2], sentence[swap_idx_1]
    return sentence

def random_delete(sentence, ratio=0.1):
    '''
    usage: Random delete words in sentence with ratio
    args: sentence -> str, string split by space
          ratio -> float, delete ratio and default is 0.1
    return: deleted_sentence -> str
    '''
    sentence = sentence.strip().split(" ")
    if len(sentence) == 1:
        return sentence
    deleted_sentence = []
    for i in range(len(sentence)):
        delete_ratio = random.random()
        if delete_ratio > ratio:
            deleted_sentence.append(sentence[i])
    if len(deleted_sentence) == 0:
        random_idx = random.randint(0, len(sentence)-1)
        deleted_sentence.append(sentence[random_idx])
    deleted_sentence = " ".join(deleted_sentence)
    return deleted_sentence


