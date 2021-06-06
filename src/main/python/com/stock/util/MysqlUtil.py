# coding:utf-8

import pymysql


class MysqlUtil:
    def __init__(self, username, password, host, port=3306):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
