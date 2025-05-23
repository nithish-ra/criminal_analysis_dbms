from pymongo import MongoClient

# Connect to local MongoDB (default)
client = MongoClient('mongodb://localhost:27017/')

# Or connect to MongoDB Atlas (cloud)
# client = MongoClient('your_connection_string')
db = client['db']            # Create or access a database
collection = db['emp']      # Create or access a collection (table)

user = db['user']
user.insert_one({"name": "John", "username": "john123", "password": "jxhn23"})

for doc in user.find():
    print(doc)

'''
# Insert one document
collection.insert_one({"name": "Siddharth", "age": 21})

# Insert multiple documents
collection.insert_many([
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30}
])
'''
# Find one
print(collection.find_one({"name": "Siddharth"}))

collection.delete_one({"name": "Alice"})
# Find all
for doc in collection.find():
    print(doc)

collection.delete_one({"name": "Alice"})

