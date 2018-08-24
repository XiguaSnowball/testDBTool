# _*_ coding: utf-8 _*_


from flask import request, jsonify
from flask import json

from testDBTool import app
from testDBTool.model.utils.commonFun import log
from testDBTool.model.utils import DBUtils as dbUtils


# 静态模板index.html等都放在‘/static/'下。　路由不用再加’/static/index.html‘而是'index.html'就好
@app.route('/sqlExecute', methods=['POST'])
def sqlExecuteFun():
    if request.method == 'POST':
        inData = json.loads(request.get_data())

        database = inData["database"]
        hostNameList = inData["hostNameList"]
        sqlStr = inData["sqlStr"]
        resultJson = []
        # sqlStr = """CREATE TABLE `gms_template_goods_shelf` (`id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',`template_name` varchar(10) COLLATE utf8_bin NOT NULL COMMENT '模板展示名称',`template_inner_name` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '模板内部名称',`template_type` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '模板分类:A-100人以上|B-100人以下|X-特殊类',`store_condition` tinyint(1) NOT NULL COMMENT '存储条件 (1,"冷藏";2,"常温";3,"冷冻",4,"加热")',`cities` varchar(1000) COLLATE utf8_bin NOT NULL DEFAULT '''''' COMMENT '模板匹配的城市',`status` tinyint(1) NOT NULL COMMENT '启用状态：1：启用；0：禁用',`create_time` datetime NOT NULL COMMENT '模板创建时间',`create_user` varchar(30) COLLATE utf8_bin NOT NULL COMMENT '创建货架模板用户',`update_time` datetime DEFAULT NULL COMMENT '更新时间',`update_user` varchar(30) COLLATE utf8_bin DEFAULT NULL COMMENT '更新货架模板用户',`del_flag` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1:正常|0:删除',PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8 COLLATE=utf8_bin; """

        # sqlStr = """ALTER TABLE `crm_company_approval` MODIFY COLUMN `pics` varchar(1200) NOT NULL DEFAULT '' COMMENT '图片饿' AFTER `repeat_company_ids`;"""

        for hostName in hostNameList:
            try:
                log.build_out_info_line("开始执行" + "【---------" + hostName + "----------】")
                dbUtils.DBUtils.executeSQL(hostName, database, sqlStr, resultJson)

                dbUtils.closeDB()
            except Exception as ex:
                log.build_out_error_line(str({'message': "执行失败", "data": {"hostname": hostName}, "error": ex}))
                # return jsonify({'message': "执行失败", "data": {"hostname": hostName, "error": str(ex)}})
                # return jsonify({'message': "执行失败", "data": resultJson})
        # return jsonify({'message': "执行完成", "data": {"hostname": hostNameList}, "excuResult": resultJson})
        return jsonify({'code': 0, 'msg': "执行完成", "excuResult": resultJson})
    else:
        return
