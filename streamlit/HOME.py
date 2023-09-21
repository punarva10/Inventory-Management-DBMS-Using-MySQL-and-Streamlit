import streamlit as st
from database import get_count, get_details

def main():
    st.title('INVENTO BY BTPL')
    menu = ["CURRENT PART COUNTS", "PART DETAILS"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "PART DETAILS":
        rows = get_details()
        st.dataframe(rows, width = 1000, height = 550)
        
    elif choice == "CURRENT PART COUNTS":
        rows = get_count()
        st.dataframe(rows, width = 1500)

if __name__ == '__main__':
    main()