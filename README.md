<div align="center"><img src="https://github.com/sharejing/Takin/blob/main/images/takin_logo.PNG" height="150px"/></div>

<h2 align="center">Takin: A Simple Python Toolkit for Text Parsing, Cleaning and Statistics</h2>

实验室数据大多由人工众包构建而成，其格式规范，内容干净，数据经过一些简单清洗便能用于模型训练；而真实环境下的数据往往来自于一些用户日志、员工记录等，其文件格式众多，数据内容包含大量噪声，想要获得内容干净、格式规范统一的数据，就需要对这些数据进行深度清洗。Takin就是一款用于真实环境下数据的解析、深度清洗、统计的开源工具，它集成了一些优秀的开源插件（如spacy、jieba），并通过对外提供函数接口的方式，来帮助使用者解析数据、清洗数据、统计数据等。

🚩<b>Takin的目标是：对于任何形式、任何内容的数据，通过Takin就能完全得到你所期望的最规范、最干净的数据。</b>

为了接近并最终达到这个目标，Takin包含以下功能：
* 文本解析：从多种文件格式 (如pdf、pptx、msg、html等)中解析文本；
* 数据清洗：提供多个清洗函数接口（如删除数字、序号、标点、特殊字符等）；
* 数据处理：包括分词、词性标注、数据划分等；
* 数据分析：统计文本、句子长度，词数、句子数等；
* 数据增强：提供一些简单的数据增强方法，如近义词替换、随机交换、删除单词、释义生成；
* 简单任务：提供一些简单的NLP任务，如关键词抽取、色情文本判断、命名实体识别，情感分析等。

<h2 align="center">Installation</h2>
<h3>1. 直接使用源码 (推荐方式)</h3>

```bash
git clone https://github.com/sharejing/Takin.git
cd Takin
sh setup.sh
```

> ☝️我们推荐直接使用源码来安装Takin，即<b>将stopwords和takin文件夹放入您的project下即可</b>。之所以推荐这种方式的目的是：不同数据一般预处理方式存在差异，直接使用源码可以帮助您根据您的实际情况来修改Takin中的函数，以达到自己的预处理结果。另外，如果您的函数具有很强的代表性，也请您可以pull request，便于大家查阅、使用。

<h3>2. 通过pip安装</h3>

```bash
pip install takin
```

> 😢目前Takin整体还处于初期开发阶段，未来我们会提供这种安装方式。

<h2 align="center">Usage Examples</h2>
<h3>1. 数据清洗 (Data Cleaning)</h3>

```python
import takin

# 删除多余的空格
>>> en_text1 = "I      love  python!"
>>> zh_text1 = "今天    天气  颇为   凉爽  呀 ！"
>>> print(takin.delete_extra_whitespace(en_text1, lang="en"))
>>> print(takin.delete_extra_whitespace(zh_text1, lang="zh"))
I love python!
今天天气颇为凉爽呀！

# 删除括号及括号里的内容
>>> text2 = "我们(很高兴)，他们【很快乐】，大家{都很不错哦 }，所以（今天）一起去玩吧"
>>> print(takin.delete_bracket(text2))
我们，他们，大家，所以一起去玩吧

# 删除序号
>>> test3 = "1. 内存 25.Main board (66).磁盘(9999).显卡 1).M集群2).显示器"
>>> print(takin.delete_series_number(test3))
 内存 Main board 磁盘显卡 M集群显示器
```

<h3>2. 数据处理 (Data Processing)</h3>

```python
import takin

# 分词与词性标注
>>> zh_test4 = "昨天天气不错，大家都很开心啊，我的马儿在哪里啊!美丽的花儿"
>>> en_test4 = "Today is sunday, everyone is very happy!"
>>> print(takin.tokenize(zh_test4, lang="zh", with_pos=True, drop_stopwords=True))
>>> print(takin.tokenize(en_test4, lang="en", with_pos=False, drop_stopwords=False))
[('昨天', 't'), ('天气', 'n'), ('不错', 'a'), ('开心', 'v'), ('马儿', 'nr'), ('美丽', 'ns'), ('花儿', 'n')]
['Today', 'is', 'sunday', ',', 'everyone', 'is', 'very', 'happy', '!']

# 数据集划分
>>> corpus = ["A"] * 766
>>> train_dataset, dev_test, test_dataset = takin.split_dataset(corpus, ratio="7:2:1")
>>> print(len(train_dataset))
>>> print(len(dev_test))
>>> print(len(test_dataset))
537
154
75
```

<h3>3. 简单任务 (NLP Tasks)</h3>

```python
import takin

# 基于tf-idf的无监督关键词抽取
>>> corpus = [["w1", "w2", ...], ["w1", "w2", ...], ...]  # 自己准备
>>> idf = takin.get_idf(corpus)
>>> test5 = "社会工程的基础是定量测量.定量测量技术的要点包括测量原理、测量对象、测量公式、测量单位、测量频率等.测量对象一是社会成员,二是社会活动.测量原理是通过测算凝聚在人际交往中的社会能量(测量单位),在数量层面定义社会成员和社会活动的社会作用,从而形成了测量两者的具体公式.测量单位包括直接能量和间接能量的区别.测量技术在社会工程中有广泛的应用,可应用于高能控制工程、低能控制工程和定向控制工程."
>>> tokenized_test5 = takin.tokenize(test5, lang="zh", drop_stopwords=True)
>>> golden_truth = ["定量测量", "能量强度", "社会工程"]
>>> print(takin.extraction_with_tfidf(idf, tokenized_test5, topk=5))
[('控制工程', 28.826495997846088), ('测量', 22.65360513253593), ('社会活动', 22.303221799004074), ('单位', 19.404087649523138), ('成员', 16.300763937635697)]
```

# To-do list
### 文本解析 (Text Parsing)
- [ ] 从html、pdf、word、msg、ppt、excel中提取文本

### 数据清洗 (Data Cleaning)
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

### 数据处理 (Data Processing)
- [x] 分词、词性标注
- [x] 数据划分
- [ ] 词向量转化
- [ ] BPE

### 数据分析 (Data Analysis)
- [ ] 词频统计(词云)
- [ ] 字数统计/句数统计/段数统计

### 数据增强 (Data Augmentation)
- [x] 近义词替换
- [x] 随机删除、交换单词
- [ ] 释义生成

### 简单任务
- [ ] 色情文本判断、识别
- [ ] 情感分析
- [x] 关键词提取（基于tf-idf的无监督关键词抽取）
- [ ] 命名实体识别
- [ ] 摘要生成
- [ ] 事件抽取

<b>目前Takin整体还处于初期开发阶段，才疏学浅，若有错误和不当之处，请批评与指正！</b>
Email: yymmjing@gmail.com
