# Criminal Analysis System and Management
### Once you download the zip file and have completed the extraction process
### you can run the script by opening a terminal or command prompt in the current folder "Project" folder

## Step - 1:
Enable the Virtual Environment by running the below command:
Git Bash terminal:
`
    source myenv/Scripts/Activate
`

## Step - 2:
- As the required python dependencies of the project are already installed in the virtual environment, there is no need to install any packages.
- Make sure you have MongoDB installed in your system.
- To connect to MongoDB client, go to database.py file and edit the below given line:

line 5 in App/database.py:
`
client = MongoClient('mongodb://localhost:27017/')
`
edit the link to the link in your mongodb server.

## Step - 3:
- Make sure to create a database called CriminalDB in your mongodb connection.
- to fill in the database, run the App/fill_db.py file.

## Step - 4:
- To run the application, run the App/main.py file.
