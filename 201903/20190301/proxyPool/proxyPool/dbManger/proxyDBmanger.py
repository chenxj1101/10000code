#!/usr/bin/env python
# coding=UTF-8
'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Description: IP代理池，数据库部分
@Date: 2019-03-01 15:53:54
'''

import pymysql
import logging

from config import config
from config.config import get_log_config

class ProxyDBmanager(object):

    def __init__(self):

        get_log_config()

        self.__proxy_table = 'proxy'

        self.conn = pymysql.connect(
            host=config.MYSQL_HOST,
            db=config.MYSQL_DBNAME,
            user=config.MYSQL_USER,
            passwd=config.MYSQL_PASSWORD,
            charset = 'utf8',
            use_unicode=False
        )

        with self.conn:
            self.cursor = self.conn.cursor()
    

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


    def create_proxy_table(self, ):
        create_table_sql = (
            "CREATE TABLE IF NOT EXISTS {} ("
            "`id` INT(9) NOT NULL AUTO_INCREMENT,"
            "`IP` BIGINT(10) NOT NULL,"
            "`port` INT(5) NOT NULL,"
            "`http_type` VARCHAR(6) NOT NULL,"
            "`area` VARCHAR(200),"
            "`anonymity` VARCHAR(25),"
            "`speed` VARCHAR(25) DEFAULT '-1',"
            "`failed_count` INT(2) DEFAULT 0,"
            "`agent` VARCHAR(25),"
            "`survival_time` VARCHAR(25),"
            "PRIMARY KEY(id)"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8".format(self.__proxy_table, self.__proxy_table)
        )

        try:
            self.cursor.execute(create_table_sql)
            self.conn.commit()
            logging.debug('===== 成功创建数据库 proxy 表 =====')

        except Exception as e:
            logging.exception('===== 创建数据库 proxy 表出现异常 =====\n %s', e)

    
    def drop_proxy_table(self):
        delete_sql = "DROP TABLE IF EXISTS {}".format(self.__proxy_table)
        try:
            self.cursor.execute(delete_sql)
            self.conn.commit()
            logging.debug('====== 成功删除 ' + self.__proxy_table + '表 =====')

        except Exception as e:
            logging.exception('===== mysql delete data exception =====\n %s', e)