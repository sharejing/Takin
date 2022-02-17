<div align="center"><img src="https://github.com/sharejing/Takin/blob/main/images/takin_logo.PNG" height="150px"/></div>

<h2 align="center">A Python Toolkit for File Processing, Text Cleaning and Data Splitting</h2>

实验室数据大多由人工众包构建而成，其格式规范，内容干净，数据经过一些简单清洗便能用于模型训练；而真实环境下的数据往往来自于一些用户日志、员工记录等，其文件格式众多，数据内容包含大量噪声，想要获得内容干净、格式规范统一的数据，就需要对这些数据进行深度清洗。Takin就是一款用于真实环境下文件处理、文本清洗和数据划分的开源工具。通过对外提供函数接口的方式，帮助使用者快速获取模型的输入数据。

🚩<b>Takin的最终目标是：对于任何格式和内容的数据，通过Takin就能完全得到你所期望的最规范、最干净的数据。</b>

为了接近并最终达到这个目标，Takin目前包含以下功能：
* 文件处理：读取和写入各种文件；
* 文本清洗：提供多个清洗函数接口（如删除数字、序号、标点、特殊字符等）；
* 数据划分：快速划分训练集、验证集和测试集。

<h2 align="center">Installation&Usage&Plan</h2>
<h3>:sunny: Installation</h3>

```bash
pip install takin
```

<h3>:sunny: Plan&Usage</h3>

### 文件处理 (File Processing)
- [x] 加载Json文件，整个Json文件是一个python字典 [load_single_json](../../wiki/File-Processing#load_single_json)
- [x] 加载Json文件，一行是一个python字典 [load_multi_json](../../wiki/File-Processing#load_multi_json)
- [x] 将python字典或字典列表写入Json文件 [write_json](../../wiki/File-Processing#write_json)
- [x] 输出给定目录里的所有指定文件类型的绝对路径 [output_filenames](../../wiki/File-Processing#output_filenames)
- [x] 加载单个纯文本文件 load_single_txt
- [x] 加载给定目录里的所有纯文本文件 load_multi_txt
- [x] 将python列表数据写入纯文本文件 write_txt
- [x] 加载yaml参数配置文件 load_yaml
- [x] 将数据写入excel文件 write_excel

### 文本清洗 (Text Cleaning)
- [x] 删除文本中的转移字符 delete_escape_character
- [x] 删除文本中的多余空白 delete_extra_whitespace
- [x] 删除文本中的数字 delete_digit
- [x] 删除文本中的所有标点符号(包括特殊符号) delete_punctuation
- [x] 删除英文字母 delete_letter
- [x] 删除汉字 delete_chinese
- [x] 删除括号以及括号里的内容 delete_bracket
- [x] 删除文本中的序号 delete_series_number
- [x] 连续重复的标点符号只保留一次 delete_repeated_punc

### 数据划分 (Data Splitting)
- [x] 给定一个原始数据集，按照比例将其划分为训练集、验证集、测试集 split_dataset
- [x] corpus中每个元素是dict，按照类别进行数据切分 split_dataset_by_class

<b>目前Takin仍处于开发阶段，才疏学浅，若有错误和不当之处，请批评与指正！</b>

<b>如果您有更好的想法想一起合作，请联系我：yymmjing@gmail.com</b>
