# -*- encoding: utf-8 -*-
"""
@File    :   test_data_splitting.py
@Time    :   2022/02/21 18:15:55
@Author  :   Yimin Jing
@Contact :   jingym3@lenovo.com
@Desc    :   测试数据切分函数
"""

import takin

# corpus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# train, dev, test = takin.split_dataset(corpus, "7:2:1", is_shuffle=False)
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