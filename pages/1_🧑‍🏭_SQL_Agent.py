import os
from dotenv import load_dotenv
import streamlit as st

from langchain.llms import AzureOpenAI

from utilities.SqlDbUtility import SqlDbUtility
from utilities.SqlAgent import SqlAgent
import utilities.Common as Common

st.set_page_config(
    page_title="DB Copilot - SQL Agent | RazType",
    page_icon="🧑‍🏭")


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

dbutility = SqlDbUtility()
dbagent = SqlAgent(llm=llm, db=dbutility.db, verbose=True)

# Streamlit App
st.title("🧑‍🏭 Chat with your Data using the LangChain SQL Agent")
st.write("Query your data using natural language and output the results as a table, bar chart, line chart, or a plain answer.")
st.caption("This app is using the [Northwind Traders](https://github.com/raffertyuy/RazGPT/tree/main/sampledata) sample database.")

st.markdown("""> ⚠️**WARNING:** This is an experimental feature using LangChain agents.
> - retrieval of data may take a long time,
> - the results may not be accurate,
> - using this may cause issues to the database, please DO NOT use this in production.""")

st.caption("""Here are some sample queries:
- _List down the details of 5 customers._
- _Categorize the first 10 customers by their country and display in a bar chart._""")

agentQuery = st.text_area("What do you want to ask?", key="textAgentQuery")
if st.button("Submit Query", key="submitAgentQuery", type="primary"):
    agentResponse = dbagent.Query(query=agentQuery)

    decodedResponse = Common.DecodeResponse(agentResponse)
    Common.WriteResponse(decodedResponse)