import json
from flask.ext.httpauth import HTTPBasicAuth
from flask import request, render_template, flash, abort, url_for, redirect, session

from testDBTool.model.utils.task import selectDataByParams as selectDataByParams
from testDBTool import app
from testDBTool.model.utils import commonFun
from testDBTool.model.utils import configDB

auth = HTTPBasicAuth()


# 静态模板index.html等都放在‘/static/'下。　路由不用再加’/static/index.html‘而是'index.html'就好
@app.route('/sqlExecute', methods=['POST'])
def sqlExecuteFun(host_name, database_db, sqlStr):
    """

    :param host_name:测试环境
    :param database_db:数据库名
    :param sqlStr:执行的sql
    :return:
    """

    database_db = ""
    sqlStr = ""
    host_name = []

    # TODO ：for循环
    '''
        读取配置
        连接数据库
        执行sql
        返回执行结果
        关闭数据库连接

    '''

    # TODO： 定义执行成功和失败的返回

    # TODO： 数据库配置写在配置文件中
    # TODO： 通用方法读取配置文件



    sql1 = commonFun.get_sql('bi_export', 'crm_shop_daily', 'select_shop_daily_all')
    sql2 = commonFun.get_sql('bi_export', 'crm_shop_daily', 'select_shop_daily')
    try:
        # 生成带参数的sql
        cursor1 = configDB.executeSQL(sql1, None)
        # 执行sql
        dataLocal = configDB.get_all(cursor1)

        print(dataLocal)
        print('-----------------------')
        print(dataBeta1)

        log.build_out_info_line('查询成功')

    except ConnectionError as ex:
        log.build_out_info_line('查询失败')
        log.build_out_info_line(str(ex))
