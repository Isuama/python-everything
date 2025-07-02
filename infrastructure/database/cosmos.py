from azure.cosmos import CosmosClient, PartitionKey
from config import config

class CosmosDB:
    def __init__(self):
        url = config.COSMOS_ENDPOINT
        key = config.COSMOS_KEY
        database_name = config.COSMOS_DATABASE

        self.client = CosmosClient(url, credential=key)
        self.database = self.client.create_database_if_not_exists(id=database_name)

    def get_container(self, container_name: str, partition_key_path: str = "/id"):
        return self.database.create_container_if_not_exists(
            id=container_name,
            partition_key=PartitionKey(path=partition_key_path)
        )
