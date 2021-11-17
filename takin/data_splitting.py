# -*- encoding: utf-8 -*-
'''
@File   :   data_processing.py
@Time   :   2021/07/05 18:14:52
@Author :   Yimin Jing
@Email  :   yymmjing@gmail.com
@Desc   :   划分数据集
'''

import random
import math
    
    
def split_dataset(corpus: list, ratio: str, is_shuffle=True) -> list:
    """
    给定一个原始数据集，按照比例将其划分为训练集、验证集、测试集
    """
    if is_shuffle:
        random.shuffle(corpus)
    ratio = [int(ele) for ele in ratio.split(":")]
    assert sum(ratio) == 10, "ratio必须按10来划分，7:2:1或者6:4"
    length = len(corpus)
    
    # ratio等于3，即将corpus划分为训练集、验证集和测试集
    if len(ratio) == 3:
        index0 = math.ceil(length * ratio[0] / 10)
        index1 = math.ceil(length * ratio[1] / 10)
        index2 = length - index0 - index1
        return corpus[:index0], corpus[index0:index0+index1], corpus[-index2:]
    # ratio等于2，即将corpus划分为训练集、测试集
    elif len(ratio) == 2:
        index0 = math.ceil(length * ratio[0] / 10)
        index1 = length - index0
        return corpus[:index0], corpus[-index1:]
    else:
        raise Exception("ratio设置不合理，ratio=2或3")


def split_dataset_by_class(corpus: list, ratio: str, cate="category", is_shuffle=True) -> list:
    """
    corpus中每个元素是dict，按照类别进行数据切分
    """
    _ratio = [int(ele) for ele in ratio.split(":")]
    assert sum(_ratio) == 10, "ratio必须按10来划分，7:2:1或者6:4"

    cate_corpus = {}
    for sample in corpus:
        category = sample[cate]
        if category not in cate_corpus:
            cate_corpus[category] = []
            cate_corpus[category].append(sample)
        else:
            cate_corpus[category].append(sample)
    
    train_data = []
    dev_data = []
    test_data = []
    if len(_ratio) == 3:
        for key, value in cate_corpus.items():
            assert len(value) >= 10, "{}类别样例数仅为：{}".format(key, len(value)) 
            print("{}类别的数据样例为：{}".format(key, len(value)))
            train, dev, test = split_dataset(value, ratio, is_shuffle=False)
            train_data.extend(train)
            dev_data.extend(dev)
            test_data.extend(test)
        if is_shuffle:
            random.shuffle(train_data)
            random.shuffle(dev_data)
            random.shuffle(test_data)
        return train_data, dev_data, test_data
    elif len(_ratio) == 2:
        for key, value in cate_corpus.items():
            print("{}类别的数据样例为：{}".format(key, len(value)))
            train, test = split_dataset(value, ratio, is_shuffle=False)
            train_data.extend(train)
            test_data.extend(test)
        if is_shuffle:
            random.shuffle(train_data)
            random.shuffle(test_data)
        return train_data, test_data
    else:
        raise Exception("ratio设置不合理，ratio=2或3")


    


