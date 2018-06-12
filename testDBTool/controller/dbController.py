import json
from flask.ext.httpauth import HTTPBasicAuth
from flask import request, render_template, flash, abort, url_for, redirect, session

from testDBTool.model.utils.task import selectDataByParams as selectDataByParams
from testDBTool import app

auth = HTTPBasicAuth()


# 静态模板index.html等都放在‘/static/'下。　路由不用再加’/static/index.html‘而是'index.html'就好
@app.route('/sqlExecute', methods=['POST'])
def show_results():
    if not session.get('logged_in'):
        abort(401)
    return redirect(url_for('results'))


@app.route('/beta1/bi_export/select', methods=['POST,GET'])
def selectDataByParamsController(shopNo):
    # if request.method == "POST":
    shopNo = request.get('shopNo')
    #     print(shopNo)
    #
    # if request.method == "GET":
    #     print
    #     'call get now'
    #
    #     shopNo = request.args.get('shopNo')

    data_return = selectDataByParams.selectDataByParams(shopNo)

    return data_return


@app.route('/beta1/bi_export/select1', methods=['GET'])
def selectDataByParamsController1():
    shop_no = 'BLDSD00001'
    data_return = selectDataByParams.selectDataByParams(shop_no)
    return data_return

#
if __name__ == '__main__':
    # shop_no = 'BLDSD00001'
    selectDataByParamsController1()
