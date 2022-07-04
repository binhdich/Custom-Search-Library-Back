from azure.cosmos import CosmosClient, PartitionKey, exceptions


class dbConnector:

    url_db = 'https://dhbw-kino-free-tier.documents.azure.com:443/'
    key = '1Q5eHluC5jsQ8VmRDTE7TsPoJenlCSlfkkWt8zuxpaOCdYOy0hwkQVYfNAdDU5jH9fzmZraUwHTRnYRPtJ5GPA=='
    client = CosmosClient(url_db, credential=key)

    database_name = 'dhbw-kino-free-tier'
    database = client.get_database_client(database_name)
   

    def create_container(self, container_name):
        try:
            container = self.database.create_container(id=container_name, partition_key=PartitionKey(path="/url"))
        except exceptions.CosmosResourceExistsError:
            container = self.database.get_container_client(container_name)
        except exceptions.CosmosHttpResponseError:
            raise
        return container

