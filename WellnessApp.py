import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(layout='wide')
image = Image.open("Pre-ScreeningHeader.png")
st.image(image, use_column_width=True)
st.title('AVON Pre Screening Medical Assessment Portal')


#url = "https://raw.githubusercontent.com/longman86/Avon-Wellness-Survey/main/Member_Wellness.csv" # Make sure the url is the raw version of the file on GitHub
#download = requests.get(url).content
#wellness_df = pd.read_csv(io.StringIO(download.decode('utf-8')))
#path = r'C:\Users\ademola.atolagbe\Documents\Medical_Services\Member_Wellness.csv'
#path = 'https://avonhealthcareltd-my.sharepoint.com/personal/droguguah_ejinkeonye_avonhealthcare_com/Documents/Documents/Wellness%20member%20list.xlsx?web=1'
wellness_df = pd.read_csv('Wellness_Member_List.csv')
wellness_df['MemberNo'] = wellness_df['MemberNo'].astype(str)


enrollee_id = st.text_input('Kindly input your member number and press the enter key to confirm your eligibility')
enrollee_id = str(enrollee_id)


#def IsMemberEligible(enrollee_id):
#member_list = wellness_df.AvonoldEnrolleId.tolist()
if enrollee_id:
    if enrollee_id in wellness_df['MemberNo'].values:
        enrollee_name = wellness_df.loc[wellness_df['MemberNo'] == enrollee_id, 'membername'].values[0]
        st.balloons()
        st.info(f'Welcome {enrollee_name}.\n \n By clicking the link below I hereby give the scheme authorisation to the information I have provided.I understand and accept that the above authorisation constitutes a waiver of my right to privacy.',icon="✅")
        st.write("[AVON Wellness Survey](https://forms.office.com/Pages/ResponsePage.aspx?id=y7xkPyIn5UK1ynGyBgRdhwThIjvb_VxNtMX-P8ytR_1UQ01ZRU05WFhERkRIQTVLRlZVUTNNSTcxMS4u)")
       
    elif enrollee_id not in wellness_df['MemberNo'].values:
        st.info('You are not eligible to participate, please contact your HR or Client Manager')
else:
    st.write('You must input your Member number to continue')

#st.write(IsMemberEligible(memberno))
image1 = Image.open('Pre-ScreeningBottom.png')
st.image(image1, use_column_width=True)
