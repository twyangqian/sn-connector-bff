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
                columns = ['ticket', 'category', 'summary', 'description', 'ticket open date', 'owner', 'status']
                st.dataframe(pd.DataFrame(data=json.loads(report_res.text)))
                st.success('生成Daily Open Ticket Report成功！')
