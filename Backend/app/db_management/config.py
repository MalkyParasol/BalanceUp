# config.py

# Default values
MONGODB_URI = "mongodb://localhost:27017"
DATABASE_NAME = "BalanceUp"

# Function to set MongoDB URI
def set_mongodb_uri(uri):
    global MONGODB_URI
    MONGODB_URI = uri

# Function to set database name
def set_database_name(name):
    global DATABASE_NAME
    DATABASE_NAME = name

# Function to get MongoDB URI
def get_mongodb_uri():
    return MONGODB_URI

# Function to get database name
def get_database_name():
    return DATABASE_NAME
