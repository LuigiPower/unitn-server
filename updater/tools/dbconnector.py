#!/usr/bin/python
import pymysql
from dateutil.parser import parse 

class DbConnector():
    def __init__(self):
        self.mariadb_connection = pymysql.connect(host='db', user='studente',
                                     password='unitn', db='canteendb')

    def insertMenu(self, menu, calorie, date, meal_type):
        try:
            with self.mariadb_connection.cursor() as cursor:
                # Create a new record
                sql_date = parse(date).strftime("%Y-%d-%m %H:%M:%S")
                sql = "INSERT INTO 'meal' ('name', 'calorie', 'type', 'submission_date') VALUES (%s, %d, %s, %s)"
                cursor.execute(sql, (name, calorie, meal_type, sql_date))
            self.mariadb_connection.commit()
        except Exception as e:
            print(e.message)
