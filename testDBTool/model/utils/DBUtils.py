import pymysql

from testDBTool.model.utils import readConfig as readConfig
from testDBTool.model.utils.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()
log = Log.get_log()
logger = log.get_logger()


class DBUtils:
    # global host, username, password, port, database, config

    def get_db(hostName, databaseName):
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

    def connectDB(hostName, database):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            config = DBUtils.get_db(hostName, database)
            DBUtils.db = pymysql.connect(**config, charset='utf8')
            # create cursor
            DBUtils.cursor = DBUtils.db.cursor()
            log.build_out_info_line("Connect DB successfully!")
        except ConnectionError as ex:
            logger.error(str(ex))
        return DBUtils.cursor

    def executeSQL(hostName, database, sql,resultJson):
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
            log.build_out_info_line("执行成功" + "=====host为" + hostName)
            resultJson.append({"host": hostName, "msg": "执行成功","error": ''})

        except Exception as ex:
            log.build_out_error_line(str(ex))
            resultJson.append({"host": hostName, "msg": "执行失败", "error": str(ex)})


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
