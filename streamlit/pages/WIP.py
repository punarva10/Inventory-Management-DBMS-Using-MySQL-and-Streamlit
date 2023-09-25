import streamlit as st
from database import get_parts, update_wip
from datetime import datetime

st.title('Invento by BTPL')

operator = st.text_input('ENTER YOUR NAME')

machine_list = ['', 'M/C 01 DGP WINDSOR 80 TON', 
'M/C 02 ELECTRONICA 80 TON',
'M/C 03 ELECTORNICA ENDURA 120 TON',
'M/C 04 ELECTRONICA ENDURA 60 TON',
'M/C 05 HAITIAN 90',
'M/C 06 ELECTRONICA OPTIMA 75 TON',
'M/C 07 ELECTRONICA E140 SERVO 140 TON',
'M/C 08 MILICRON NOVA SERIES 140 TON',
'M/C 09 ELECTRONICA OPTIMA 75 TON',
'M/C 10 ELECTRONICA E110 SERVO 110 TON',
'M/C 11 ELECTRONICA E110 SERVO 110 TON',
'M/C 12 ELECTRONICA FUTURA 90 TON']
machine = st.selectbox('SELECT MACHINE', machine_list)

parts = get_parts()
my_parts = ['']
for i in parts:
    my_parts.append(i[0])
part = st.selectbox('SELECT PART', my_parts)

value = st.number_input('ENTER NUMBER OF PARTS PRODUCED:', min_value = 0, step = 1)

current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")

if st.button('Enter'):
    n = update_wip(part, value, current_date, operator, machine, current_time)