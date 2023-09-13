
from pymongo.mongo_client import MongoClient
import pandas as pd 
import json 

uri = "mongodb+srv://shaikhaadil:shaikhaadil@cluster0.d8v3kti.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
COLLECTION_NAME="waferfault"

# create database name and collection name 
DATABASE_NAME="DATA1"

# read the data as a dataframe
df=pd.read(r"E:\Projects\Wafer_Fault_Detection\notebooks\wafer_23012020_041211.csv")
df=df.drop("unnamed: 0", axis=1)

# convert the data into json
json_record==list(json.loads(df.T.to_json()).values())

# now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME]=json_record
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)