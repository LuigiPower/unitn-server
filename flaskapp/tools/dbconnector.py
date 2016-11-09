#!/usr/bin/python
import pymysql
from dateutil.parser import parse, parserinfo
from datetime import datetime

class DbConnector():
    def __init__(self):
        self.mariadb_connection = pymysql.connect(host='db', user='studente',
                                     password='unitn', db='canteendb')

    def getMenu(self, meal_type, date):
        menu = []
        try:
            with self.mariadb_connection.cursor() as cursor:
                # Create a new record
                sql_date = parse(date, parserinfo(True, False)).strftime("%Y-%m-%d %H:%M:%S")
                sql = "SELECT name, calorie FROM meal WHERE (submission_date = %s AND type = %s)"
                cursor.execute(sql, (sql_date, meal_type))

                for name, calorie in cursor:
                    menu.append({'name': name, 'calorie': calorie})
        except Exception as e:
            print(e)
        finally:
            return menu