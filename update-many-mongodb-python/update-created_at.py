from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/") # Connect to the MongoDB server instance
db = client["db_name"] # Update the database name
collection = db['collection_name']  # Update the collection name

# Create the update query
update_query = {
    'created_at': {'$exists': False}
}

update_data = {
    '$set': {
        'created_at': datetime(2023, 11, 29, 0, 0, 0)
    }
}

# Perform the document update
result = collection.update_many(update_query, update_data)

# Print the number of updated documents
print(f'{result.modified_count} documents updated.')

# Close the MongoDB connection
client.close()
