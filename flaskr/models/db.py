# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient

# Provide the mongodb atlas url to connect python to mongodb using pymongo
client = MongoClient("mongodb://novacept:qhu5IVPqCjS3IQCI@ac-658ugvq-shard-00-00.wkfg1lx.mongodb.net:27017,"
                         "ac-658ugvq-shard-00-01.wkfg1lx.mongodb.net:27017,"
                         "ac-658ugvq-shard-00-02.wkfg1lx.mongodb.net:27017/?ssl=true&replicaSet=atlas-hg0dc7"
                         "-shard-0&authSource=admin&retryWrites=true&w=majority")


def get_db():
    # Create the database for our example (we will use the same database throughout the tutorial
    db = client.Panrange
    return db
