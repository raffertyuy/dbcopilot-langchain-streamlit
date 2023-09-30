# Chat with your Database

This code is inspired from Ngonidzashe Nzenze [blog post](https://dev.to/ngonidzashe/chat-with-your-csv-visualize-your-data-with-langchain-and-streamlit-ej7).
But instead of CSV data, it is modified to connect to an MS SQL Database, and using Azure OpenAI.

This app is envisioned to grow. Here are the initial ideas:
- [x] Use LangChain SQL Agent
- [ ] Query DB stored procedures directly, and then use the LangChain panda dataframe agent.
- [ ] Use LangChain tools or OpenAI function calling to execute DB write operations


## Running Locally
Pre-requisites:
- Install [Python](https://python.org)
- Install Python libraries `pip install -r requirements.txt`

Run `start.bat` or `streamlit run Hello.py`

> Note: At this time, VS Code debugging is not working properly. If you know hot to fix `/.vscode/launch.json`, please submit a pull request!
> Possible fix [here](https://awesome-streamlit.readthedocs.io/en/latest/vscode.html)


## Other Files
To keep this repo clean, and for my own organization, I opted to not place any extra files onto this repo.
My Jupyter notebooks and the sample database that I'm using are in [RazGPT](https://github.com/raffertyuy/RazGPT).