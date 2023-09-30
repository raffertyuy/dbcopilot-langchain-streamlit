import os
from dotenv import load_dotenv

import streamlit as st
import pandas as pd

from langchain.llms import AzureOpenAI

from utilities.DataFrameAgent import DataFrameAgent
import utilities.Common as Common

st.set_page_config(
    page_title="DB Copilot - CSV Agent | RazType",
    page_icon="📝")


load_dotenv()

COMPLETION_MODEL = os.environ["OPENAI_COMPLETION_MODEL"]
COMPLETION_DEPLOYMENT = os.environ["OPENAI_COMPLETION_DEPLOYMENT"]
OPENAI_API_VERSION = os.environ["OPENAI_API_VERSION"]
OPENAI_TEMPERATURE = float(os.environ["OPENAI_TEMPERATURE"])

llm = AzureOpenAI(
    model_name=COMPLETION_MODEL,
    deployment_name=COMPLETION_DEPLOYMENT,
    temperature=OPENAI_TEMPERATURE,
    verbose=True
)

# Streamlit App
st.title("📝 Chat with your CSV Data using the LangChain Pandas DataFrame Agent")
st.write("Query your data using natural language and output the results as a table, bar chart, line chart, or a plain answer.")
st.caption("The [here](https://github.com/raffertyuy/RazGPT/tree/main/sampledata) for sample CSV files.")

filename = st.file_uploader("Step 1: Upload CSV")
if filename is not None:
    df = pd.read_csv(filename)
    st.dataframe(df)
    
    query = st.text_area("Step 2: Ask your Data", key="textDataCsv")
    if st.button("Submit Query", key="submitCsvQuery", type="primary"):
        agent = DataFrameAgent(llm=llm, df=df, verbose=True)

        response = agent.Query(query=query)
        decodedResponse = Common.DecodeResponse(response)
        Common.WriteResponse(decodedResponse)