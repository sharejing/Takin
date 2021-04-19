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


jieba.setLogLevel(logging.INFO)


def tokenize(text: str, lang="en", with_pos=False, drop_stopwords=False) -> list:
    """
    分词，中文分词调用jieba，英文分词调用spacy;
    停用词表从文件中加载，也可自行上传
    """
    if drop_stopwords:
        with open("stopwords/stopwords.txt", "r", encoding="utf-8") as f:
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






