import streamlit as st
from database import get_part_track, get_details, get_fg_entry, get_sales_entry, get_wip_entry

def main():
    st.title('INVENTO BY BTPL')
    menu = ["CURRENT PART COUNTS", "PART DETAILS", "WIP ENTRY DETAILS", "FG ENTRY DETAILS", "SALES ENTRY DETAILS"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "PART DETAILS":
        rows = get_details()
        st.dataframe(rows, width = 1000, height = 550)
        
    elif choice == "CURRENT PART COUNTS":
        rows = get_part_track()
        st.dataframe(rows, width = 1500)
    
    elif choice == "WIP ENTRY DETAILS":
        rows = get_wip_entry()
        st.dataframe(rows, width = 2000)
    
    elif choice == "FG ENTRY DETAILS":
        rows = get_fg_entry()
        st.dataframe(rows, width = 1500)
    
    elif choice == "SALES ENTRY DETAILS":
        rows = get_sales_entry()
        st.dataframe(rows, width = 1500)

if __name__ == '__main__':
    main()