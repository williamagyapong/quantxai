import streamlit as st

st.title("Data Analysis with PandasAI")

uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV file",
    type=['csv']
    )

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())
    st.write(data.shape)
