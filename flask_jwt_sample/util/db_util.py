from bson.objectid import ObjectId
from pymongo import MongoClient

mongo_client = MongoClient('localhost', 27017)


def connect():
    """
    :return: the mongo database this project.
    """
    return mongo_client['flask_jwt_sample']


def get(collection, data_filter):
    """
    Get one or more document registers.
    :param collection: The mongodb collection.
    :param data_filter: The params to filter.
    :return: The filtered document.
    """
    filtered_documents = collection.find(data_filter)
    print 'Get/Filter document into the ' + collection.name + ' collection.'
    return filtered_documents


def get_one(collection, data_filter):
    """
    Get one document register.
    :param collection: The mongodb collection.
    :param data_filter: The params to filter.
    :return: The filtered document.
    """
    filtered_document = collection.find_one(data_filter)
    print 'Get/Filter document into the ' + collection.name + ' collection.'
    return filtered_document


def get_by_id(collection, document_id):
    """
    Get one documents's registers.
    :param collection: The mongodb collection.
    :param document_id: The document id
    :return: The filtered document
    """
    filtered_collection = collection.find_one({'_id': ObjectId(document_id)})
    print "Get/Filter documents into the " + collection.name + " collection."
    return filtered_collection


def save(collection, data):
    """
    Save data in specific collection.
    :param collection: The mongodb collection.
    :param data: The data to be added in collection.
    :return: The id object collection.
    """
    saved = collection.insert_one(data)
    print 'Inserted a document into the ' + collection.name + ' collection.'
    return saved.inserted_id
