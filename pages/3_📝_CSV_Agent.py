import streamlit as st
import pandas as pd

from util.DataFrameAgent import DataFrameAgent
import util.Common as Common

st.set_page_config(
    page_title="DB Copilot - CSV Agent | RazType",
    page_icon="📝")


# Streamlit App
st.title("📝 Chat with your CSV Data using the LangChain Pandas DataFrame Agent")
st.write("Query your data using natural language and output the results as a table, bar chart, line chart, or a plain answer.")
st.caption("The [here](https://github.com/raffertyuy/RazGPT/tree/main/sampledata) for sample CSV files.")

st.caption("""Here are some sample queries for using [`books.csv`](https://github.com/raffertyuy/RazGPT/tree/main/sampledata):
- _Which book has the highest rating count?_
- _Tabulate the first 5 books. Include the title and the rating count columns only._
- _Create a bar graph on the first 5 books._
- _Create a line graph of the first 5 books._
""")

filename = st.file_uploader("Step 1: Upload CSV")
if filename is not None:
    df = pd.read_csv(filename)
    st.dataframe(df)
    
    query = st.text_area("Step 2: Ask your Data", key="textDataCsv")
    if st.button("Submit Query", key="submitCsvQuery", type="primary"):
        llm = Common.GetLlm()
        agent = DataFrameAgent(llm=llm, df=df, verbose=True)

        response = agent.Query(query=query)
        decodedResponse = Common.DecodeResponse(response)
        Common.WriteResponse(decodedResponse)