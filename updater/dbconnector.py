#!/usr/bin/python
import pymysql

class DbConnector():
    def __init__(self):
        self.mariadb_connection = pymysql.connect(host='db', user='studente',
                                     password='unitn', db='canteendb')
        self.cursor = mariadb_connection.cursor()
    


