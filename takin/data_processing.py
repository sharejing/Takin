# -*- encoding: utf-8 -*-
'''
@File   :   data_processing.py
@Time   :   2021/04/19 15:09:13
@Author :   ShareJing
@Email  :   yymmjing@gmail.com
@Desc   :   The function set of data processing.
'''

import jieba
import jieba.posseg as pseg
import spacy
import logging
import random
import math

jieba.setLogLevel(logging.INFO)


def tokenize(text: str, lang="en", with_pos=False, drop_stopwords=False) -> list:
    """
    分词，中文分词调用jieba，英文分词调用spacy;
    停用词表从文件中加载，也可自行上传
    """
    if drop_stopwords:
        with open("resources/stopwords.txt", "r", encoding="utf-8") as f:
            stopwords = [line.strip() for line in f]
    else:
        stopwords = []
    
    tokenized_text = []
    if lang == "zh":
        for word, flag in pseg.cut(text):
            if word not in stopwords:
                tokenized_text.append((word, flag))
    if lang == "en":
        nlp = spacy.load("en_core_web_sm")
        for token in nlp(text):
            if token.text not in stopwords:
                tokenized_text.append((token.text, token.pos_))
    if with_pos:
        return tokenized_text
    else:
        return [ele[0] for ele in tokenized_text]
    
    
def split_dataset(corpus: list, ratio: str) -> list:
    """
    给定一个原始数据集，打乱后，按照比例将其划分为训练集、验证集、测试集
    """
    random.shuffle(corpus)
    ratio = [int(ele) for ele in ratio.split(":")]
    length = len(corpus)
    
    # ratio等于3，即将corpus划分为训练集、验证集和测试集
    if len(ratio) == 3:
        index0 = math.ceil(length * ratio[0] / 10)
        index1 = math.ceil(length * ratio[1] / 10)
        index2 = length - index0 - index1
        return corpus[:index0], corpus[index0:index0+index1], corpus[:index2]
    # ratio等于2，即将corpus划分为训练集、测试集
    elif len(ratio) == 2:
        index0 = math.ceil(length * ratio[0] / 10)
        index1 = length - index0
        return corpus[:index0], corpus[:index1]
    else:
        return "ratio设置不合理，ratio=2或3"






