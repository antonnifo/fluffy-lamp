from abc import ABC, abstractmethod

class Cassandra(ABC):

    @abstractmethod
    def create_keyspace(self,keyspace_name,replication):
        pass

    @abstractmethod
    def list_keyspaces(self):
        pass

    @abstractmethod
    def drop_keyspace(self,keyspace_name):
        pass

    @abstractmethod
    def create_table(self,query):
        pass

    @abstractmethod
    def insert_into_table(self,table_name,columns,values):
        pass

    @abstractmethod
    def update_table(self,query):
        pass

    @abstractmethod
    def delete_row_data(self,table_name,condition):
        pass

    @abstractmethod
    def delete_column_data(self,column_name,table_name,condition):
        pass

    @abstractmethod
    def read_all_table(self,table_name):
        pass

    @abstractmethod
    def read_single_table(self,table_name,condition):
        pass

