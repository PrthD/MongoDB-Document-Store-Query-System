import sys
import json
import time
from pymongo import MongoClient

def loadMessagesJSON(messages_collection):
    """
    Purpose: Read messages.json and insert the data by small batches into the "messages" collection
    Return: time of load (in seconds)
    """
    start = time.time()
    batch = []
    with open("messages.json", 'r', encoding='utf-8') as file:
        for line in file:
            cur_line = line.strip()
            if cur_line == "[" or cur_line == "]":
                continue
            cur_line = cur_line[:-1]  # Removing "," of each line
            if cur_line[-1] != "}":  # Edge case: last line's last char isn't a ","
                cur_line += "}"
            batch.append(json.loads(cur_line))
            if len(batch) == 5000:  # 5k messages per read
                messages_collection.insert_many(batch)
                batch = []
    if batch:
        messages_collection.insert_many(batch)
        del batch
    end = time.time()
    time_taken = end - start
    return time_taken

def loadSendersJSON(senders_collection):
    """
    Purpose: Read senders.json and insert data into the "senders" collection
    Return: time of load (in seconds)
    """
    start = time.time()
    with open("senders.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    senders_collection.insert_many(data)
    end = time.time()
    time_taken = end - start
    return time_taken

def main(portNumber):
    client = MongoClient("localhost", portNumber)
    # Create/Open database
    db = client["MP2Norm"]
    # Step 1:
    # Check if "messages" collection exists. If it does, drop it and create new
    col_list = db.list_collection_names()
    if "messages" in col_list:
        db["messages"].drop()
    # Create the "messages" collection and load json file
    messages_collection = db["messages"]
    time_load_messages = loadMessagesJSON(messages_collection)

    # Step 2:
    # Check if "senders" collection exists. If it does, drop it and create new
    if "senders" in col_list:
        db["senders"].drop()
    # Create the "senders" collection and load json file
    senders_collection = db["senders"]
    time_load_senders = loadSendersJSON(senders_collection)

    # Print the time taken by step 1 and step 2
    print(f"Runtime to read the data and create the messages collection (step 1): {time_load_messages} seconds")
    print(f"Runtime to read the data and create the senders collection (step 2): {time_load_senders} seconds")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 task1_build.py <portNumber>")
        sys.exit(1)

    portNumber = int(sys.argv[1])
    main(portNumber)