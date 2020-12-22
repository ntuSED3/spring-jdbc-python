import jaydebeapi
from AbstractDriverBasedDataSource import AbstractDriverBasedDataSource

class JaydebeDataSource(AbstractDriverBasedDataSource):
    """	
    SimpleDriverDataSource
    """
    def __init__(self):
        self.url = None
        self.jar = None
        self.jclassname = None
        self.username = None
        self.password = None

    def getConnectionFromDriver(self, username=None, password=None):
        return jaydebeapi.connect(
                self.jclassname,
                self.url,
                [username, password],
                self.jar)

    def setUrl(self, url):
        self.url = url
	
    def setJarPath(self, jar):
        self.jar = jar
	
    def setJClassName(self, name):
        self.jclassname = name

    def setUserName(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password
