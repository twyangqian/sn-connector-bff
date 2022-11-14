import json
from enum import Enum


class SquadEnum(Enum):
    PARTS = 'PARTS'
    RWO = 'RWO'
    SALES = 'SALES'


class TrelloConfig(object):
    squad = ''
    trelloBoardId = ''
    defaultListCardName = ''
    trelloConfigCheckLists = []

    def __init__(self, squad, trelloBoardId: str, defaultListCardName: str, trelloConfigCheckLists: []):
        self.squad = squad
        self.trelloBoardId = trelloBoardId
        self.defaultListCardName = defaultListCardName
        self.trelloConfigCheckLists = [TrelloConfigCheckList(**checkList) for checkList in trelloConfigCheckLists]

    def addCheckList(self, checkList):
        self.trelloConfigCheckLists.append(checkList)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)


class TrelloConfigCheckList(object):
    checkListName = ''

    def __init__(self, checkListName: str):
        self.checkListName = checkListName
