import os
from dotenv import load_dotenv

import streamlit as st
import pandas as pd
import json
import re

from langchain.llms import AzureOpenAI

from SqlDbUtility import SqlDbUtility
from SqlAgent import SqlAgent

st.set_page_config(page_title="DB Copilot | RazType")

##########################################################################################
# Functions
##########################################################################################
def DecodeResponse(response: str) -> dict:
    """This function converts the string response from the model to a dictionary object.

    Args:
        response (str): response from the model

    Returns:
        dict: dictionary with response data
    """
    for i in range(5): # try 5 times
        try:
            result = json.loads(response)   # try to parse...
            return result
        except Exception as e:
            # "Expecting , delimiter: line 34 column 54 (char 1158)"
            # position of unexpected character after '"'
            unexp = int(re.findall(r'\(char (\d+)\)', str(e))[0])
            # position of unescaped '"' before that
            unesc = response.rfind(r'"', 0, unexp)
            response = response[:unesc] + r'\"' + response[unesc+1:]
            # position of correspondig closing '"' (+2 for inserted '\')
            closg = response.find(r'"', unesc + 2)
            response = response[:closg] + r'\"' + response[closg+1:]

    raise Exception("Failed to decode response after 5 attempts.")


def WriteResponse(response_dict: dict):
    """
    Write a response from an agent to a Streamlit app.

    Args:
        response_dict: The response from the agent.

    Returns:
        None.
    """

    # Check if the response is an answer.
    if "answer" in response_dict:
        st.write(response_dict["answer"])

    # Check if the response is a bar chart.
    if "bar" in response_dict:
        data = response_dict["bar"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        st.bar_chart(df)

    # Check if the response is a line chart.
    if "line" in response_dict:
        data = response_dict["line"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        st.line_chart(df)

    # Check if the response is a table.
    if "table" in response_dict:
        data = response_dict["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)


##########################################################################################
# App
##########################################################################################

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
st.title("👨‍💻 Chat with your Database")
st.write("Query your database using natural language and output the results as a table, bar chart, line chart, or a plain answer.")
st.caption("This app is using the [Northwind Traders](https://github.com/raffertyuy/RazGPT/tree/main/sampledata) sample database.")

tabAgent, tabSP = st.tabs(["🧑‍🏭 Agent (Experimental)", "📝 Stored Procedures"])

with tabAgent:
    st.header("Ask anything about your data")
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

        decodedResponse = DecodeResponse(agentResponse)
        WriteResponse(decodedResponse)


with tabSP:
    st.subheader("**_🚧 NOTE: This feature is still under development. 🚧_**")
    
    st.header("Step 1: Retrieve Data")
    st.selectbox('Which data do you want to retrieve?', ('Customers', 'Orders', 'Products'))
    st.write("DATA TABLE HERE")
    
    st.divider()
    
    st.header("Step 2: Ask your Data")
    dataQuery = st.text_area("What do you want to ask?", key="textDataQuery")
    if st.button("Submit Query", key="submitDataQuery", type="primary"):
        st.write("RESPONSE HERE")