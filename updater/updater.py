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
db = DbConnector()

# Add pastolesto_menu
for menu in pastolesto_menu:
    db.insertMenu(menu['menu'], int(menu['calorie']), menu['day'], 'pastolesto')

# Add dinner menu
for menu in complete_menu_dinner:
    db.insertMenu(menu['menu'], int(menu['calorie']), menu['day'], 'dinner')

# Add lunch menu
for menu in complete_menu_lunch:
    db.insertMenu(menu['menu'], int(menu['calorie']), menu['day'], 'lunch')