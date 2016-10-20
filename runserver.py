from services.canteen import Canteen
import json
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/canteen")
def canteen():
	cant = Canteen()
	menu_type = request.args.get('type')
	if not menu_type:
		return json.dumps({"message": "wrong request"}), 500, {'Content-Type': 'application/json;'}
	
	if menu_type == '0':
		menu = cant.getPastolestoMenu()
	elif menu_type == '1':
		menu = cant.getCompleteMenuDinner()
	else:
		menu = cant.getCompleteMenu()
		
	if not menu:
		err_resp = {"message": "no food today"}
		return json.dumps(err_resp)
	else:
		return json.dumps(menu), 200, {'Content-Type': 'application/json;'}
	
if __name__ == "__main__":
    app.run()
