import streamlit as st
from config import SquadEnum, connectDataBase, TrelloConfig
import pandas as pd

database = connectDataBase()

st.title('ServiceNow -> Trello Auto Sync Data')

# Using object notation
select_squad = st.sidebar.selectbox(
    "请选择Squad",
    (SquadEnum.PARTS.value, SquadEnum.RWO.value, SquadEnum.SALES.value)
)

select_squad_config = database.getConfigBySquad(select_squad)

if select_squad_config is None:
    select_squad_config = TrelloConfig(select_squad, '', '', [])
    database.trelloConfig.append(select_squad_config)

st.header('trello card配置')
st.subheader('配置trello board id')
trello_board_id = st.text_input('Trello board id', select_squad_config.trelloBoardId)
select_squad_config.trelloBoardId = trello_board_id

st.subheader('配置自定义创建card所在的列表名称（例如TODO）')
trello_card_default_list_card_name = st.text_input('Trello default list card name',
                                                   select_squad_config.defaultListCardName)
select_squad_config.defaultListCardName = trello_card_default_list_card_name

st.subheader('配置自定义创建card的checklist，多个用,分隔')
trello_card_check_lists = st.text_input('Trello card check lists', ','.join(select_squad_config.checkLists))
select_card_check_lists = st.multiselect('选择你需要创建的checklist，注意先后顺序', trello_card_check_lists.split(','),
                                         select_squad_config.checkLists)
select_squad_config.checkLists = select_card_check_lists

if st.button('保存配置'):
    database.save()
    st.write('保存成功')

st.header('数据展示')
df = pd.read_csv('./parts.csv')
st.write(df)


@st.experimental_memo
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


csv = convert_df(df)

st.download_button(
    "Press to Download",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
)
