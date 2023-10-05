# Chat with your Database

This code is inspired from Ngonidzashe Nzenze [blog post](https://dev.to/ngonidzashe/chat-with-your-csv-visualize-your-data-with-langchain-and-streamlit-ej7).
But instead of CSV data, it is modified to connect to an MS SQL Database, and using Azure OpenAI.


## Running Locally
Pre-requisites:
- Install [Python](https://python.org)
- Install Python libraries `pip install -r requirements.txt`

Run `start.bat` or `streamlit run app/Hello.py`


## Deploy to Azure
[![Deploy To Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fraffertyuy%2Fdbcopilot-langchain-streamlit%2Fmain%2Fazuredeploy.json)

## Other Files
To keep this repo clean, and for my own organization, I opted to not place any extra files onto this repo.
My Jupyter notebooks and the sample database that I'm using are in [RazGPT](https://github.com/raffertyuy/RazGPT).