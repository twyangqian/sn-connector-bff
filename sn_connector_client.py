import requests

from config import TrelloConfig


class sn_connector_api:
    def __init__(self):
        self.headers = {
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
        self.sn_connector_api = 'http://10.205.129.7:8080/api/sn-connector/trello/'

    def get_trello_config_by_squad(self, squad: str):
        request_params = {
            'squad': squad
        }
        return requests.get(self.sn_connector_api + 'config', headers=self.headers, params=request_params)

    def create_or_update_trello_config(self, trelloConfig: TrelloConfig):
        return requests.post(self.sn_connector_api + 'config', headers=self.headers,
                             data=trelloConfig.toJson().encode('utf-8'))
