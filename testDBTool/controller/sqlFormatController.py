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
            response1 = json.loads(response.text)
            if response1:
                if '>' + sqlStrToFormat in response1['result']:
                    return jsonify({'status': 1, 'result': sqlStrToFormat, 'error': '格式化失败咯,不是标准SQL'})
                else:
                    status = response1['status']
                    result = response1['result']
                    resultR = jsonify({'status': status, 'result': result, 'error': 'SQL格式化成功^_^'})
                    return resultR
            else:
                return jsonify({'status': 1, 'result': sqlStrToFormat, 'error': '格式化失败,不知道咋了。。'})

        except Exception as ex:
            return jsonify({'status': 1, 'result': sqlStrToFormat, 'error': '格式化失败,异常了'})
