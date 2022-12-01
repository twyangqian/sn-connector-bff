import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from dto.trello_config import TrelloConfig


class sn_connector_api:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'close',
            'Content-Length': '90',
            'Content-Type': 'application/json;charset=UTF-8',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        }
        self.host = 'http://10.205.129.7:8080'
        self.sn_connector_api = self.host + '/api/sn-connector/trello/'
        self.sn_connector_report_api = self.host + '/api/sn-connector/report'
        self.session = requests.Session()
        self.retry = Retry(connect=3, backoff_factor=0.5)
        self.adapter = HTTPAdapter(max_retries=self.retry)
        self.session.mount('http://', self.adapter)

    def get_trello_config_by_squad(self, squad: str):
        request_params = {
            'squad': squad
        }
        return self.session.get(self.sn_connector_api + 'config', headers=self.headers, params=request_params)

    def create_or_update_trello_config(self, trelloConfig: TrelloConfig):
        return self.session.post(self.sn_connector_api + 'config', headers=self.headers,
                                 data=trelloConfig.toJson().encode('utf-8'))

    def get_parts_open_tickets_report(self):
        return self.session.get(self.sn_connector_report_api + '/parts/open-tickets', headers=self.headers)
