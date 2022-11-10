import requests
import json

sn_connector_api = 'http://127.0.0.1:8080/api/sn-connector/trello/'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '90',
    'Content-Type': 'application/json;charset=UTF-8',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
}


def createTrelloCard(boardId: str, defaultListCard: str, checkLists: [], request_data):
    request_params = {
        "boardId": boardId,
        "defaultListCard": defaultListCard,
        "checkLists": checkLists
    }
    return requests.post(sn_connector_api + 'cards', headers=headers, params=request_params, data=json.dumps(request_data).encode('utf-8'))
