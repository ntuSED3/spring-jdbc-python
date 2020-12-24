import abc
from .DataSource import DataSource


class AbstractDriverBasedDataSource(DataSource):
    def __init__(self):
        self.url = None
        self.username = None
        self.password = None
    
    def setUrl(self,url):
        self.url = url
    def getUrl(self):
        return self.url
    
    def setUsername(self,username):
        self.username = username
    def getUsername(self):
        return self.username

    def setPassword(self,password):
        self.password = password
    def getPassword(self):
        return self.password
    
    def getConnection(self, username=None, password=None):
        if username == None:
            username = self.username
        if password == None:
            password = self.password
        return self.getConnectionFromDriver(username, password)
    
    @abc.abstractmethod
    def getConnectionFromDriver(self, username=None, password=None):
        raise NotImplementedError
