import streamlit as st
import pandas as pd
import json
import re

import os
from dotenv import load_dotenv
from langchain.schema.language_model import BaseLanguageModel
from langchain.llms import AzureOpenAI

@st.cache_data
def GetLlm() -> BaseLanguageModel:
    """
    Get the LangChain Language Model (LLM) from the session state.

    Args:
        None.

    Returns:
        BaseLanguageModel: The LangChain Base Language Model (LLM).
    """
    if 'llm' not in st.session_state:
        load_dotenv()

        COMPLETION_MODEL = os.environ["OPENAI_COMPLETION_MODEL"]
        COMPLETION_DEPLOYMENT = os.environ["OPENAI_COMPLETION_DEPLOYMENT"]
        OPENAI_API_VERSION = os.environ["OPENAI_API_VERSION"]
        OPENAI_TEMPERATURE = float(os.environ["OPENAI_TEMPERATURE"])

        st.session_state['llm'] = AzureOpenAI(
            model_name=COMPLETION_MODEL,
            deployment_name=COMPLETION_DEPLOYMENT,
            openai_api_version=OPENAI_API_VERSION,
            temperature=OPENAI_TEMPERATURE,
            verbose=True
        )
    
    return st.session_state['llm']


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

    raise Exception("Failed to decode response after 5 attempts.\n" + response + "\n")


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