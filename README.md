[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Fozs_Okj)
# CMPUT 291 Mini Project 2 - Winter 2024  
Group member names and ccids  
* hetbhara, Het Bharatkumar Patel
* kjemhus, Nole Kjemhus
* dmhoang, Manh Duong Hoang
* pdadhani, Parth Dadhania

# Group work break-down strategy
* Manh Duong Hoang (SID:1753180): Implemented task1_build.py and query 3, 4 of task1_query.py. Reviewed others' code, partially filled out report file.  (Time spent: 2 days)
* Het Bharatkumar Patel (SID:1742431): Implemented parts of task2_build.py and task2_query.py. Reviewed others' code, partially filled out report file.  (Time spent: 4 days)
* Parth Dadhania (SID: 1722612): Implemented parts of task2_build.py & task2_query.py. Reviewed others' code, partially filled out report file.  (Time spent: 4 days)
* Nole Kjemhus (SID: 1742095): Implemented main, query 1, and query 2 of task1_query.py. Reviewed others' code, partially filled out report file.  (Time spent: 2 days)

Method of coordination to keep the project on track: Discord group chat + keeping track of each other.

# Code execution guide
> System Overview:
The system is designed to load and query data from JSON files into MongoDB collections, analyzing the impact of different document models and indexing on query performance. It consists of four main scripts:
1. task1_build.py: Builds a normalized document store with separate collections for messages and senders.
2. task2_build.py: Builds an embedded document store with sender information embedded within each message document.
3. task1_query.py: Executes and analyzes queries on the normalized document store.
4. task2_query.py: Executes and analyzes queries on the embedded document store.

> Setup:
1. Download all files from the github repository to a folder
2. In that same folder, copy in the messages.json file and senders.json file.
3. By now, you should have all these files in one folder (task1_build.py, task2_build.py, task1_query.py, task2_query.py, messages.json, senders.json)

> Initiate MongoDB Server:
1. Create a data directory: mkdir ~/mongodb_data_folder
2. Start MongoDB server: mongod --port portNumber --dbpath ~/mongodb_data_folder &

> To run task1:
1. In the command line, in the folder that includes all the files, the syntax to run the build file is:
python3 task1_build.py portNumber
Make sure you run task1_build.py before continuing. Next, we will run task1_query.py with the same portNumber, run:
python3 task1_query.py portNumber
2. To run task2:
In the command line, in the folder that includes all the files, the syntax to run the build file is:
python3 task2_build.py portNumber
Make sure you run task2_build.py before continuing. Next, we will run task2_query.py with the same portNumber, run:
python3 task1_query.py portNumber

> Explore Database using MongoDB client:
1. Run the client listening to the same port of server (make sure the server is running in the background): mongosh --port portNumber
2. Navigate the database using following commands:
     * Open database: use DATABASE_NAME
     * List databases: show dbs
     * Drop database: db.dropDatabase()
     * Create collection: db.createCollection(name, options)
     * Drop collection: db.COLLECTION_NAME.drop()
     * Query collection: db.COLLECTION_NAME.find()

# AI Agents
We have not used any AI tools for the completion of this project.

# Collaborations
We did not collaborate with anyone else to complete this project.
