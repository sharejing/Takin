# -*- encoding: utf-8 -*-
'''
@File   :   test.py
@Time   :   2021/04/15 16:47:49
@Author :   ShareJing
@Email  :   yymmjing@gmail.com
@Desc   :   Test each function
'''

import takin


#=============================================
# Testing
#=============================================

test1 = "jjjAA kk HHGhhGG"
print(takin.lowercase(test1))

test2 = "this is my apple."
print(takin.capitalize(test2))

test3 = "tbubs\t nkkj\rndsnd  sjdsn  \t\t \r \t\f\n"
print(takin.delete_escape_character(test3))

test4 = "I lovw        python   d     "
print(takin.delete_extra_whitespace(test4))

test5 = "jjj 555 5  555   jkdn33 78 0 6 7"
print(takin.delete_digit(test5)) 

test6 = "hh.,?？。，《hshhh》dddi;';'；‘，。、’‘“”"
print(takin.delete_punctuation(test6))

test7 = "dd<dd>d[e]dd【33445可爱】dd{众多}（就就很尴尬）jjj(尅啊)"
print(takin.delete_bracket(test7))

test8 = "1. 亨 2.hhjsidh (66).jasckjs   2.34    (9999).周星驰你上课 1).2)."
print(takin.delete_extra_whitespace(takin.delete_series_number(test8)))

test9 = "今天天气不错，大家都很开心啊，我的马儿在哪里啊!美丽的花儿"
test10 = "Today is sunday, everyone is very happy!"
print(takin.tokenize(test9, lang="zh", with_pos=False, drop_stopwords=True))
print(takin.tokenize(test10, lang="en", with_pos=False, drop_stopwords=True))

corpus = ["A"] * 766
train_dataset, test_dataset = takin.split_dataset(corpus, ratio="8:2")
print(len(train_dataset))
print(len(test_dataset))

idf = takin.get_idf(corpus)
sentence = "社会工程的基础是定量测量.定量测量技术的要点包括测量原理、测量对象、测量公式、测量单位、测量频率等.测量对象一是社会成员,二是社会活动.测量原理是通过测算凝聚在人际交往中的社会能量(测量单位),在数量层面定义社会成员和社会活动的社会作用,从而形成了测量两者的具体公式.测量单位包括直接能量和间接能量的区别.测量技术在社会工程中有广泛的应用,可应用于高能控制工程、低能控制工程和定向控制工程."
tokenized_sent = takin.tokenize(sentence, lang="zh", drop_stopwords=True)
golden_truth = ["定量测量", "能量强度", "社会工程"]
print(takin.extraction_with_tfidf(idf, tokenized_sent, topk=5))


# data argumentation 测试用例
case1 = "我们就像蒲公英，我也祈祷着能和你飞去同一片土地"
# case2 = "I am looking for a restaurant that is moderately priced and serves Cantonese food ."
case1_words = takin.tokenize(case1, lang="zh")
# case2_words = takin.tokenize(case2, lang="en")
p = 0.3
n = max(1, int(p*len(case1_words)))
print(takin.synonym_replacement(case1_words, n, lang="zh"))  # 同义词替换
print(takin.random_insertion(case1_words, n, lang="zh"))  # 随机插入
print(takin.random_swap(case1_words, n))  # 随机交换
print(takin.random_deletion(case1_words, 0.3))  # 随机删除
print(takin.drop_stopwords(case1_words))  # 随机删除