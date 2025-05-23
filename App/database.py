
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Connect to the database
db = client['CriminalDB']

# Create collection handles
users = db['Users']
criminals = db['Criminals']
crimes = db['Crimes']
stations = db['Stations'] 
prisons = db['Prisons']
crime_records = db['CrimeRecords']
investigator = db['Investigators']
victims = db['Victims']
witnesses = db['Witnesses']
court_cases = db['CourtCases']
court_trials = db['CourtTrials']

collections = {
            "Criminals": criminals,
            "Crimes": crimes,
            "Stations": stations,
            "Prisons": prisons,
            "CrimeRecords": crime_records,
            "Investigators": investigator,
            "Victims": victims,
            "Witnesses": witnesses,
            "CourtCases": court_cases,
            "CourtTrials": court_trials
}

# CREATE
def create_document(collection, document):
    result = collection.insert_one(document)
    return result.inserted_id

def insert_manydocs(collection, documents: list):
    result = collection.insert_many(documents)
    return result

# READ 
def read_documents(collection, query={}):
    return list(collection.find(query))

def read_document_by_id(collection, doc_id):
    return collection.find_one({"_id": doc_id})

# UPDATE
def update_document(collection, query, new_values):
    return collection.update_one(query, new_values)


# DELETE
def delete_document(collection, doc_id):
    result = collection.delete_one({"_id": doc_id})
    return result.deleted_count
