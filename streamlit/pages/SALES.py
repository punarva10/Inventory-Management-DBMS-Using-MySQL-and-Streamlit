import streamlit as st
from database import get_parts, update_ng2

st.title('Invento by BTPL')

operator = st.text_input('ENTER YOUR NAME')

parts = get_parts()
my_parts = ['']
for i in parts:
    my_parts.append(i[0])
part = st.selectbox('SELECT PART', my_parts)

value = st.number_input('ENTER NUMBER OF DEFECTIVE PARTS: (NG2)', min_value = 0, step = 1)

if st.button('Enter'):
    n = update_ng2(part, value)
    st.write(n)