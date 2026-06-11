import os

from dotenv import load_dotenv

from azure.ai.projects import AIProjectClient

from azure.identity import DefaultAzureCredential

load_dotenv()

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.getenv(
        "AZURE_PROJECT_CONNECTION_STRING"
    )
)
