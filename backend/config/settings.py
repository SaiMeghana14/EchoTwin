from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):

    # Application

    app_name: str = "EchoTwin"
    environment: str = "development"
    debug: bool = True

    secret_key: str

    # Azure OpenAI

    azure_openai_endpoint: str
    azure_openai_api_key: str
    azure_openai_deployment: str

    # Azure AI Foundry

    azure_foundry_project: str
    azure_foundry_connection: str

    # Cosmos DB

    cosmos_endpoint: str
    cosmos_key: str
    cosmos_database: str

    # Blob Storage

    azure_storage_connection_string: str
    azure_storage_container: str

    # Speech

    azure_speech_key: str
    azure_speech_region: str

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
