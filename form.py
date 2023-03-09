import streamlit as st
import datetime
st.title('R J Collage')
st.header('Master Form Application')
st.text_input('My First Name ')
st.text_input('My Last Name ')
st.text_input('My Father Name ')
st.text_input('My Mother Name ')
st.text('Qualification ')
st.radio('Gender',('Male','Female','trance','Other'))
st.checkbox('SSC')
st.checkbox('HSC')
st.checkbox('BSC')
st.checkbox('MSC')
st.checkbox('Phd')
st.text_area('Enter Your SOP',max_chars = 200)
st.date_input('DOB',datetime.date(2023,3,2))
st.write('Your Date Of Birth')
b = st.button('submit')
if(b):
    st.warning('your form is submited')
    st.header('your filled information is follows')



