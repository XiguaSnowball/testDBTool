from flask import request
from flask import json
from flask.ext.httpauth import HTTPBasicAuth
import pandas as pd

from testDBTool import app
from testDBTool.model.utils import configDBBeta1 as Beta1DB
from testDBTool.model.utils.commonFun import log

auth = HTTPBasicAuth()
configDBBeta1 = Beta1DB.MyBeta1DB()


# 静态模板index.html等都放在‘/static/'下。　路由不用再加’/static/index.html‘而是'index.html'就好
@app.route('/sqlExecute', methods=['POST'])
def sqlExecuteFun():

    if request.method == 'POST':
        inData = json.loads(request.get_data())

        hostId = inData["hostId"]
        databaseDB = inData["databaseDB"]
        hostName = inData["hostName"]
        sqlStr = inData["sqlStr"]

        try:
            dataBeta1 = configDBBeta1.executeSQLBeta1(sqlStr)
            log.build_out_info_line('执行成功'+"\n执行sql为\n"+sqlStr)
            # log.build_out_info_line(str(dataBeta1))
            rs = dataBeta1.fetchall()
            resultsData = pd.DataFrame(list(rs))
            # print(resultsData)

            configDBBeta1.closeDBBeta1()

            return ('执行成功' + str(resultsData)+"\n执行sql为\n"+sqlStr)




        except ConnectionError as ex:
            log.build_out_info_line('查询失败')
            log.build_out_info_line(str(ex))

    else:
        # return '<h1>只接受post请求！</h1>'
        return
#
# @app.route('/test/json', methods=['GET', 'POST'])
# def jsontest():
#     if request.method == 'POST':
#         a = request.get_data()
#         dict1 = json.loads(a)
#
#         if dict1:
#             # return str(d['title'])
#             return json.dumps(dict1["opr"])
#         else:
#             return ('空的')
#     else:
#         return '<h1>只接受post请求！</h1>'

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
    #
    # try:
    #     # 生成带参数的sql
    #     cursor1 = configDB.executeSQL(sql1, None)
    #     # 执行sql
    #     dataLocal = configDB.get_all(cursor1)
    #
    #     print(dataLocal)
    #     print('-----------------------')
    #     print(dataBeta1)
    #
    #     log.build_out_info_line('查询成功')
    #
    # except ConnectionError as ex:
    #     log.build_out_info_line('查询失败')
    #     log.build_out_info_line(str(ex))
