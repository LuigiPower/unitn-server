#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import datetime
import re

class Canteen:
    def __getDateString(self):
        today = datetime.datetime.today()
        daystring = "%d/%d" % (today.day, today.month)
        return daystring #NOTE this returns the daystring, like 19/10

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

        menu = []

        for column in range(0, sh.ncols):
            for row in range(0, sh.nrows):
                if datestring in "%s" % sh.cell_value(row, column):
                    for rx in range(row + 1, row + 8): # 6 rows of data
                        if sh.cell_value(rx, column) != '':
                            detail = (sh.cell_value(rx, column), sh.cell_value(rx, column + 1))
                            menu.append(self.__cleanMenu(detail))
                    return menu
