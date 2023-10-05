# Chat with your Database

This code is inspired from Ngonidzashe Nzenze [blog post](https://dev.to/ngonidzashe/chat-with-your-csv-visualize-your-data-with-langchain-and-streamlit-ej7).
But instead of CSV data, it is modified to connect to an MS SQL Database, and using Azure OpenAI.


## Running Locally
Pre-requisites:
- Install [Python](https://python.org)
- Install Python libraries `pip install -r requirements.txt`

Run `start.bat` or `streamlit run app/Hello.py`


## Deploy to Azure
> **WARNING**: This section is a work-in-progress. Followed these references but currently still not working:
> - https://benalexkeen.com/deploying-streamlit-applications-with-azure-app-services/
> - https://stackoverflow.com/questions/76807756/azure-app-service-unable-to-deploy-streamlit-app

1. [![Deploy To Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fraffertyuy%2Fdbcopilot-langchain-streamlit%2Fmain%2Fazuredeploy.json)
2. Update the **Configuration** of the deployed App Service
  - In General Settings, enable _Basic Auth Publishing_
  - In Application Settings, add the values in your .env variables
  - In Application Settings, add the following additional settings:
    - **ENABLE_ORYX_BUILD**: True
    - **SCM_DO_BUILD_DURING_DEPLOYMENT**: True

Here is an example of the App Service Configuration
```json
[
  {
    "name": "OPENAI_API_BASE",
    "value": "https://RESOURCE.openai.azure.com",
    "slotSetting": false
  },
  {
    "name": "OPENAI_API_KEY",
    "value": "",
    "slotSetting": false
  },
  {
    "name": "OPENAI_API_TYPE",
    "value": "azure",
    "slotSetting": false
  },
  {
    "name": "OPENAI_API_VERSION",
    "value": "2022-12-01",
    "slotSetting": false
  },
  {
    "name": "OPENAI_COMPLETION_DEPLOYMENT",
    "value": "davinci",
    "slotSetting": false
  },
  {
    "name": "OPENAI_COMPLETION_MODEL",
    "value": "text-davinci-003",
    "slotSetting": false
  },
  {
    "name": "OPENAI_TEMPERATURE",
    "value": "0.3",
    "slotSetting": false
  },
  {
    "name": "SQL_CONNECTIONSTRING_FORMAT",
    "value": "mssql+pymssql://{database_user}:{database_password}@{database_server}.database.windows.net:1433/{database_db}",
    "slotSetting": false
  },
  {
    "name": "SQL_DB_NAME",
    "value": "northwindtraders",
    "slotSetting": false
  },
  {
    "name": "SQL_DB_PASSWORD",
    "value": "",
    "slotSetting": false
  },
  {
    "name": "SQL_DB_SERVER_NAME",
    "value": "",
    "slotSetting": false
  },
  {
    "name": "SQL_DB_USER",
    "value": "",
    "slotSetting": false
  },
  {
    "name": "ENABLE_ORYX_BUILD",
    "value": "True",
    "slotSetting": false
  },
  {
    "name": "SCM_DO_BUILD_DURING_DEPLOYMENT",
    "value": "True",
    "slotSetting": false
  },
  {
    "name": "WEBSITE_HTTPLOGGING_RETENTION_DAYS",
    "value": "1",
    "slotSetting": false
  }
]
```


## Other Files
To keep this repo clean, and for my own organization, I opted to not place any extra files onto this repo.
My Jupyter notebooks and the sample database that I'm using are in [RazGPT](https://github.com/raffertyuy/RazGPT).