import streamlit as st
import pandas as pd
import numpy as np
import os
import webbrowser
from PIL import Image

st.set_page_config(layout='wide')
image = Image.open('C:\\Users\\ademola.atolagbe\\Downloads\\Avon.jfif')
st.image(image, use_column_width=False)
st.title('AVON HMO Wellness Survey')



path = r'C:\Users\ademola.atolagbe\OneDrive - Avon Healthcare Ltd\Member Wellness.csv'
wellness_df = pd.read_csv(path)
link = 'https://forms.office.com/Pages/ResponsePage.aspx?id=y7xkPyIn5UK1ynGyBgRdh8-wGEk3Z51JtzuJQUW5THtUN0s5RVJQOFQ5R0swSktXSlQyWlBBUjFWUi4u&origin=Invitation&channel=1'
memberno = st.text_input('Kindly input your member number to confirm your eligibility')


def IsMemberEligible(enrollee_id):
    memberno = wellness_df.AvonoldEnrolleId.tolist()
    if enrollee_id in memberno:
        st.button('Open Wellness Survey')
        result = webbrowser.open_new_tab(link)

    else:
        result = 'You are not eligible to participate, please contact your HR or Client Manager'

    return result

st.write(IsMemberEligible(memberno))
