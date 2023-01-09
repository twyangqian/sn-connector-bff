import streamlit as st

from dto.trello_config import TrelloConfig, TrelloConfigCheckList
from enums.group import GroupEnum

from sn_connector_client import sn_connector_api
from parts.show_parts_report import show_open_ticket_report
import json

api = sn_connector_api()

st.title('ServiceNow -> Trello Auto Sync Data')

select_group = st.sidebar.selectbox(
    "请选择Group",
    (GroupEnum.PARTS.value, GroupEnum.RWO.value, GroupEnum.SALES.value, GroupEnum.ACCOUNTING.value,
     GroupEnum.WARRANTY.value, GroupEnum.WORKSHOP.value, GroupEnum.OPERATION.value, GroupEnum.ACCIDENT.value)
)

select_group_config_res = api.get_trello_config_by_group(select_group)
select_group_config = None

if select_group_config_res.status_code != 200:
    st.error('无法连接sn-connector，请重试')
else:
    trello_config_json = json.loads(select_group_config_res.text)
    select_group_config = TrelloConfig(**trello_config_json)

if select_group_config is None:
    select_group_config = TrelloConfig(select_group, '', '', [])

st.header('trello card配置')
st.subheader('配置trello board id')
trello_board_id = st.text_input('Trello board id', select_group_config.trelloBoardId)
select_group_config.trelloBoardId = trello_board_id

st.subheader('配置自定义创建card所在的列表名称（例如TODO）')
trello_card_default_list_card_name = st.text_input('Trello default list card name',
                                                   select_group_config.defaultListCardName)
select_group_config.defaultListCardName = trello_card_default_list_card_name

st.subheader('配置自定义创建card的checklist，多个用,分隔')
trello_card_check_lists = st.text_input('Trello card check lists', ','.join(
    [checkList.checkListName for checkList in select_group_config.trelloConfigCheckLists]))
select_card_check_lists = st.multiselect('选择你需要创建的checklist，注意先后顺序', trello_card_check_lists.split(','),
                                         [checkList.checkListName for checkList in
                                          select_group_config.trelloConfigCheckLists])
select_group_config.trelloConfigCheckLists = [TrelloConfigCheckList(checkList) for checkList in select_card_check_lists]

if st.button('保存配置'):
    api.create_or_update_trello_config(select_group_config)
    st.success('保存成功')

if select_group == GroupEnum.PARTS.value:
    show_open_ticket_report(api)
