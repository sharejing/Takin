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

