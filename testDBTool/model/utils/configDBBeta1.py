import pymysql
from testDBTool.model.utils import readConfig as readconfig
from testDBTool.model.utils.Log import MyLog as mylog

localReadConfig = readconfig.ReadConfig()


class MyBeta1DB:
    global host, username, password, port, database, config

    host = localReadConfig.get_db_beta1("host")
    username = localReadConfig.get_db_beta1("username")
    password = localReadConfig.get_db_beta1("password")
    port = localReadConfig.get_db_beta1("port")
    database = localReadConfig.get_db_beta1("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database,
        'charset': 'utf8'
    }

    def __init__(self):
        self.log = mylog.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDBBeta1(self):
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

    def executeSQLBeta1(self, sql, params):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDBBeta1()
        # executing sql
        self.log.build_out_info_line("执行sql")
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()

        return self.cursor

    def get_all_dbBeta1(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = (cursor.fetchall())
        self.log.build_out_info_line("获取返回值")
        return value

    def get_one_dbBeta1(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        self.log.build_out_info_line("获取返回值")

        return value

    def closeDBBeta1(self):
        """
        close database
        :return:
        """
        self.db.close()
        self.log.build_out_info_line("Database closed!")
