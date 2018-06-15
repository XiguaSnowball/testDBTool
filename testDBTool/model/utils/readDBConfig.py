import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "dbConfig.ini")


class readDBConfig:
    fd = open(configPath)
    data = fd.read()

    #  remove BOM
    if data[:3] == codecs.BOM_UTF8:
        data = data[3:]
        file = codecs.open(configPath, "w")
        file.write(data)
        file.close()
    fd.close()

    cf = configparser.ConfigParser()
    cf.read(configPath)
    #
    # def get_db_config(databaseName):
    #     value = readDBConfig.cf.get(databaseName)
    #     print(value)
    #     return value

    def get_db_info(self, hostName, name):
        value = readDBConfig.cf.get(hostName,name)
        # print(value)
        return value
#