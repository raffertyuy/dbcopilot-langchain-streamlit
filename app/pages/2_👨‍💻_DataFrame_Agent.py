import streamlit as st

from util.SqlDbUtility import SqlDbUtility
from util.SqlAgent import SqlAgent
import util.Common as Common

st.set_page_config(
    page_title="DB Copilot - DataFrame Agent | RazType",
    page_icon="👨‍💻")

llm = Common.GetLlm()
dbutility = SqlDbUtility()
dbagent = SqlAgent(llm=llm, db=dbutility.db, verbose=True)

# Streamlit App
st.title("👨‍💻 Chat with your Data using SQL Stored Procedures and the LangChain Pandas DataFrame Agent")
st.write("Query your data using natural language and output the results as a table, bar chart, line chart, or a plain answer.")
st.caption("This app is using the [Northwind Traders](https://github.com/raffertyuy/RazGPT/tree/main/sampledata) sample database.")

st.header("**_🚧 NOTE: This feature is still under development. 🚧_**")
    
st.subheader("Step 1: Retrieve Data")
st.selectbox('Which data do you want to retrieve?', ('Customers', 'Orders', 'Products'))
st.write("DATA TABLE HERE")

st.divider()

st.subheader("Step 2: Ask your Data")
dataQuery = st.text_area("What do you want to ask?", key="textDataQuery")
if st.button("Submit Query", key="submitDataQuery", type="primary"):
    st.write("RESPONSE HERE")