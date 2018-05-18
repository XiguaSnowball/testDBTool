import pymysql
import readConfig as readConfig
from utils.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()


class MyLocalDB:
    global host, username, password, port, database, config

    host = localReadConfig.get_db_local("host")
    username = localReadConfig.get_db_local("username")
    password = localReadConfig.get_db_local("password")
    port = localReadConfig.get_db_local("port")
    database = localReadConfig.get_db_local("database")
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

    def connectDBLocal(self):
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

    def executeSQLLocal(self, sql, params):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDBLocal()
        # executing sql
        self.log.build_out_info_line("执行sql")
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()

        return self.cursor

    def get_all_dblocal(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = (cursor.fetchall())
        return value

    def get_one_dblocal(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        self.log.build_out_info_line("获取返回值")

        return value

    def closeDBLocal(self):
        """
        close database
        :return:
        """
        self.db.close()
        self.log.build_out_info_line("Database closed!")
