#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import datetime
import re

class Canteen:
    def __getDateString(self):
        days = ["LUNEDÌ", "MARTEDÌ", "MERCOLEDÌ", "GIOVEDÌ", "VENERDÌ"]
        today = datetime.datetime.today()
        weekday = today.weekday()
        weekstring = days[weekday]
        daystring = "%d/%d" % (today.day, today.month)
        datestring = weekstring + " " + daystring
        return datestring

    def __cleanMenu(self, menu):
        name = menu[0]
        name = name.replace('*', '')
        name = name.replace(',', '')
        name = name.replace('*', '')
        name = re.sub('\d', '', name)
        return name.strip(), menu[1]

    def getTodayMenu(self):
        datestring = self.__getDateString()
        book = xlrd.open_workbook("./resources/menusettimanale.xls")
        sh = book.sheet_by_index(0)

        # rows from 5 to 11 contain the information we need
        # 11 - 5 = 6 --> 5 rows of info
        rx = 3
        # columns from 1 to 15 contain the information we need
        # look for DAY x/xx
        cx = 1

        currentweek = 1
        columntolookfor = -1

        while columntolookfor == -1:
            for cx in range(sh.ncols):
                if sh.cell_value(rx, cx) == datestring:
                    columntolookfor = cx

            if currentweek >= 4 or columntolookfor != -1:
                break
            else:
                rx = rx + 35 #Go to the next week
                currentweek = currentweek + 1

        if columntolookfor == -1:
            return None
        else:
            menu = []
            for row in range(rx + 1, rx + 8): # 6 rows of data
                if sh.cell_value(row, columntolookfor) != '':
                    detail = (sh.cell_value(row, columntolookfor), sh.cell_value(row, columntolookfor + 1))
                    menu.append(self.__cleanMenu(detail))
            return menu
