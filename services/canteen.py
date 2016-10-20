#!/usr/bin/python
# -*- coding: utf-8 -*-

import xlrd
import datetime
import re


class Canteen:

    def __getDateString(self):
        today = datetime.datetime.today()
        daystring = '%d/%d' % (today.day, today.month)
        return daystring

    def __cleanMenu(self, menu):
        name = menu[0]
        name = name.replace('*', '')
        name = name.replace(',', '')
        name = name.replace('*', '')
        name = re.sub('\d', '', name)
        return (name.strip(), menu[1])

    def __getMenu(self, xlsfile, sheet):
        datestring = self.__getDateString()
        book = xlrd.open_workbook(xlsfile)
        sh = book.sheet_by_index(sheet)
        menu = []
        for column in range(0, sh.ncols):
            for row in range(0, sh.nrows):
                if datestring in '%s' % sh.cell_value(row, column):
                    for rx in range(row + 1, row + 9):
                        if sh.cell_value(rx, column) != '':
                            detail = (sh.cell_value(rx, column),
                                    sh.cell_value(rx, column + 1))
                            menu.append(self.__cleanMenu(detail))
                    return menu
        return menu

    def __convertToDic(self, menu):
        menu_dic = []
        i = 0
        for ele in menu:
            menu_dic.append({'name': menu[i][0], 'calorie': menu[i][1]})
            i = i + 1
        return menu_dic

    def getPastolestoMenu(self):
        menu = self.__getMenu('./resources/pastolesto.xls', 0)
        return self.__convertToDic(menu)

    def getCompleteMenu(self):
        menu = self.__getMenu('./resources/complete.xls', 0)
        return self.__convertToDic(menu)

    def getCompleteMenuDinner(self):
        menu = self.__getMenu('./resources/complete.xls', 1)
        return self.__convertToDic(menu)

