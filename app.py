from flask import Flask, request
from flask_api import status
import requests
import os


app = Flask(__name__)


@app.route("/api/v2/poke")
def poke():

    endpoint_poke_api = request.headers.get("endpoint_poke_api")
    ability_name = request.headers.get("ability_name")

    response = requests.get(str(endpoint_poke_api))
    response = response.json()
    abilities = response["abilities"]

    for ability in abilities:
        if ability_name == ability["ability"]["name"]:
            return {"status": "success", "message": "This pokemon has the ability!", "data": abilities}, 200
        else:
            return {"status": "not found", "message": "This pokemon hasn't the ability"}, 404


@app.route("/api/v2/status")
def status():
    return {"status": "success", "data": str(os.environ)}, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)
