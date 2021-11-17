<div align="center"><img src="https://github.com/sharejing/Takin/blob/main/images/takin_logo.PNG" height="150px"/></div>

<h2 align="center">Takin: A Python Toolkit for File Parsing, Text Cleaning and Data Splitting</h2>

实验室数据大多由人工众包构建而成，其格式规范，内容干净，数据经过一些简单清洗便能用于模型训练；而真实环境下的数据往往来自于一些用户日志、员工记录等，其文件格式众多，数据内容包含大量噪声，想要获得内容干净、格式规范统一的数据，就需要对这些数据进行深度清洗。Takin就是一款用于真实环境下文件解析、文本清洗和数据划分的开源工具。通过对外提供函数接口的方式，帮助使用者快速获取模型的输入数据。

🚩<b>Takin的最终目标是：对于任何格式和内容的数据，通过Takin就能完全得到你所期望的最规范、最干净的数据。</b>

为了接近并最终达到这个目标，Takin目前包含以下功能：
* 文件解析：从多种文件格式 (txt/docx/pptx/pdf/html/eml)中解析文本；
* 文本清洗：提供多个清洗函数接口（如删除数字、序号、标点、特殊字符等）；
* 数据划分：快速划分训练集、验证集和测试集。

<h2 align="center">Installation&Usage&Plan</h2>
<h3>:sunny: Installation&Usage</h3>

```bash
pip install takin
```

> 具体的API使用请查阅Takin的开发者文档：[The_guideline_of_Takin.pdf](https://github.com/sharejing/Takin/blob/main/The_guideline_of_Takin.pdf) :point_up:

<h3>:sunny: Plan</h3>

### 文件解析 (File Parsing)
- [x] 从txt/docx/pptx/pdf/html/eml中提取文本

### 文本清洗 (Text Cleaning)
- [x] 删除转义字符
- [x] 删除文本中的多余空白
- [x] 删除文本中的数字
- [x] 删除文本中的所有标点符号(包括特殊符号)
- [x] 删除英文字母
- [x] 删除汉字
- [x] 删除括号及括号里的内容
- [x] 删除序号
- [x] 连续重复的标点符号只保留一次

### 数据划分 (Data Splitting)
- [x] 给定一个原始数据集，按照比例将其划分为训练集、验证集、测试集
- [x] 给定一个有类别的数据集，在每个类别中按比例划分

<b>目前Takin仍处于开发阶段，才疏学浅，若有错误和不当之处，请批评与指正！</b>

<b>如果您有更好的想法想一起合作，请联系我：yymmjing@gmail.com</b>
