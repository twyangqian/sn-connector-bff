import codecs
import json
from enum import Enum


class SquadEnum(Enum):
    PARTS = 'PARTS'
    RWO = 'RWO'
    SALES = 'SALES'


class TrelloConfig(object):
    squadName = ''
    trelloBoardId = ''
    defaultListCardName = ''
    checkLists = []

    def __init__(self, squadName, trelloBoardId: str, defaultListCardName: str, checkLists: []):
        self.squadName = squadName
        self.trelloBoardId = trelloBoardId
        self.defaultListCardName = defaultListCardName
        self.checkLists = checkLists

    def addCheckList(self, checkList):
        self.checkLists.append(checkList)


class DataBase(object):
    trelloConfig = []

    def __init__(self, trelloConfig):
        self.trelloConfig = [TrelloConfig(**config) for config in trelloConfig]

    def getConfigBySquad(self, squadName):
        for config in self.trelloConfig:
            if config.squadName == squadName:
                return config

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)

    def save(self):
        with codecs.open("database.json", "w", encoding="utf-8") as save:
            save.write(self.toJson())


def connectDataBase():
    with open('database.json', 'r') as read:
        database_file = json.load(read)
        return DataBase(**database_file)
