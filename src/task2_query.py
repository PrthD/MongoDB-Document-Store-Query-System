import sys
import time
from pymongo import MongoClient, errors

def query1(messages_collection):
    """
    Q1: Return the number of messages that have “ant” in their text.
    """
    start_time = time.time()
    try:
        count = messages_collection.count_documents({"text": {"$regex": "ant"}}, maxTimeMS=120000)  # 120000 milliseconds = 2 minutes
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
        print("Q2: Sender with most messages:", result['_id'], "with", result['count'], "messages")
    except errors.ExecutionTimeout:
        print("Q2: Time limit exceeded (2 minutes)")
    finally:
        end_time = time.time()
        print("Q2: Time needed to run the query:", end_time - start_time, "seconds, or", (end_time - start_time) * 1000, "milliseconds")

def query3(messages_collection):
    """
    Q3: Return the number of messages where the sender’s credit is 0.
    """
    start_time = time.time()
    try:
        count = messages_collection.count_documents({"sender_info.credit": 0}, maxTimeMS=120000)
        print("Q3: Number of messages from senders with 0 credit:", count)
    except errors.ExecutionTimeout:
        print("Q3: Time limit exceeded (2 minutes)")
    finally:
        end_time = time.time()
        print("Q3: Time needed to run the query:", end_time - start_time, "seconds, or", (end_time - start_time) * 1000, "milliseconds")

def query4(messages_collection):
    """
    Q4: Double the credit of all senders whose credit is less than 100.
    """
    start_time = time.time()
    try:
        unique_senders = messages_collection.aggregate([
            {"$match": {"sender_info.credit": {"$lt": 100}}},
            {"$group": {"_id": "$sender_info.sender_id"}}
        ])

        sender_count = 0
        message_update_count = 0
        
        for sender in unique_senders:
            result = messages_collection.update_many(
                {"sender_info.sender_id": sender["_id"]},
                {"$mul": {"sender_info.credit": 2}}
            )
            sender_count += 1
            message_update_count += result.modified_count

    finally:
        end_time = time.time()
        print("Q4: Time needed to run the query:", end_time - start_time, "seconds, or", (end_time - start_time) * 1000, "milliseconds")

def main(portNumber):
    client = MongoClient("localhost", portNumber)
    db = client["MP2Embd"]
    messages_collection = db["messages"]

    query1(messages_collection)
    query2(messages_collection)
    query3(messages_collection)
    query4(messages_collection)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task2_query.py <portNumber>")
        sys.exit(1)

    portNumber = int(sys.argv[1])
    main(portNumber)