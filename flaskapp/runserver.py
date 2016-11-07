#from services.canteen import Canteen
import json
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/canteen")
def canteen():
	err_resp = {"message": "no food today"}
	return json.dumps(err_resp)

if __name__ == "__main__":
    app.run()
