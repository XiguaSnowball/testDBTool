# _*_ coding: utf-8 _*_


from flask import request, jsonify
from flask import json
import pandas as pd

from testDBTool import app
from testDBTool.model.utils import configDBBeta1 as Beta1DB
from testDBTool.model.utils.commonFun import log
from testDBTool.model.utils import DBUtils as dbUtils

configDBBeta1 = Beta1DB.MyBeta1DB()


# 静态模板index.html等都放在‘/static/'下。　路由不用再加’/static/index.html‘而是'index.html'就好
@app.route('/sqlExecute', methods=['POST'])
def sqlExecuteFun():
    if request.method == 'POST':
        inData = json.loads(request.get_data())

        database = inData["database"]
        hostNameList = inData["hostNameList"]
        sqlStr = inData["sqlStr"]

        # sqlStr = """CREATE TABLE `gms_template_goods_shelf` (`id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',`template_name` varchar(10) COLLATE utf8_bin NOT NULL COMMENT '模板展示名称',`template_inner_name` varchar(50) COLLATE utf8_bin NOT NULL COMMENT '模板内部名称',`template_type` varchar(10) COLLATE utf8_bin DEFAULT NULL COMMENT '模板分类:A-100人以上|B-100人以下|X-特殊类',`store_condition` tinyint(1) NOT NULL COMMENT '存储条件 (1,"冷藏";2,"常温";3,"冷冻",4,"加热")',`cities` varchar(1000) COLLATE utf8_bin NOT NULL DEFAULT '''''' COMMENT '模板匹配的城市',`status` tinyint(1) NOT NULL COMMENT '启用状态：1：启用；0：禁用',`create_time` datetime NOT NULL COMMENT '模板创建时间',`create_user` varchar(30) COLLATE utf8_bin NOT NULL COMMENT '创建货架模板用户',`update_time` datetime DEFAULT NULL COMMENT '更新时间',`update_user` varchar(30) COLLATE utf8_bin DEFAULT NULL COMMENT '更新货架模板用户',`del_flag` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1:正常|0:删除',PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8 COLLATE=utf8_bin; """

        #         sqlStr = """CREATE TABLE `pss_city_template` (
        #   `id` int(11) NOT NULL AUTO_INCREMENT,
        #   `city_id` int(11) NOT NULL COMMENT '城市id',
        #   `grade` varchar(4) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT '等级编码',
        #   `store_condition` smallint(2) DEFAULT NULL COMMENT '存储条件',
        #   `template_id` int(11) NOT NULL COMMENT '模版id',
        #   `is_default` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1:默认|0:非默认',
        #   `create_user` varchar(30) NOT NULL COMMENT '创建人',
        #   `create_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '创建时间',
        #   `update_user` varchar(30) DEFAULT NULL COMMENT '修改人',
        #   `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
        #   `del_flag` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1:正常|0:删除',
        #   PRIMARY KEY (`id`)
        # ) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COMMENT='公司模版默认信息';"""

        for hostName in hostNameList:
            try:
                log.build_out_info_line("开始执行" + "【---------" + hostName + "----------】")
                result_data = dbUtils.DBUtils.executeSQL(hostName, database, sqlStr)

                # rs = result_data.fetchall()
                # results_data2 = pd.DataFrame(list(rs))

                dbUtils.closeDB()
                exc_flag = True

            except Exception as ex:
                log.build_out_error_line(str({'message': "执行失败", "data": {"hostname": hostName}, "error": ex}))
                exc_flag = False
                # return jsonify({'message': "执行失败", "data": {"hostname": hostName, "error": str(ex)}})
        # log.build_out_info_line("=*30")
        return jsonify({'message': "执行完成", "data": {"hostname": hostNameList}, "sql": sqlStr})
    else:
        return
