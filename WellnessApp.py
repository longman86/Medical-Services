import streamlit as st
import pandas as pd
from PIL import Image
import datetime as dt
import pyodbc

st.set_page_config(layout='wide')
image = Image.open("Pre-ScreeningHeader.png")
st.image(image, use_column_width=True)
st.title('AVON Pre Screening Medical Assessment Portal')


@st.experimental_memo(ttl = dt.timedelta(hours=24))
def get_data_from_sql(query):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};SERVER='
        +st.secrets['server']
        +';DATABASE='
        +st.secrets['database']
        +';UID='
        +st.secrets['username']
        +';PWD='
        +st.secrets['password']
        )
    df = pd.read_sql(query, conn)
    conn.close()
    return df
query = 'SELECT * from vw_wellness_enrollee'
wellness_df = get_data_from_sql(query=query)
#wellness_df = pd.read_csv('Wellness_Member_List.csv')
wellness_df['memberno'] = wellness_df['memberno'].astype(str)


enrollee_id = st.text_input('Kindly input your member number and press the enter key to confirm your eligibility')
enrollee_id = str(enrollee_id)


#def IsMemberEligible(enrollee_id):
#member_list = wellness_df.AvonoldEnrolleId.tolist()
if enrollee_id:
    if enrollee_id in wellness_df['memberno'].values:
        enrollee_name = wellness_df.loc[wellness_df['memberno'] == enrollee_id, 'membername'].values[0]
        st.balloons()
        st.info(f'Welcome {enrollee_name}.\n \n By clicking the link below, I understand and hereby acknowledge that my data would be collected and processed only for the performance of this wellness screening exercise.',icon="✅")
        st.write("[AVON Wellness Survey](https://forms.office.com/Pages/ResponsePage.aspx?id=y7xkPyIn5UK1ynGyBgRdhwThIjvb_VxNtMX-P8ytR_1UQ01ZRU05WFhERkRIQTVLRlZVUTNNSTcxMS4u)")
       
    elif enrollee_id not in wellness_df['memberno'].values:
        st.info('You are not eligible to participate, please contact your HR or Client Manager')
else:
    st.write('You must input your Member number to continue')

#st.write(IsMemberEligible(memberno))
image1 = Image.open('Pre-ScreeningBottom.png')
st.image(image1, use_column_width=True)
