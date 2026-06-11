from azure.cosmos import CosmosClient
from backend.config.settings import settings


class CosmosDBService:

    def __init__(self):

        self.client = CosmosClient(
            settings.cosmos_endpoint,
            settings.cosmos_key
        )

        self.database = self.client.get_database_client(
            settings.cosmos_database
        )

    def get_container(self, container_name):

        return self.database.get_container_client(
            container_name
        )

    def create_item(self,
                    container_name,
                    item):

        container = self.get_container(
            container_name
        )

        return container.create_item(item)

    def get_item(self,
                 container_name,
                 item_id,
                 partition_key):

        container = self.get_container(
            container_name
        )

        return container.read_item(
            item=item_id,
            partition_key=partition_key
        )

    def query(self,
              container_name,
              query):

        container = self.get_container(
            container_name
        )

        return list(
            container.query_items(
                query=query,
                enable_cross_partition_query=True
            )
        )


cosmos_service = CosmosDBService()
