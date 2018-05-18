import pymysql
import readConfig as readConfig
from utils.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()


class MyVmDB:
    global host, username, password, port, database, config

    host = localReadConfig.get_db_vm("host")
    username = localReadConfig.get_db_vm("username")
    password = localReadConfig.get_db_vm("password")
    port = localReadConfig.get_db_vm("port")
    database = localReadConfig.get_db_vm("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database,
        'charset': 'utf8'
    }

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDBVm(self):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            self.log.build_out_info_line("Connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQLVm(self, sql, params):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDBVm()
        self.log.build_out_info_line("执行sql")
        self.cursor.execute(sql, params)
        self.db.commit()

        return self.cursor

    def get_all_dbvm(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        return value

    def get_one_dbvm(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        self.log.build_out_info_line("获取返回值")

        return value

    def closeDBVm(self):
        """
        close database
        :return:
        """
        self.db.close()
        self.log.build_out_info_line("Database closed!")
