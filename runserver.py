from services.pastolesto import Canteen
import json
from flask import Flask
app = Flask(__name__)

@app.route("/pastolesto")
def pastolesto():
	canteen = Canteen()
	menu = canteen.getTodayMenu()
	print(menu)
	if menu == None:
		err_resp = {"message": "no food today"}
		return json.dumps(err_resp)
	else:
		menu_dic = [{'name': menu[0][0], 'calorie': menu[0][1]},
					{'name': menu[1][0], 'calorie': menu[1][1]},
					{'name': menu[2][0], 'calorie': menu[2][1]}]
		return json.dumps(menu_dic), 200, {'Content-Type': 'application/json;'}

if __name__ == "__main__":
    app.run()
