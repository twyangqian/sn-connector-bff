import json

import pandas as pd
import streamlit as st

from sn_connector_client import sn_connector_api


def show_open_ticket_report(api: sn_connector_api):
    st.header('报表')
    st.subheader('1.Daily Open Ticket Report')
    if st.button("生成报表"):
        with st.spinner('loading...'):
            report_res = api.get_parts_open_tickets_report()
            st.balloons()
            if report_res.status_code != 200:
                st.error('生成Daily Open Ticket Report失败！')
            else:
                st.dataframe(pd.DataFrame(data=json.loads(report_res.text)).fillna("待补充"))
                st.success('生成Daily Open Ticket Report成功！')
                st.download_button(
                    label="下载报表",
                    data=pd.DataFrame(data=json.loads(report_res.text)).fillna("待补充").to_csv().encode('utf-8'),
                    file_name='parts_report.csv',
                    mime='text/csv',
                )