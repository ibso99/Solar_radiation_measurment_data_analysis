import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 

st.set_page_config(page_title="simple Dashboard", layout="wide")

st.header("Option 1: Upload your csv file and plot Data")
uploaded_file = st.file_uploader("Choose a csv file to upload", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader('Uploaded Data pre-view')
    st.dataframe(data.head())

    st.subheader("Graph of uploaded data")

    if st.checkbox("Show plot"):
        if data.shape[1] >= 2:
            x_col = st.selectbox('select x-axis column', data.columns)
            y_col = st.selectbox('select y-axis column', data.columns)
            
            fig, ax = plt.subplots(figsize=(8,2))
            ax.plot(data[x_col], data[y_col], marker='o', color='b')
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f'{x_col} vs {y_col}')
            st.pyplot(fig)
        else:
            st.warning('Uploaded data must have atleast two columns')
    else:
        st.warning("please upload the csv file")
