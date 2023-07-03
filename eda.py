import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # visualization
import streamlit as st # web app framework
from ydata_profiling import ProfileReport # ydata EDA library
from streamlit_pandas_profiling import st_profile_report # EDA library
# title
st.markdown(''' 
# **The EDA App** 
This is the **EDA App** created in Streamlit using the **ydata** and **streamlit-pandas-profiling** libraries. 
''') 
# file upload
with st.sidebar.header('1. Upload data in CSV format'): # sidebar
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"]) # file upload
   
   
# Pandas Profiling Report
if uploaded_file is not None: # if file is uploaded
    @st.cache_resource # cache the uploaded file
    def load_csv(): # function to load csv
        csv = pd.read_csv(uploaded_file) # read csv
        return csv # return csv
    df = load_csv() # call load_csv() function
    pr = ProfileReport(df, explorative=True) # pandas profiling
    st.header('**Input DataFrame**') # title
    st.write(df) # write DataFrame
    st.write('---') # separator
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else: # if no file is uploaded
    st.info('Awaiting for CSV file to be uploaded.') # if no file is uploaded
    if st.button('Press to use Example Dataset'): # button to use example dataset
        # example dataset function
        @st.cache_resource # cache the function
        def load_data():
            a = sns.load_dataset('iris') # load iris dataset
            return a # return DataFrame
        df = load_data() # call load_data() function
        pr = ProfileReport(df, explorative=True) # pandas profiling
        st.header('**Input DataFrame**') # title 
        st.write(df.head()) # write DataFrame head (default 5)
        st.write('---') # separator
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)