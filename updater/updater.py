from parsecanteen import Canteen
from dbconnector import DbConnector

# Retrieve latest xls files from the website
cant = Canteen()
cant.update()

# Parse the xls file
pastolesto_menu = cant.getPastolestoMenu()
complete_menu_dinner = cant.getCompleteMenuDinner()
complete_menu_lunch = cant.getPastolestoMenu()

# Init db connector
#db = DbConnector()
for menu in pastolesto_menu:
    print(menu)