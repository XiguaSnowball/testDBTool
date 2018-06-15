import pymysql
from testDBTool.model.utils import readDBConfig as readDBConfig
from testDBTool.model.utils.Log import MyLog as Log

localReadConfig = readDBConfig.readDBConfig()


class MyDB:
    global host, username, password, port, database, config
    host = localReadConfig.get_db_info("host")
    username = localReadConfig.get_db_info("username")
    password = localReadConfig.get_db_info("password")
    port = localReadConfig.get_db_info("port")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
    }

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
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

    def executeSQL(self, sql, params):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDB()
        # executing sql
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()
        self.log.build_out_info_line("执行sql")

        return self.cursor

    # def executeSQLByDatabase(self, sql, databaseName):
    #     """
    #     execute sql
    #     :param sql:
    #     :return:
    #     """
    #     self.connectDB()
    #     # executing sql
    #     self.cursor.execute(sql,)
    #     # executing by committing to DB
    #     self.db.commit()
    #     self.log.build_out_info_line("执行sql")
    #
    #     return self.cursor

    def get_all(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        self.log.build_out_info_line("获取查询结果:" + str(value))

        return value

    def closeDB(self):
        """
        close database
        :return:
        """
        self.db.close()
        self.log.build_out_info_line("Database closed!")
