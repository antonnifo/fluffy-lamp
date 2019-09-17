from abc import ABC, abstractmethod

class Mongo(ABC):

    @abstractmethod
    def get_client(self, url):
        pass

    @abstractmethod    
    def list_dbs(self):
        pass

    @abstractmethod
    def use_db(self,database_name):
        pass

    @abstractmethod
    def use_collection(self,database_name, collection_name):
        pass

    @abstractmethod
    def insert_one(self,database_name, collection_name,data):
        pass

    @abstractmethod
    def insert_many(self,database_name, collection_name,data):
        pass

    @abstractmethod
    def find_one(self,database_name, collection_name):
        pass

    @abstractmethod
    def find_many(self,database_name, collection_name,query={}):
        pass

    @abstractmethod
    def update_one(self,database_name, collection_name,query,new_values):
        pass

    @abstractmethod        
    def update_many(self,database_name, collection_name,query,new_values):
        pass

    @abstractmethod
    def delete_one(self,database_name, collection_name,query):
        pass

    @abstractmethod
    def delete_many(self,database_name, collection_name,query):
        pass
        