# -*- encoding: utf-8 -*-
'''
@File   :   data_cleaning.py
@Time   :   2021/04/12 18:28:06
@Author :   ShareJing
@Email  :   yymmjing@gmail.com
@Desc   :   文本清洗函数集
'''

import re
from string import punctuation
from itertools import groupby


def delete_escape_character(text, lang="zh"):
    """
    删除文本中的转移字符
    """
    list_text = list(text)
    for index, ele in enumerate(list_text):
        if ele in ["\t", "\v", "\f", "\r"]:
            list_text[index] = ""
        if lang == "zh":
            if ele == "\n" and list_text[index-1] != "。":
                list_text[index] = "。"
            if ele == "\n" and list_text[index-1] == "。":
                list_text[index] = ""
        else:
            if ele == "\n" and list_text[index-1] != ".":
                list_text[index] = ". "
            if ele == "\n" and list_text[index-1] == ".":
                list_text[index] = " "
    return "".join(list_text)


def delete_extra_whitespace(text, lang="zh"):
    """
    删除文本中的多余空白
    """
    if lang == "zh":
        return "".join(text.split())
    else:
        list_text = list(" ".join(text.split()))
        for index, ele in enumerate(list_text):
            if index!= 0 and ele in punctuation:
                if list_text[index-1] == " ":
                    list_text[index-1] = ""
        return "".join(list_text)


def delete_digit(text):
    """
    删除文本中的数字
    """
    return re.sub(r"[0-9]", "", text)


def delete_punctuation(text):
    """
    删除文本中的所有标点符号
    """
    return re.sub(r"[;:,.\"?!'·！？；，。：“”、‘’《》\[\╔\ˊ\〉\〈\–\η\●\®\·\•\-\~#/*&$|★▶><\\^@+[=\]()（）{%_}?…]+]", "", text)


def delete_letter(text):
    """
    删除所有英文字母
    """
    return re.sub(r"[A-Za-z]", "", text)


def delete_chinese(text):
    """
    删除所有中文字符
    """
    return re.sub(r"[\u4e00-\u9fa5]", "", text)


def delete_bracket(text):
    """
    删除括号以及括号里的内容，包括 <*>、(*)、（*）、【*】、[*]、{*}
    """
    text = re.sub(r"<[^<>]*>", "", text)
    text = re.sub(r"\([^()]*\)", "", text)
    text = re.sub(r"\（[^（）]*\）", "", text)
    text = re.sub(r"\【[^【】]*\】", "", text)
    text = re.sub(r"\[[^\[\]]*\]", "", text)
    text = re.sub(r"\{[^{}]*\}", "", text)
    return text


def delete_series_number(text):
    """
    删除文本中的序号
    """
    text = re.sub(r"\d+\.", "", text)
    text = re.sub(r"\d+\。", "", text)
    text = re.sub(r"\(\d+\)[.]?", "", text)
    text = re.sub(r"\（[一|二|三|四|五|六|七|八|九|十|百|千|万|亿]+\）[、]?", "", text)
    text = re.sub(r"\d+\)[.]", "", text)
    text = re.sub(r"\d+\)[、]", "", text)
    text = re.sub(r"\d+\)", "", text)
    return text


def delete_repeated_punc(text):
    """
    连续重复的标点符号只保留一次
    """
    punctuations = [';', ':', ',', '.', '"', '?', '!', "'", '·', '！', '？', '；', '，', '。', '：', '“', '”', '、', '‘', '’', '《', '》', '[', '╔', 'ˊ', '〉', '〈', '–', 'η', '●', '®', '·', '•', '-', '~', '#', '/', '*', '&', '$', '|', '★', '▶', '>', '<', '\\', '^', '@', '+', '[', '=', ']', '(', ')', '（', '）', '{', '%', '_', '}', '?', '…']
    t = [[k, len(list(g))] for k, g in groupby(text)]
    res = ""
    for ele in t:
        char = ele[0]
        count = ele[1]
        if char in punctuations and count > 1:
            count = 1
        res += char * count
    return res