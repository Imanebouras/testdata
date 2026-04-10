import streamlit as st

# Set the title of the app
st.title('Lead Generation Tool')

# Upload CSV file
uploaded_file = st.file_uploader('Upload CSV with Google Maps Links', type='csv')
if uploaded_file:
    st.success('File uploaded successfully!')