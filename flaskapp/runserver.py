import json
from tools.dbconnector import DbConnector
import datetime
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/canteen")
def canteen():
	menu_type = request.args.get('type', None)
	menu_date = request.args.get('date', None)

	if menu_type == None:
		menu_type = '3'

	if menu_date == None:
		today = datetime.datetime.today()
		menu_date = '%d/%d/%d' % (today.day, today.month, today.year)
	else:
		menu_date = '%s/%s/%s' % (menu_date[:2], menu_date[2:4], menu_date[4:8])

	typename = ''
	if menu_type == '0':
		typename = 'pastolesto'
	elif menu_type == '1':
		typename = 'dinner'
	else:
		typename = 'lunch'

	db = DbConnector()
	menu = db.getMenu(typename, menu_date)
	res = {'type': typename, 'date': menu_date, 'menu': menu}

	if not menu:
		err_resp = {"message": "no food today"}
		return json.dumps(err_resp)
	else:
		return json.dumps(res), 200, {'Content-Type': 'application/json;'}

if __name__ == "__main__":
    app.run()