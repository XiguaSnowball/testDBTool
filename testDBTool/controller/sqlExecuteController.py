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
        sqlStr = """
                                                CREATE TABLE crm_dict(
                                                    `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '编号',
                                                    `value` varchar(100) NOT NULL COMMENT '数据值',
                                                    `label` varchar(100) NOT NULL COMMENT '标签名',
                                                    `type` varchar(100) NOT NULL COMMENT '类型',
                                                    `description` varchar(100) NOT NULL COMMENT '描述',
                                                    `sort` int(11) NOT NULL COMMENT '排序（升序）',
                                                    `parent_id` bigint(20) DEFAULT '0' COMMENT '父级编号(预留)',
                                                    `create_user` varchar(64) DEFAULT NULL COMMENT '创建者',
                                                    `create_time` datetime NOT NULL COMMENT '创建时间',
                                                    `update_user` varchar(64) DEFAULT NULL COMMENT '更新者',
                                                    `update_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
                                                    `remarks` varchar(255) DEFAULT NULL COMMENT '备注信息',
                                                    `del_flag` tinyint(4) NOT NULL DEFAULT '1' COMMENT '删除标记：1、正常，0、删除',
                                                    PRIMARY KEY (`id`),
                                                    KEY `console_dict_value` (`value`),
                                                    KEY `console_dict_label` (`label`),
                                                    KEY `console_dict_del_flag` (`del_flag`)
                                                  ) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8 COMMENT='字典表';"""
        for hostName in hostNameList:
            try:
                result_data = dbUtils.DBUtils.executeSQL(hostName, database, sqlStr)
                log.build_out_info_line('执行成功')

                rs = result_data.fetchall()
                results_data2 = pd.DataFrame(list(rs))

                dbUtils.closeDB()

            except sqlExecuteFun as ex:
                log.build_out_info_line('执行失败')
                log.build_out_info_line(str(ex))

                return jsonify({'message': "执行失败", "data": {"hostname": hostName}, "error": str(ex)})
        return jsonify({'message': "执行完成", "data": {"hostname": hostNameList}, "sql": sqlStr})


    else:
        return
