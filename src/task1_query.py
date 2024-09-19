import sys
import time
from pymongo import MongoClient, errors

def connect_to_db(portNumber):
    """ 
    Purpose: Connect to the database
    Return: database object
    """
    client = MongoClient("localhost", portNumber)
    db = client["MP2Norm"]
    return db

def query1(messages_collection):
    """ 
    Q1: Return the number of messages that have “ant” in their text.
    """
    start_time = time.time()
    try:   
        count = messages_collection.count_documents({"text": {"$regex": "ant"}}, maxTimeMS=120000) # 120000 milliseconds = 2 minutes
        print("Q1: The number of messages that have 'ant' in their text:", count)
    except errors.ExecutionTimeout:
        print("Q1: Time limit exceeded (2 minutes)")
    finally:
        end_time = time.time()
        print("Q1: Time needed to run the query:", end_time - start_time, "seconds, or", (end_time - start_time) * 1000, "milliseconds")

def query2(messages_collection):
    """ 
    Q2: Find the nickname/phone number of the sender who has sent the greatest number of messages.
    """
    start_time = time.time()
    try:
        result = messages_collection.aggregate([
            {"$group": {"_id": "$sender", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 1}
        ], maxTimeMS=120000).next()
        print("Q2: The sender who has sent the greatest number of messages is:", result["_id"], "with", result["count"], "messages")
    except errors.ExecutionTimeout:
        print("Q2: Time limit exceeded (2 minutes)")
    finally:
        end_time = time.time()
        print("Q2: Time needed to run the query:", end_time - start_time, "seconds, or", (end_time - start_time) * 1000, "milliseconds")
    
def query3(senders_collection):
    """
    Q3: Return the number of messages where the sender’s credit is 0.
    """
    start_time = time.time()
    try:
        result = senders_collection.aggregate([  # Pipeline
            {
                "$match": {   # Filters out only senders with credit = 0
                    "credit": 0
                }
            },
            {
                "$lookup": {   # Left join the senders with messages, creating a new field for each senders that has an array of all messages sent by that sender
                    "from": "messages",
                    "localField": "sender_id",
                    "foreignField": "sender",
                    "as": "messages_sent"
                }
            },
            {
                "$project": {   # Get the total messages sent of each sender by getting the length of the above mentioned array
                    "messages_sent_count": { "$size": "$messages_sent" }
                }
            }
            ,
            {
                "$group": {   # group by nothing, and get the total messages sent of all senders by summing the newly created "messages_sent_count" field in the $project part
                    "_id": None,
                    "total_count": { "$sum": "$messages_sent_count" }
                }
            }
        ], maxTimeMS=120000).next()
        print("Q3: Number of messages from senders with 0 credit:", result["total_count"])
    except errors.ExecutionTimeout:
        print("Q3: Time limit exceeded (2 minutes)")
    finally:
        end_time = time.time()
        print("Q3: Time needed to run the query:", end_time - start_time, "seconds, or", (end_time - start_time) * 1000, "milliseconds")

def query4(senders_collection):
    """
    Q4: Double the credit of all senders whose credit is less than 100.
    """
    start_time = time.time()
    try:
        result = senders_collection.update_many(
            {"credit": {"$lt": 100}},
            {"$mul": {"credit": 2}}
        )
    finally:
        end_time = time.time()
        print("Q4: Time needed to run the query:", end_time - start_time, "seconds, or", (end_time - start_time) * 1000, "milliseconds")

def create_indices(messages_collection, senders_collection):
    """
    Create indices for the collections
    """
    messages_collection.create_index("sender") # default index for "sender" 
    messages_collection.create_index([("text", "text")]) # text index for "text" field
    senders_collection.create_index("sender_id") # default index for "sender_id"

def main(portNumber):
    # connecting to the database
    db = connect_to_db(portNumber)
    
    # getting the collections
    messages_collection = db["messages"]
    senders_collection = db["senders"]

    # running the queries (step 3)
    query1(messages_collection)
    query2(messages_collection)
    query3(senders_collection)
    query4(senders_collection)

    # creating the indices and running queries 1-3 again (step 4)
    create_indices(messages_collection, senders_collection)
    print("Queries after creating indices:")
    query1(messages_collection)
    query2(messages_collection)
    query3(senders_collection)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 task1_query.py <port number>")
        sys.exit(1)

    portNumber = int(sys.argv[1])
    main = main(portNumber)
