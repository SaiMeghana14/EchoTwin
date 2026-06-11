from azure.storage.blob import BlobServiceClient
from backend.config.settings import settings


class BlobStorageService:

    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(
            settings.azure_storage_connection_string
        )

        self.container = self.client.get_container_client(
            settings.azure_storage_container
        )

    def upload_file(self, file_name: str, data):

        blob_client = self.container.get_blob_client(file_name)

        blob_client.upload_blob(
            data,
            overwrite=True
        )

        return {
            "success": True,
            "file_name": file_name
        }

    def get_blob_url(self, file_name: str):

        blob_client = self.container.get_blob_client(file_name)

        return blob_client.url

    def delete_file(self, file_name: str):

        blob_client = self.container.get_blob_client(file_name)

        blob_client.delete_blob()

        return True


blob_service = BlobStorageService()
