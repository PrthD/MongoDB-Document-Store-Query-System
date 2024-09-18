# MongoDB Document Store Query System

## Project Overview
This project is designed to load and query data from JSON files into MongoDB collections, analyzing the impact of different document models (normalized vs. embedded) and indexing on query performance. The system is composed of four main scripts:

- **task1_build.py**: Builds a normalized document store with separate collections for messages and senders.
- **task2_build.py**: Builds an embedded document store with sender information embedded within each message document.
- **task1_query.py**: Executes and analyzes queries on the normalized document store.
- **task2_query.py**: Executes and analyzes queries on the embedded document store.

## Prerequisites
- Python 3.x
- MongoDB Server
- MongoDB Client (`mongosh`)
- `messages.json` and `senders.json` data files

## Setup Instructions

1. **Download Files**:
   - Clone the repository and download the following files into a single folder:
     - `task1_build.py`
     - `task2_build.py`
     - `task1_query.py`
     - `task2_query.py`
     - `messages_senders_JSON_zip.7z`
   - Extract the contents of messages_senders_JSON_zip.7z to obtain messages.json and senders.json.

2. **Initiate MongoDB Server**:
   - Create a data directory:
     ```bash
     mkdir ~/mongodb_data_folder
     ```
   - Start the MongoDB server:
     ```bash
     mongod --port <portNumber> --dbpath ~/mongodb_data_folder &
     ```

## Running the System

### 1. Task 1: Normalized Document Store

- **Build the Normalized Store**:
  Run the following command in the folder containing all files:
  ```bash
  python3 task1_build.py <portNumber>
- **Query the Normalized Store**:
  After building the normalized store, execute the query script:
  ```bash
  python3 task1_query.py <portNumber>

### 2. Task 2: Embedded Document Store

- **Build the Embedded Store**:
  Run the following command:
  ```bash
  python3 task2_build.py <portNumber>
- **Query the Embedded Store**:
  After building the embedded store, execute the query script:
  ```bash
  python3 task2_query.py <portNumber>

## Exploring the Database with MongoDB Client

### You can explore the MongoDB database using the MongoDB client:

- **Start the MongoDB client**:
  ```bash
  mongosh --port <portNumber>
- **Use the following commands to navigate and interact with the database**:
  - Open database:
    ```bash
    use DATABASE_NAME
    ```
  - List all databases:
    ```bash
    show dbs
    ```
  - Drop a database:
    ```bash
    db.dropDatabase()
    ```
  - Create a collection:
    ```bash
    db.createCollection("COLLECTION_NAME")
    ```
  - Drop a collection:
    ```bash
    db.COLLECTION_NAME.drop()
    ```
  - Query a collection:
    ```bash
    db.COLLECTION_NAME.find()
    ```

## Conclusion

This project provides a comparison between different MongoDB document models and demonstrates the performance impacts of normalized and embedded document stores when running queries. The results from this project can help in making informed decisions when designing MongoDB schemas for real-world applications.
