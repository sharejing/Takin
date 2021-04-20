# -*- encoding: utf-8 -*-
'''
@File   :   text_parsing.py
@Time   :   2021/04/20 17:00:00
@Author :   Jiazuo Qiu
@Email  :   450388261@qq.com
@Desc   :   各种格式的文件读取函数集
'''

import docx

########################################################################
# 读取txt文件
########################################################################
def read_txt(in_path):
    f = open(in_path, "r")

    data = []
    for para in f:
        text = para.strip()
        if len(text) == 0:
            continu
        data.append(text)
    
    return data


########################################################################
# 读取docx文件
########################################################################
def read_docx(in_path):
    f = docx.Document(in_path)

    data = []
    for para in f.paragraphs:
        text = para.text.strip()
        if len(text) == 0:
            continue
        data.append(text)

    return data
