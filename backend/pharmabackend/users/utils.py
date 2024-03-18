from pharmabackend.settings import URI_STRING
from mongoengine import connect


def connect_to_db(db_name):
    connect(host=URI_STRING + "/" + db_name)
