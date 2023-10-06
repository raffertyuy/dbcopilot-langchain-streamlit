import streamlit as st

st.set_page_config(
    page_title="DB Copilot | RazType",
    page_icon="👨‍💻")

st.sidebar.success("Select a method above.")

st.title("👨‍💻 Chat with your Data")
st.write("Query your data using natural language and output the results as a table, bar chart, line chart, or as a plain answer.")
st.caption("The [code](https://github.com/raffertyuy/dbcopilot-langchain-streamlit) and [sample data](https://github.com/raffertyuy/RazGPT/tree/main/sampledata) used by this app are both in GitHub.")