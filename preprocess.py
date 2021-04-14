# -*- encoding: utf-8 -*-
'''
@File   :   preprocess.py
@Time   :   2021/04/12 18:28:06
@Author :   ShareJing
@Email  :   yymmjing@gmail.com
@Desc   :   The function set of text preprocess.
'''

import re


def lowercase(text: str) -> str:
    """
    All characters of text are converted into lowercase. 
    """
    return text.lower()


def capitalize(text: str) -> str:
    """
    The first character of text are converted into uppercase.
    """
    return text.capitalize()


def delete_escape_character(text: str) -> str:
    """
    Delete all escape characters (\r|\n|\t|\f|\v) of text.
    """
    return re.sub(r"[\r\n\t\f\v\\n]", "", text)


def delete_extra_whitespace(text: str) -> str:
    """
    Delete any extra white spaces of text.
    """
    return " ".join(text.split())


def delete_digit(text: str) -> str:
    """
    Delete all digits in text.
    """
    return re.sub(r"[0-9]", "", text)


def delete_punctuation(text: str) -> str:
    """
    Delete all punctuation in text.
    """
    return re.sub(r"[;:,.\"?!'·！？；，。：“”、‘’《》]", "", text)


def delete_special_character(text: str) -> str:
    """
    Delete special characters in text.
    """
    return re.sub(r"[-~#/*&$|★▶><\\^@+[=\](){%_}]+", "", text)


def delete_bracket(text: str) -> str:
    """
    Delete the content in the brackets and the brackets themselves.
    Including <*>、(*)、（*）、【*】、[*]、{*}
    """
    text = re.sub(r"<[^<>]*>", "", text)
    text = re.sub(r"\([^()]*\)", "", text)
    text = re.sub(r"\（[^（）]*\）", "", text)
    text = re.sub(r"\【[^【】]*\】", "", text)
    text = re.sub(r"\[[^\[\]]*\]", "", text)
    text = re.sub(r"\{[^{}]*\}", "", text)
    return text


def delete_number(text: str) -> str:
    """
    Delete all serial numbers in text.
    Including *.、(*).、*).
    """
    text = re.sub(r"\d+\.[^\d+]", "", text)
    text = re.sub(r"\(\d+\).", "", text)
    text = re.sub(r"\d+\).", "", text)
    text = re.sub(r"\d+\)、", "", text)
    return text


#=============================================
# Testing
#=============================================

# test1 = "jjjAA kk HHGhhGG"
# print(lowercase(test1))

# test2 = "this is my apple."
# print(capitalize(test2))

# test3 = "tbubs\t nkkj\rndsnd  sjdsn  \t\t \r \t\f\n"
# print(delete_escape_character(test3))

# test4 = "I lovw        python   d     "
# print(delete_extra_whitespace(test4))

# test5 = "jjj 555 5  555   jkdn33 78 0 6 7"
# print(delete_digit(test5)) 

# test6 = "hh.,?？。，《hshhh》dddi;';'；‘，。、’‘“”"
# print(delete_punctuation(test6))

# test7 = "dd<dd>d[e]dd【33445可爱】dd{众多}（就就很尴尬）jjj(尅啊)"
# print(delete_bracket(test7))

# test8 = "1. 亨 2.hhjsidh (66).jasckjs   2.34    (9999).周星驰你上课 1).2)."
# print(delete_extra_whitespace(delete_number(test8)))

# test9 = "\\n \\n------------ \\n\\n*&++++==--_<>%%%%%%%%abc"
# test10 = delete_escape_character(test9)
# print(test10)
# print(delete_special_character(test10))