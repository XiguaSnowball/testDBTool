# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__, static_url_path='', root_path='/Users/xingyukun/PycharmProjects/testDBTool/testDBTool/')
# app = Flask(__name__)


# 只有在app对象之后声明，用于导入view模块

from dbTool.controller import testController
