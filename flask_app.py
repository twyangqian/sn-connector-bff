from flask import Flask, request
from config import connectDataBase
from errors import bad_request
from sn_connector_client import createTrelloCard
import json

app = Flask(__name__)


@app.route("/api/sn-connector-bff/trello/cards", methods=['POST'])
def create_trello_card():
    database = connectDataBase()
    squad = request.args.get('squad')
    if squad is None:
        return bad_request("Squad is blank!")

    request_data = request.json

    if request_data is None:
        return bad_request("request data is blank!")

    trello_config = database.getConfigBySquad(squad)
    if trello_config is None:
        return bad_request("Squad Name can not found!")

    res = createTrelloCard(trello_config.trelloBoardId, trello_config.defaultListCardName, trello_config.checkLists,
                           request_data)
    response = json.loads(res.text)
    if res.status_code == 200:
        return response
    else:
        return bad_request(response, res.status_code)
