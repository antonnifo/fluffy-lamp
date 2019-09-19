import os

import pymongo

from tests.integration.mongo_test_data import insert_many_data, insert_one_data, update_one_query, set_values

from mongo_abc import Mongo

CONNECTION_URL = os.getenv('CONNECTION_URL')

class MongoConfig(Mongo):

    def get_client(self, url=CONNECTION_URL):
        '''Get a Mongo Client Object used to create or use a database.
        
        Args:
            url (str, optional): a connection url with the correct ip address. Defaults to CONNECTION_URL.
        
        Returns:
            MongoClient Object.
        '''

        try:    
            my_client = pymongo.MongoClient(url)
            return my_client

        except:
            return "Unable to create MongoClient"

    def list_dbs(self,url=CONNECTION_URL):
        '''List all databases using the given ip address.
        
        Args:
            url (str, optional): a connection url with the correct ip address. Defaults to CONNECTION_URL.
        
        Returns:
            a list of databases using the given ip address.
        '''

        try:
            db_list = self.get_client(url).list_database_names()
            return db_list

        except:
            return "Unable to list databases"

    def use_db(self, database_name, url=CONNECTION_URL):
        '''Use a given database.
        
        Args:
            database_name (str): name of the database you want to use.
            url (str, optional): a connection url with the correct ip address. Defaults to CONNECTION_URL.
        
        Returns:
            a database object.
        '''

        try:
            client = self.get_client(url)
            my_db  = client[database_name]
            return my_db

        except:
            return "Unable to use database"    

    def use_collection(self, database_name, collection_name, url=CONNECTION_URL):
        '''Get a collection in a given database.
        
        Args:
            database_name (str): name of the database you want to use.
            collection_name (str): name of the collection you want to use.
        
        Returns:
            a collection object
        '''

        try:
            my_db  = self.use_db(database_name,url)
            my_col = my_db[collection_name]
            return my_col

        except:
            return "Unable to use collection"   

    def insert_one(self, database_name, collection_name, data, url=CONNECTION_URL):      
        '''Insert one document in the given collection.
        
        Args:
            database_name : name of the database with the collection to insert data.
            collection_name: name of collecton to insert data.
            data (dict): data to insert on the collection.
            url (str, optional): a connection url with the correct ip address. Defaults to CONNECTION_URL.
        
        Returns:
            insert one results object.
        '''
        try:

            results = self.use_collection(
                database_name, collection_name,url).insert_one(data)
            return results
        except:
            return "Unable to insert document"    

    def insert_many(self, database_name, collection_name, data, url=CONNECTION_URL):
        '''Insert many documents in the given collection.
        
        Args:
            database_name : name of the database with the collection to insert data.
            collection_name: name of collecton to insert data.
            data (list of dicts): data to insert on the collection.
            url (str, optional): a connection url with the correct ip address. Defaults to CONNECTION_URL.
        
        Returns:
            insert many results object.
        '''
        try:
            results = self.use_collection(
                database_name, collection_name,url).insert_many(data)
            return results
        except:
            return "Unable to insert more documents"

    def find_one(self, database_name, collection_name, url=CONNECTION_URL):
        '''Get the first occurance of a selection.
        
        Args:
            database_name (str): name of the database with the collection to search.
            collection_name (str): name of the collection to find document.
            url (str, optional): url with the ip address of mongo db. Defaults to CONNECTION_URL.
        
        Returns:
            document of the first occurance of a selection.
        '''

        try:
            my_col = self.use_collection(database_name, collection_name,url)
            results = my_col.find_one()
            return results
        except:
            return "Unable to find one document"    

    def find_many(self, database_name, collection_name, query={}, url=CONNECTION_URL):
        '''Get all the occurances of the selection.
        
        Args:
            database_name (str): name of the db with the collection.
            collection_name (str): name of the collection with the documents to be searched.
            query (dict, optional): query object specifying fields to include in the results.
                                    If omitted all fields will be included.
                                    Defaults to {}.
            url (str, optional): ip address of the mongo client. Defaults to CONNECTION_URL.
        
        Returns:
            list: contains all the documents sartisyfing the search.
                  It supports the container protocol.   
        '''

        try:
            my_col = self.use_collection(database_name, collection_name,url)
            results = my_col.find(query)
            return results

        except:
            "Unable to print documents"

    def update_one(self, database_name, collection_name, filter_, update, url=CONNECTION_URL):
        '''Update the value of a given document.If there are multiple occurances only
            the first one is updated.
        
        Args:
            database_name (str): name of the db that the collection with the data belongs to.
            collection_name (str): name of the collection data to be updated
            filter_ (object): defines which document to update.
            update (object): new values of the document.
        '''
        try:
            my_col = self.use_collection(database_name, collection_name,url)
            my_col.update_one(filter_, update)
        except:
            return 'Unable to update document'    
               
    def update_many(self, database_name, collection_name, filter_, update, url=CONNECTION_URL):
        '''Update all documents that meets a criteria specified in the query.
        
        Args:
            database_name (str): name of the db that the collection with the data belongs to.
            collection_name (str): name of the collection data to be updated
            filter (object): defines which document to update.
            update (object): new values of the document.
        '''
        try:
            my_col = self.use_collection(database_name, collection_name, url)
            my_col.update_many(filter_ , update)
        except:
            return "Unable to update the documents"

    def delete_one(self, database_name, collection_name, query):

        try:
            my_col = self.use_collection(database_name, collection_name)
            my_col.delete_one(query)
        except:
            return "Unable to delete document"    

    def delete_many(self, database_name, collection_name, query):

        try:
            my_col = self.use_collection(database_name, collection_name)
            my_col.delete_many(query)
        except:
            return "Unable to delete documents"    


if __name__ == "__main__":
    
    mongo = MongoConfig()
    # print(mongo.get_client())
    # print(mongo.list_dbs())
    # print(mongo.use_db('my_database'))
    # print(mongo.use_collection('my_database','customers'))
    # print(mongo.insert_one('my_database','customers',insert_one_data))
    # print(mongo.insert_many('my_database','customers',insert_many_data))
    # print(mongo.find_one('my_database','customers'))
    customers = mongo.find_many('my_database','customers')
    for customer in customers:
        print(customer)
    # print(mongo.update_one('my_database', 'customers', update_one_query, set_values))
  

