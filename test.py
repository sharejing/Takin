# -*- encoding: utf-8 -*-
'''
@File   :   test.py
@Time   :   2021/07/5 16:47:49
@Author :   ShareJing
@Email  :   yymmjing@gmail.com
@Desc   :   测试每一个模块
'''

import takin


"""
测试数据清洗函数
"""
# print(takin.delete_escape_character("Today is sunday.\nwe are \thappy.", lang="en"))
# print(takin.delete_extra_whitespace("我 们  都非   常快 乐   。 ", lang="zh"))
# print(takin.delete_extra_whitespace("Takin  ,    is very   useful  .    ", lang="en"))
# print(takin.delete_digit("今天6天777气7908762345不错！"))
# print(takin.delete_punctuation("Long;:,.\"??!''·！？；，。：“”、‘’《》[╔ˊ〉〈–η●®·•-~#/*&$|★▶><\^@+[=]()（）{%_}?…]"))
# print(takin.delete_letter("明天将会是一个beautiful晴朗的天气"))
# print(takin.delete_chinese("This is another 胜利victory!"))
# print(takin.delete_bracket("机器阅读理解（MRC），【旨在】教机器理解人类语言(language){热爱学习}[hah]"))
# print(takin.delete_series_number("1.努力工作；(2).用心学习；(3)锻炼身体；4).热爱家庭 5。快乐；6)学习, 7)、（一）、集中学习 （十五）高度集中 （一百二十三）"))
# print(takin.delete_repeated_punc("what's up????????????????...。。《《《"))


"""
测试数据切分函数
"""
# corpus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# train, dev, test = takin.split_dataset(corpus, "7:2:1", is_shuffe=False)
# print(len(train), train)
# print(len(dev), dev)
# print(len(test), test)

# data = []

# with open("./data/train.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         ele = line.strip().split("\t")
#         data.append({"text": ele[1], "label": ele[0]})

# with open("./data/test.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         ele = line.strip().split("\t")
#         data.append({"text": ele[1], "label": ele[0]})

# print(len(data))

# train, dev, test = takin.split_dataset_by_class(data, "7:2:1", cate="label", is_shuffle=True)
# print(len(train))
# print(len(dev))
# print(len(test))

# print(test[-5:])


"""
测试数据解析函数
"""
# print(takin.read_txt("./resources/parsing_examples/test.txt"))
# print(takin.read_docx("./resources/parsing_examples/test.docx"))
# print(takin.read_pptx("./resources/parsing_examples/test.pptx"))
# print(takin.read_pdf("./resources/parsing_examples/test.pdf"))
# print(takin.read_html("./resources/parsing_examples/test.html"))
# print(takin.read_eml("./resources/parsing_examples/test.eml"))