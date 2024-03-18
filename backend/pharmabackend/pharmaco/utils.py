from pharmabackend.settings import URI_STRING, DB_NAME
from contextlib import contextmanager
from mongoengine import connect, disconnect

@contextmanager
def connect_to_db(db_name):
    try:
        # Connect to MongoDB
        connect(host=URI_STRING + "/" + DB_NAME)
        yield
    finally:
        # Disconnect from MongoDB
        disconnect(db_name)