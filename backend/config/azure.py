from openai import AzureOpenAI

from backend.config.settings import settings


def get_azure_openai_client():

    client = AzureOpenAI(
        api_key=settings.azure_openai_api_key,
        api_version="2024-02-15-preview",
        azure_endpoint=settings.azure_openai_endpoint,
    )

    return client
