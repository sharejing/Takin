# -*- encoding: utf-8 -*-
'''
@File   :   preprocess.py
@Time   :   2021/04/12 18:28:06
@Author :   ShareJing
@Email  :   yymmjing@gmail.com
@Desc   :   The function set of text preprocess.
'''

import re


def lowercase(text):
    """
    All characters of text are converted into lowercase. 
    """
    return text.lower()


def capitalize(text):
    """
    The first character of text are converted into uppercase.
    """
    return text.capitalize()


def delete_escape_characters(text):
    """
    Delete all escape characters (\r|\n|\t|\f|\v) of text.
    """
    return re.sub("[\r\n\t\f\v]", "", text)


def delete_extra_whitespaces(text):
    """
    Delete any extra white spaces of text.
    """
    return " ".join(text.split())


def delete_digits(text):
    """
    Delete all digits in text.
    """
    return re.sub("[0-9]", "", text)


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
# print(delete_digits(test5)) 