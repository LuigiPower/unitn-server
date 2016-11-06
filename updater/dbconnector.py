#!/usr/bin/python
import mysql.connector as mariadb

class DbConnector():
    def __init__(self):
        self.mariadb_connection = mariadb.connect(host='db', user='studente',
                                     password='unitn', database='canteendb')
        self.cursor = mariadb_connection.cursor()
    


