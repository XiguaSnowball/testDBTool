# _*_ coding: utf-8 _*_
from testDBTool import app

import requests
from flask import request, jsonify
from flask import json


# localConfigHttp = configHttp.ConfigHttp()


# 静态模板index.html等都放在‘/static/'下。　路由不用再加’/static/index.html‘而是'index.html'就好
@app.route('/sqlFormat', methods=['POST'])
def sqlFormat():
    if request.method == 'POST':
        inData = json.loads(request.get_data())
        sqlStrToFormat = inData["sqlStrToFormat"]


        url = 'https://1024tools.com/sqlformat'
        params = {"type": 'format', "query": sqlStrToFormat}

        try:
            response = requests.post(url, params)
            response1= json.loads(response.text)
            print(response1)


            if '>'+sqlStrToFormat in response1['result'] :
                return jsonify({'status':1,'result':sqlStrToFormat})
            else:
                return jsonify(response1)

        except Exception as ex:
            return str(ex)

