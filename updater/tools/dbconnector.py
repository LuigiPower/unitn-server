#!/usr/bin/python
import pymysql
from dateutil.parser import parse, parserinfo
from datetime import datetime

class DbConnector():
    def __init__(self):
        self.mariadb_connection = pymysql.connect(host='db', user='studente',
                                     password='unitn', db='canteendb')

    def insertMenu(self, name, calorie, date, meal_type):
        try:
            with self.mariadb_connection.cursor() as cursor:
                # Create a new record
                sql_date = parse(date, parserinfo(True, False)).strftime("%Y-%m-%d %H:%M:%S")
                sql = "INSERT INTO meal (name, calorie, type, submission_date) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (name, calorie, meal_type, sql_date))
            self.mariadb_connection.commit()
        except Exception as e:
            print(e)
    
    def cleanMealTable(self):
        try:
            with self.mariadb_connection.cursor() as cursor:
                sql = "DELETE from meal"
                cursor.execute(sql)
            self.mariadb_connection.commit()
        except Exception as e:
            print(e)

