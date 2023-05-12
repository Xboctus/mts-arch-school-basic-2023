import json, os
from pymongo import MongoClient

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Making Connection
myclient = MongoClient("mongodb://"+DB_USER+":"+DB_PASSWORD+"@"+DB_HOST+":"+DB_PORT+"/?authMechanism=DEFAULT")

# database
db = myclient[DB_USER]

print(db)

list_of_collections = db.list_collection_names()

print(list_of_collections)

# Re-initialize authors
if "authors" in db.list_collection_names():
    authors = db['authors']
    authors.drop()

db.create_collection("authors")

# Re-initialize presentation
if "presentations" in db.list_collection_names():
    presentations = db['presentations']
    presentations.drop()

db.create_collection("presentations")

# Prepare authors
authors = db['authors']

# Loading or Opening the json file
with open('ExportJson.json') as file:
    file_data = json.load(file)

i=1
for data in file_data:
    data["author_id"] = i
    i += 1

# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
if isinstance(file_data, list):
    authors.insert_many(file_data)
else:
    authors.insert_one(file_data)