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


def delete_escape_character(text, lang="zh", add_punc=False):
    """
    @Desc: 删除文本中的转移字符
    @Args: 
        text: 指定文本
        lang: 该文本对应的语言
        add_punc: 是否补全标点符号
    @Returns: 
        删除后的文本
    """
    list_text = list(text)
    for idx, char in enumerate(list_text):
        if char in ["\t", "\v", "\f", "\r", "\n"]:
            list_text[idx] = ""
            if add_punc:
                if lang == "zh":
                    if list_text[idx-1] != "。":
                        list_text[idx] = "。"
                else:
                    if list_text[idx-1] != ".":
                        list_text[idx] = ". "
    return "".join(list_text)


def delete_extra_whitespace(text, lang="zh"):
    """
    @Desc: 删除文本中的多余空白
    @Args:
        text: 指定文本
        lang: 该文本对应的语言
    @Returns:
        删除后的文本
    """
    if lang == "zh":
        return "".join(text.split())
    else:
        list_text = list(" ".join(text.split()))
        for index, ele in enumerate(list_text):
            if index != 0 and ele in punctuation:
                if list_text[index-1] == " ":
                    list_text[index-1] = ""
        return "".join(list_text)


def delete_digit(text):
    """
    @Desc: 删除文本中的数字 (百分数、分数、小数、整数)
    @Args:
        text: 指定文本
    @Returns:
        删除后的文本
    """
    # 百分数、分数、小数、整数
    DIGIT_PATTERN = r"\d+\.?\d+?%(?#百分数)|\d/\d+(?#分数)|-?\d+\.?\d+(?#小数和整数)"
    return re.sub(DIGIT_PATTERN, "", text)


def delete_punctuation(text):
    """
    @Desc: 删除文本中的所有标点符号 (运算符保留)
    @Args: None
    @Returns: None
    """
    CHINESE_PUNC = r"(，|。|、|？|！|“|”|‘|’|；|：|《|》|￥|（|）|〈|〉|·)"
    ENGLISH_PUNC = r"(,|!|\?|'|\"|…|-|\$|@|\[|\]|{|}|_|\^|#|<|>|\(|\)|&|\\|;|:)"
    SPECIAL_PUNC = r"(╔|ˊ|η|●|®|•|~|★|\||▶|–)"
    OPERATION_PATTERN = r"(?<!\d)(\.|\+|\=|\*|/|%)(?!\d)"

    text = re.sub(CHINESE_PUNC, "", text)
    text = re.sub(ENGLISH_PUNC, "", text)
    text = re.sub(SPECIAL_PUNC, "", text)
    text = re.sub(OPERATION_PATTERN, "", text)
    return text


def delete_letter(text):
    """
    @Desc: 删除所有英文字母
    @Args:
        text: 指定文本
    @Returns:
        删除后的文本
    """
    LETTER_PATTERN = r"[A-Za-z]+"
    return re.sub(LETTER_PATTERN, "", text)


def delete_chinese(text):
    """
    @Desc: 删除所有中文字符
    @Args:
        text: 指定文本
    @Returns:
        删除后的文本
    """
    CHINESE_PATTERN = r"[\u4e00-\u9fa5]+"
    return re.sub(CHINESE_PATTERN, "", text)


def delete_bracket(text):
    """
    @Desc: 删除括号以及括号里的内容，包括 <*>、(*)、（*）、【*】、[*]、{*}
    @Args:
        text: 指定文本
    @Returns:
        删除后的文本
    """
    BRACKET_PATTERN = r"<.*>|\(.*\)|（.*）|【.*】|\[.*\]|{.*}"
    return re.sub(BRACKET_PATTERN, "", text)


def delete_series_number(text):
    """
    @Desc: 删除文本中的序号
    @Args:
        text: 指定文本
    @Returns:
        删除后的文本
    """ 
    # 1.|(2)|(2).|4)|4)、|（一）|（二）、 
    SERIES_PATTERN = r"\d+\.|\(\d+\)\.?|\d+\)(\.|、)?|（(一|二|三|四|五|六|七|八|九|十|百|千|万|亿)+）(\.|、)?"
    return re.sub(SERIES_PATTERN, "", text)


def delete_repeated_punc(text):
    """
    @Desc: 连续重复的标点符号只保留一次
    @Args:
        text: 指定文本
    @Returns:
        删除后的文本
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