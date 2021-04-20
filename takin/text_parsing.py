# -*- encoding: utf-8 -*-
'''
@File   :   text_parsing.py
@Time   :   2021/04/20 17:00:00
@Author :   Jiazuo Qiu
@Email  :   450388261@qq.com
@Desc   :   各种格式的文件读取函数集 (txt/docx/ html/pdf/msg/ppt/excel)
'''

import docx
from bs4 import BeautifulSoup
from pptx import Presentation
from pptx.util import Cm, Pt

########################################################################
# 读取txt文件
########################################################################
def read_txt(in_path):
    data = []

    f = open(in_path, 'r', encoding='utf-8')
    for para in f:
        text = para.strip()
        if len(text) == 0:
            continue
        data.append(text)
    
    return data


########################################################################
# 读取docx文件
########################################################################
def read_docx(in_path):
    data = []

    f = docx.Document(in_path, encoding='utf-8')
    for para in f.paragraphs:
        text = para.text.strip()
        if len(text) == 0:
            continue
        data.append(text)

    return data


########################################################################
# 读取ppt文件
########################################################################
def read_ppt(in_path):
    data = []

    prs = Presentation(in_path)
    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                text_frame = shape.text_frame
                for paragraph in text_frame.paragraphs:
                    data.append(paragraph.text)

    return data

