# -*- encoding: utf-8 -*-
'''
@File   :   nlp_task.py
@Time   :   2021/04/19 18:34:25
@Author :   ShareJing
@Email  :   yymmjing@gmail.com
@Desc   :   一些简单的nlp任务
'''

import math
from tqdm import tqdm


#======================================================================
# 基于tf-idf的无监督关键词抽取
#======================================================================

def get_idf(corpus: list) -> dict:
    """
    给定语料库，计算单词的逆文档频率
    corpus: [["A", "B", "C"], ["A", "F"], ["D", "E"], ......]
    """
    df, idf = {}, {}
    N = len(corpus)

    for doc in tqdm(corpus):
        for x in set(doc):
            df[x] = df.get(x, 0) + 1
    for key, value in df.items():
        idf[key] = math.log(N / value, 2)
    return idf


def extraction_with_tfidf(idf: dict, sentence: list, topk: int) -> list:
    """
    基于tf-idf抽取关键词
    """
    tf = {}
    mean_idf = sum(idf.values()) / len(idf)
    tf_idf = {}

    for x in sentence:
        tf[x] = tf.get(x, 0) + 1
    for key in tf:
        """
        计算sentence中每一个单词的tf-idf值，这里有多种计算方法
        wtf-idf: (1+log(tf)) * log(N/df), 对数以2维底
        ntf-pidf: (0.5+(0.5*tf)/max(tf.values())) * max(0, log((N-df)/df))
        Ltf-idf: ((1+log(tf))/(1+log(sum(tf.values())/len(tf)))) * log(N/df)
        vtf-idf: (tf/sum(tf.values())) * log(N/df)
        """
        tf_idf[key] = (1 + math.log(tf[key], 2)) * idf.get(key, mean_idf)
    
    # 对字典按value值降序排列，输出topk个关键词
    sorted_words = sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:topk]