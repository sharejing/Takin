# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2021/11/17 18:13:17
@Author  :   Sharejing
@Contact :   yymmjing@gmail.com
@Desc    :   
'''

from setuptools import setup


setup(
    name="takin",
    version="1.1.4",
    author="Yimin Jing",
    author_email="yymmjing@gmail.com",
    description="A Python Toolkit for File Processing, Text Cleaning and Data Splitting",
    license="MIT",
    url="https://github.com/sharejing/Takin",
    packages=["takin"],
    keywords="NLP text cleaning file processing data splitting",
    python_requires=">=3.6.0",
    install_requires=[
        "pyyaml",
        "pandas",
        "openpyxl",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)