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
