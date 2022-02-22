# -*- encoding: utf-8 -*-
"""
@File    :   test_new.py
@Time    :   2022/02/17 17:09:05
@Author  :   Yimin Jing
@Contact :   jingym3@lenovo.com
@Desc    :   测试文件处理函数
"""

import takin
# single_json_data = takin.load_single_json("files/single_json.json", prefix="data")
# print(single_json_data)

# multi_json_data = takin.load_multi_json("files/multi_json.json")
# print(multi_json_data)

# single_json_data = takin.load_single_json("files/single_json.json", prefix="data")
# multi_json_data = takin.load_multi_json("files/multi_json.json")
# takin.write_json(single_json_data, "files/writed_single_json.json")
# takin.write_json(multi_json_data, "files/writed_multi_json.json")

# paths = takin.output_filenames("files", "json")
# print(paths)

# data = takin.load_single_txt("files/single_txt.txt", keep_enter=True)
# print(data)

# data = takin.load_multi_txt("files/multi_data", file_type="txt", keep_enter=False)
# print(data)

# data = ["123", "2345", "中国人"]
# takin.write_txt(data, "/data/yymmjing/Keeping_Projects/Takin/files/writed_txt.txt")

# config = takin.load_yaml("files/config.yaml")
# print(config)


# data = {"name": ["张三", "李四"], "age": [13, 14], "school": ["苏州市第一幼儿园", "北京市第三幼儿园"]}
# takin.write_excel(data, "files/wrote_excel.xlsx")

# ddata = {"name": ["张三", "李四", "王五"], "age": [13, 14, 17], "school": ["苏州市第一幼儿园", "北京市第三幼儿园", "123456789"]}
# takin.write_excel(ddata, "files/wrote_excel.xlsx", sheet_name="student")

# sata = {"aaaa": ["张三", "李四", "王五"], "bbb": [13, 14, 17], "cccc": ["苏州市第一幼儿园", "北京市第三幼儿园", "123456789"]}
# takin.write_excel(sata, "files/wrote_excel.xlsx", sheet_name="woman")