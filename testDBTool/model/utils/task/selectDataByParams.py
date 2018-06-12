# coding=utf-8
from testDBTool.model.utils import configDBLocal as localDB
from testDBTool.model.utils import configDBBeta1 as Beta1DB
from testDBTool.model.utils import commonFun
from testDBTool.model.utils.commonFun import log

configDBLocal = localDB.MyLocalDB()
configDBBeta1 = Beta1DB.MyBeta1DB()


def selectDataByParams(shopNo):
    # shop_no = 'BLDSD00001'
    shop_no = shopNo
    sql1 = commonFun.get_sql('bi_export', 'crm_shop_daily', 'select_shop_daily_all')
    sql2 = commonFun.get_sql('bi_export', 'crm_shop_daily', 'select_shop_daily')
    try:
        # 生成带参数的sql
        cursor1 = configDBLocal.executeSQLLocal(sql1, None)
        cursor2 = configDBBeta1.executeSQLBeta1(sql2, shop_no)

        dataLocal = configDBLocal.get_all_dblocal(cursor1)
        dataBeta1 = configDBBeta1.get_all_dbBeta1(cursor2)

        print(dataLocal)
        print('-----------------------')
        print(dataBeta1)

        log.build_out_info_line('查询成功')

    except ConnectionError as ex:
        log.build_out_info_line('查询失败')
        log.build_out_info_line(str(ex))
