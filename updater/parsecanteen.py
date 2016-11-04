#!/usr/bin/python
# -*- coding: utf-8 -*-

import xlrd
import datetime
import re
import requests
from bs4 import BeautifulSoup
import urllib.request

class Canteen:

    def __cleanMenu(self, menu):
        name = menu[0]
        name = name.replace('*', '')
        name = name.replace(',', '')
        name = re.sub('\d', '', name)
        return (name.strip(), menu[1], menu[2])

    def __getMenu(self, xlsfile, sheet):
        date_regex = '\d{1,2}\/\d{1,2}'
        book = xlrd.open_workbook(xlsfile)
        sh = book.sheet_by_index(sheet)
        menu = []
        for column in range(0, sh.ncols):
            for row in range(0, sh.nrows):
                cell_value = '%s' % sh.cell_value(row, column)
                match = re.search(r'\d{1,2}\/\d{1,2}', cell_value)
                if match:
                    # cell_value is a date
                    for rx in range(row + 1, row + 9):
                        if sh.cell_value(rx, column) != '':
                            detail = (sh.cell_value(rx, column),
                                    sh.cell_value(rx, column + 1), match.group())
                            menu.append(self.__cleanMenu(detail))
        return menu

    def __convertToDic(self, menu):
        menu_dic = []
        i = 0
        for ele in menu:
            menu_dic.append({'name': menu[i][0], 'calorie': menu[i][1], 'day': menu[i][2]})
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
        
    def update(self):
    	r = requests.get('http://www.operauni.tn.it/servizi/ristorazione/menu')
    	if r.status_code == 200:
    		soup = BeautifulSoup(r.text, 'html.parser')
    		documents_link = []
    		for download_button in soup.find_all('i', 'icon-download'):
    			documents_link.append(download_button.parent['href'])
    		
    		urllib.request.urlretrieve(documents_link[0], './resources/complete.xls')
    		urllib.request.urlretrieve(documents_link[1], './resources/pastolesto.xls')