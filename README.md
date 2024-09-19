
# MongoDB Document Store Query System

## Project Overview
This project is designed to load and query data from JSON files into MongoDB collections, analyzing the impact of different document models (normalized vs. embedded) and indexing on query performance. The system is composed of four main scripts:

- **task1_build.py**: Builds a normalized document store with separate collections for messages and senders.
- **task2_build.py**: Builds an embedded document store with sender information embedded within each message document.
- **task1_query.py**: Executes and analyzes queries on the normalized document store.
- **task2_query.py**: Executes and analyzes queries on the embedded document store.

## Project Structure

- **/src/**:
  - `task1_build.py`
  - `task2_build.py`
  - `task1_query.py`
  - `task2_query.py`
- **/resources/**
  - `messages_senders_JSON_zip.7z`
- `README.md`

## Prerequisites
- Python 3.x
- MongoDB Server
- MongoDB Client (`mongosh`)
- `messages.json` and `senders.json` data files (extracted from `/resources/messages_senders_JSON_zip.7z`)

## Setup Instructions

1. **Download Files**:
   - Clone the repository and navigate to the `/src/` and `/resources/` directories for required files.
     - `/src/` contains the Python scripts:
       - `task1_build.py`
       - `task2_build.py`
       - `task1_query.py`
       - `task2_query.py`
     - `/resources/` contains the compressed JSON files:
       - `messages_senders_JSON_zip.7z` (which contains `messages.json` and `senders.json`)
   - Extract the contents of `messages_senders_JSON_zip.7z` to obtain `messages.json` and `senders.json`.

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
  Run the following command in the `/src/` folder:
  ```bash
  python3 task1_build.py <portNumber>
  ```
- **Query the Normalized Store**:
  After building the normalized store, execute the query script:
  ```bash
  python3 task1_query.py <portNumber>
  ```

### 2. Task 2: Embedded Document Store

- **Build the Embedded Store**:
  Run the following command in the `/src/` folder:
  ```bash
  python3 task2_build.py <portNumber>
  ```
- **Query the Embedded Store**:
  After building the embedded store, execute the query script:
  ```bash
  python3 task2_query.py <portNumber>
  ```

## Exploring the Database with MongoDB Client

You can explore the MongoDB database using the MongoDB client:

- **Start the MongoDB client**:
  ```bash
  mongosh --port <portNumber>
  ```
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

This project demonstrates a comparison between normalized and embedded MongoDB document stores, highlighting the impact of document models and indexing on query performance. By examining the results from both approaches, this system provides valuable insights for designing MongoDB schemas for real-world applications.
