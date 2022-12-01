from flask import Flask, request
from flask_api import status
import requests
import os

ENDPOINT_POKE_API = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(ENDPOINT_POKE_API)
response = response.json()

abilities = response["abilities"][0]
ability_name = abilities["ability"]["name"]


app = Flask(__name__)


@app.route("/api/v2/poke/<abilit_I_wish>")
def poke(abilit_I_wish):
    if abilit_I_wish in ability_name:
        return {"status": "success", "message": "you find limber ability!", "data": abilities}, 200
    else:
        return "limber is not here"


@app.route("/api/v2/status")
def status():
    return {"status": "success", "data": str(os.environ)}, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)
