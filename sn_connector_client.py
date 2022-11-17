import requests

from dto.trello_config import TrelloConfig


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
        self.host = 'http://127.0.0.1:8080'
        self.sn_connector_api = self.host + '/api/sn-connector/trello/'
        self.sn_connector_report_api = self.host + '/api/sn-connector/report'

    def get_trello_config_by_squad(self, squad: str):
        request_params = {
            'squad': squad
        }
        return requests.get(self.sn_connector_api + 'config', headers=self.headers, params=request_params)

    def create_or_update_trello_config(self, trelloConfig: TrelloConfig):
        return requests.post(self.sn_connector_api + 'config', headers=self.headers,
                             data=trelloConfig.toJson().encode('utf-8'))

    def get_parts_open_tickets_report(self):
        return requests.get(self.sn_connector_report_api + '/parts/open-tickets', headers=self.headers)
