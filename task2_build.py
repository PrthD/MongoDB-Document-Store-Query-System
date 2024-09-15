import sys
import json
import time
from pymongo import MongoClient

def loadSendersToMemory():
    """
    Purpose: Load all sender information into memory from "senders.json"
    Return: Dictionary with sender_id as keys and sender information as values
    """
    senders_dict = {}
    with open("senders.json", 'r', encoding='utf-8') as file:
        senders_data = json.load(file)
        for sender in senders_data:
            senders_dict[sender['sender_id']] = sender
    return senders_dict

def enrichAndInsertMessages(messages_collection, senders_dict):
    """
    Purpose: Read messages.json, enrich each message with sender information from memory,
             and insert by small batches into the "messages" collection
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
            message = json.loads(cur_line)
            # Enrich message with sender information
            sender_info = senders_dict.get(message['sender'])
            if sender_info:
                message['sender_info'] = sender_info
            batch.append(message)
            if len(batch) == 5000:  # 5k messages per read
                messages_collection.insert_many(batch)
                batch = []
    if batch:
        messages_collection.insert_many(batch)
        del batch
    end = time.time()
    time_taken = end - start
    return time_taken

def main(portNumber):
    client = MongoClient("localhost", portNumber)
    # Create/Open database
    db = client["MP2Embd"]

    # Load sender information into memory
    senders_dict = loadSendersToMemory()

    # Check if "messages" collection exists. If it does, drop it and create new
    col_list = db.list_collection_names()
    if "messages" in col_list:
        db["messages"].drop()
    messages_collection = db["messages"]

    # Enrich messages with sender information and insert into the database
    time_load_messages = enrichAndInsertMessages(messages_collection, senders_dict)

    # Print the time taken by the operation
    print(f"Runtime for embedding sender information and loading messages: {time_load_messages} seconds")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 task2_build.py <portNumber>")
        sys.exit(1)

    portNumber = int(sys.argv[1])
    main(portNumber)