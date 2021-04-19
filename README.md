<div align="center"><img src="https://github.com/sharejing/Takin/blob/main/images/takin_logo.PNG" height="150px"/></div>

<h2 align="center">Takin: A Simple Python Toolkit for Text Parsing, Cleaning and Statistics</h2>

实验室数据大多由人工众包构建而成，其格式规范，内容干净，数据经过一些简单清洗便能用于模型训练；而真实环境下的数据往往来自于一些用户日志、员工记录等，其文件格式众多，数据内容包含大量噪声，想要获得内容干净、格式规范统一的数据，就需要对这些数据进行深度清洗。Takin就是一款用于真实环境下数据的解析、深度清洗、统计的Python工具，它集成了一些优秀的开源插件（如spacy、jieba），通过对外提供函数接口的方式，来帮助使用者解析数据、清洗数据、统计数据等。

<b>Takin的目标是：对于任何形式、任何内容的数据，通过Takin就能完全得到你所期望的最规范、最干净的数据。</b>

为了达到这个目标，Takin包含以下功能：
* 文本解析：从多种文件格式 (如pdf、pptx、msg、html等)中解析文本；
* 数据清洗：提供多个清洗函数接口（如删除数字、序号、标点、特殊字符等）；
* 数据处理：包括分词、词性标注、数据划分等；
* 数据分析：统计文本、句子长度，词数、句子数等；
* 数据增强：提供一些简单的数据增强方法，如近义词替换、随机交换、删除单词、释义生成；
* 简单任务：提供一些简单的NLP任务，如关键词抽取、色情文本判断、命名实体识别，情感分析等；

# Usage
```python
import takin

# 删除转义字符
test3 = "tbubs\t nkkj\rndsnd  sjdsn  \t\t \r \t\f\n"
print(takin.delete_escape_character(test3))

# 删除多余的空格
test4 = "I lovw        python   d     "
print(takin.delete_extra_whitespace(test4))

# 删除数字
test5 = "jjj 555 5  555   jkdn33 78 0 6 7"
print(takin.delete_digit(test5)) 

# 删除标点符号
test6 = "hh.,?？。，《hshhh》dddi;';'；‘，。、’‘“”"
print(takin.delete_punctuation(test6))

# 删除括号及括号里的内容
test7 = "dd<dd>d[e]dd【33445可爱】dd{众多}（就就很尴尬）jjj(尅啊)"
print(takin.delete_bracket(test7))

# 删除序号
test8 = "1. 亨 2.hhjsidh (66).jasckjs   2.34    (9999).周驰你上课 1).2)."
print(takin.delete_extra_whitespace(takin.delete_series_number(test8)))

```

# To-do list
### 文本抽取
- [ ] 从html、pdf、word、msg、ppt、excel中提取文本
- [ ] 删除所有该格式的专属标签 (如删除html文本中的html标签)

### 文本清洗
- 转化类
- [x] 大小写转化
- [x] 首字母大写
- [ ] 简繁体转化
- [ ] 全半角转化
- [ ] 词干还原
- [ ] 文本去重
- [ ] 单词拼写纠错
- 删除类
- [x] 删除所有标点符号
- [x] 删除多余空白格
- [x] 删除所有转义字符
- [x] 删除所有数字
- [x] 删除所有括号([]、{}、())及里面的内容
- [x] 删除序号数字 (1.或(1).)
- [x] 删除一些特殊字符 (-~#/*&$|★▶><\\^@)
- [x] 删除中文文本里的英文字符
- [x] 删除英文文本里的中文字符 
- 处理类
- [ ] 分句/分段
- [ ] 词频统计(词云)
- [ ] 字数统计/句数统计/段数统计
- [ ] 数据划分
- [ ] 词向量转化
- [ ] BPE

### 简单任务
- [ ] 色情文本判断、识别
- [ ] 情感分析
- [ ] 关键词提取
- [ ] 命名实体识别
- [ ] 摘要生成
- [ ] 事件抽取
