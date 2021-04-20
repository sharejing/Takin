# -*- encoding: utf-8 -*-
'''
@File   :   data_aumentation.py
@Time   :   2021/04/19 16:19:12
@Author :   Jun Quan, Qian Cao
@Email  :   terryqj0107@gmail.com, caoqian0905@gmail.com
@Desc   :   一些简单的数据增强函数集
'''

import jieba
import synonyms as syns
import random
from random import shuffle
from nltk.corpus import wordnet 

random.seed(2021)


#停用词列表
f = open('resources/stopwords.txt', encoding="utf-8")
stop_words = list()
for stop_word in f.readlines():
    stop_words.append(stop_word[:-1])
f.close()


########################################################################
# 同义词替换
# 替换一个语句中的n个单词为其同义词
########################################################################
def synonym_replacement(words, n, lang="zh"):
    new_words = words.copy()
    random_word_list = list(set([word for word in words if word not in stop_words]))     
    random.shuffle(random_word_list)
    num_replaced = 0  
    for random_word in random_word_list:          
        synonyms = get_synonyms(random_word, lang)
        if len(synonyms) >= 1:
            synonym = random.choice(synonyms)   
            new_words = [synonym if word == random_word else word for word in new_words]   
            num_replaced += 1
        if num_replaced >= n: 
            break

    sentence = ' '.join(new_words)
    new_words = sentence.split(' ')
    return new_words


def get_synonyms(word, lang):
    if lang == "en":
        synonyms = set()
        for syn in wordnet.synsets(word): 
            for l in syn.lemmas(): 
                synonym = l.name().replace("_", " ").replace("-", " ").lower()
                synonym = "".join([char for char in synonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
                synonyms.add(synonym) 
        if word in synonyms:
            synonyms.remove(word)
        return list(synonyms)
    elif lang == "zh":
        return syns.nearby(word)[0]


########################################################################
# 随机插入
# 随机在语句中插入n个词
########################################################################
def random_insertion(words, n, lang="zh"):
    new_words = words.copy()
    for _ in range(n):
        add_word(new_words, lang)
    return new_words

def add_word(new_words, lang):
    synonyms = []
    counter = 0    
    while len(synonyms) < 1:
        random_word = new_words[random.randint(0, len(new_words)-1)]
        synonyms = get_synonyms(random_word, lang)
        counter += 1
        if counter >= 10:
            return
    random_synonym = random.choice(synonyms)
    random_idx = random.randint(0, len(new_words)-1)
    new_words.insert(random_idx, random_synonym)


########################################################################
# 随机交换
# 交换句子中两个词，随机交换n次
########################################################################

def random_swap(words, n):
    new_words = words.copy()
    for _ in range(n):
        new_words = swap_word(new_words)
    return new_words

def swap_word(new_words):
    random_idx_1 = random.randint(0, len(new_words)-1)
    random_idx_2 = random_idx_1
    counter = 0
    while random_idx_2 == random_idx_1:
        random_idx_2 = random.randint(0, len(new_words)-1)
        counter += 1
        if counter > 3:
            return new_words
    new_words[random_idx_1], new_words[random_idx_2] = new_words[random_idx_2], new_words[random_idx_1] 
    return new_words

########################################################################
# 随机删除
# 以概率p删除语句中的词
########################################################################
def random_deletion(words, p):

    if len(words) == 1:
        return words

    new_words = []
    for word in words:
        r = random.uniform(0, 1)
        if r > p:
            new_words.append(word)

    if len(new_words) == 0:
        rand_int = random.randint(0, len(words)-1)
        return [words[rand_int]]

    return new_words


########################################################################
# 丢弃停用词
########################################################################
def drop_stopwords(words):
    filtered_sentence = []  # 过滤后的句子
    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence
