from parser.canteen import Canteen
from tools.dbconnector import DbConnector

# Retrieve latest xls files from the website
cant = Canteen()
cant.update()

# Parse the xls file
pastolesto_menu = cant.getPastolestoMenu()
complete_menu_dinner = cant.getCompleteMenuDinner()
complete_menu_lunch = cant.getCompleteMenu()

# Init db connector
db = DbConnector()

# Clear all the meal table
db.cleanMealTable()

# Add pastolesto_menu
for menu in pastolesto_menu:
    calorie = 0
    if menu['calorie'] != '':
        calorie = int(menu['calorie'])
    db.insertMenu(menu['name'], calorie, menu['day'], 'pastolesto')

# Add dinner menu
for menu in complete_menu_dinner:
    calorie = 0
    if menu['calorie'] != '':
        calorie = int(menu['calorie'])
    db.insertMenu(menu['name'], calorie, menu['day'], 'dinner')

# Add lunch menu
for menu in complete_menu_lunch:
    calorie = 0
    if menu['calorie'] != '':
        calorie = int(menu['calorie'])
    db.insertMenu(menu['name'], calorie, menu['day'], 'lunch')

print("updated!")
