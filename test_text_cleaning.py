# -*- encoding: utf-8 -*-
"""
@File    :   test_text_cleaning.py
@Time    :   2022/02/17 18:02:31
@Author  :   Yimin Jing
@Contact :   jingym3@lenovo.com
@Desc    :   测试文本清洗函数
"""

import takin

# zh_text = "中国是一个美丽的地方\n请告诉我你在哪儿。\n我一定会去找你\t在我的怀里\t在你的眼里"
# en_text = "Today is sunday\nwe are happy\nwe are fun."
# print(takin.delete_escape_character(zh_text, lang="zh", add_punc=False))
# print(takin.delete_escape_character(zh_text, lang="zh", add_punc=True))
# print(takin.delete_escape_character(en_text, lang="en", add_punc=False))
# print(takin.delete_escape_character(en_text, lang="en", add_punc=True))

# zh_text = "我 们  都非   常快 乐   。 "
# en_text = "Takin  ,    is very   useful  .    "
# print(takin.delete_extra_whitespace(zh_text, lang="zh"))
# print(takin.delete_extra_whitespace(en_text, lang="en"))

# text = "980.152%的人都没有来，1/120的孩子失去了饮水，20.34块蛋糕，100个人，97%的老人"
# print(takin.delete_digit(text))

# text = "今天的MoonCake真的非常nice啊！"
# print(takin.delete_letter(text))

# text = "This is another 胜利victory!"
# print(takin.delete_chinese(text))

# text = "机器阅读理解（MRC），【【旨在】】教机器理解人类语言(language){热爱学习}[hah]<<hahgag>>"
# print(takin.delete_bracket(text))

# text = "1.努力工作；2. 用心学习 (2).用心学习；(3)锻炼身体；4).热爱家庭快乐；6)学习, 7)、（一）、集中学习 （十五）高度集中 （一百二十三）"
# print(takin.delete_series_number(text))

# text = "what's up????????????????...。。《《《"
# print(takin.delete_repeated_punc(text))

# text1 = "Long;:,.\"??!''·！？；，。：“”、‘’《》[╔ˊ〉〈–η●®·•-~#/*&$|★▶><\^@+[=]()（）{%_}?…]"
# text2 = "this day is a friday. We are 3.123, 90%....   3. 中国, 3/2=5, 我峨%嵋你+"
# print(takin.delete_punctuation(text1))
# print(takin.delete_punctuation(text2))

