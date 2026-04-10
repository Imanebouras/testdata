import streamlit as st
from lead_processor import process_leads

if __name__ == '__main__':
    st.title('Lead Generation Tool')
    st.write('Enter Google Maps links or manual entries:')
    user_input = st.text_area('Business Links')

    if st.button('Process Leads'):
        leads = process_leads(user_input)
        st.write(leads)
