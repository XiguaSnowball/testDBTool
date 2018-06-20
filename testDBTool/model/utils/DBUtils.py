from importlib import reload

import pymysql
import sys

from testDBTool.model.utils import readDBConfig as readDBConfig
from testDBTool.model.utils.Log import MyLog as Log

localReadConfig = readDBConfig.readDBConfig()
log = Log.get_log()
logger = log.get_logger()


class DBUtils:
    # global host, username, password, port, database, config

    def get_db(hostName,databaseName):
        host_name = 'host'
        username_name = "username"
        password_name = "password"
        port_name = "port"

        host = localReadConfig.get_db_info(hostName, host_name)
        username = localReadConfig.get_db_info(hostName, username_name)
        password = localReadConfig.get_db_info(hostName, password_name)
        port = localReadConfig.get_db_info(hostName, port_name)
        database = databaseName

        config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db': database
        }

        return config

    def connectDB(hostName,database):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            config = DBUtils.get_db(hostName,database)
            DBUtils.db = pymysql.connect(**config)
            # create cursor
            DBUtils.cursor = DBUtils.db.cursor()
            log.build_out_info_line("Connect DB successfully!")
        except ConnectionError as ex:
            logger.error(str(ex))

    def executeSQL(hostName,database,sql):
        """
        execute sql
        :param hostName:
        :param sql:
        :return:
        """
        try:
            DBUtils.connectDB(hostName, database)
            # executing sql
            DBUtils.cursor.execute(sql.encode('utf-8'))
            # executing by committing to DB
            DBUtils.db.commit()
            log.build_out_info_line("执行sql" + sql)
            log.build_out_info_line("执行成功"+"=====host为"+hostName)
        except Exception as ex:
            log.build_out_error_line(str(ex))

        return DBUtils.cursor

    def get_all(cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        return value

    def get_one(cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        log.build_out_info_line("获取查询结果:" + str(value))

        return value

def closeDB():
    """
    close database
    :return:
    """
    DBUtils.db.close()
    log.build_out_info_line("Database closed!")

#

#
# if __name__ == '__main__':
#     config =DBUtils.get_db("beta7","test")
#     con = pymysql.connect(**config)
#     with con:
#         cur=con.cursor()
#         a = """
#             CREATE TABLE crm_dict(
#       `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '编号',
#       `value` varchar(100) NOT NULL COMMENT '数据值',
#       `label` varchar(100) NOT NULL COMMENT '标签名',
#       `type` varchar(100) NOT NULL COMMENT '类型',
#       `description` varchar(100) NOT NULL COMMENT '描述',
#       `sort` int(11) NOT NULL COMMENT '排序（升序）',
#       `parent_id` bigint(20) DEFAULT '0' COMMENT '父级编号(预留)',
#       `create_user` varchar(64) DEFAULT NULL COMMENT '创建者',
#       `create_time` datetime NOT NULL COMMENT '创建时间',
#       `update_user` varchar(64) DEFAULT NULL COMMENT '更新者',
#       `update_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
#       `remarks` varchar(255) DEFAULT NULL COMMENT '备注信息',
#       `del_flag` tinyint(4) NOT NULL DEFAULT '1' COMMENT '删除标记：1、正常，0、删除',
#       PRIMARY KEY (`id`),
#       KEY `console_dict_value` (`value`),
#       KEY `console_dict_label` (`label`),
#       KEY `console_dict_del_flag` (`del_flag`)
#     ) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8 COMMENT='字典表';"""
#         cur.execute(a.encode('utf-8'))
#
