#! /usr/bin/env python
# -*- coding: utf-8 -*_
from distutils.core import setup

import setuptools

setup(
    name='spider',  # 包的名字
    version='0.0.1',  # 版本号
    description='spider',  # 描述
    author='zjx',  # 作者
    author_email='zhongjixin@163.com',  # 你的邮箱**
    package_dir = {'':'lib'},
    packages=setuptools.find_packages(),
    # 依赖包
    install_requires=[
        "requests",
        "lxml",
        "mysqlclient",
        "cx_Oracle",
        "apscheduler"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: windows server 2012'  # 你的操作系统
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # BSD认证
        'Programming Language :: Python',  # 支持的语言
        'Programming Language :: Python :: 3',  # python版本 。。。
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
)
