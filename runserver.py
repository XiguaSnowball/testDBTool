from testDBTool import app


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12139, debug=False)
    # 本地启动去掉host
    # app.run(port=12138, debug=False)
