from xml.etree import ElementTree as ElementTree
from testDBTool.model.utils import readConfig as readconfig
from testDBTool.model.utils.Log import MyLog as mylog
import os

localReadConfig = readconfig.ReadConfig()
proDir = readconfig.proDir
log = mylog.get_log()
logger = log.get_logger()

caseNo = 0

# ****************************** read SQL xml ********************************
database = {}


def get_sql(database_name, table_name, sql_id):
    """
    get sql by given name and sql_id
    :param database_name:
    :param table_name:
    :param sql_id:
    :return:
    """
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql


def set_xml():
    """
    set sql xmlc
    :return:
    """
    if len(database) == 0:
        sql_path = os.path.join(proDir, "testFile", "SQL.xml")
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            database_name = db.get("name")
            # print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                # print(table_name)
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    # print(sql_id)
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[database_name] = table


def get_xml_dict(database_name, table_name):
    """
    get db dict by given name
    :param database_name:
    :param table_name:
    :return:
    """
    set_xml()
    first_dict = database.get(database_name)
    database_dict = first_dict.get(table_name)
    return database_dict
