# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__, static_url_path='', root_path='/Users/xingyukun/PycharmProjects/testDBTool/testDBTool/')

# 只有在app对象之后声明，用于导入view模块

# from testDBTool.controller import testController
# from testDBTool.controller import dbController
from testDBTool.controller import sqlExecuteController
from testDBTool.controller import sqlFormatController

