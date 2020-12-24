import jaydebeapi
from ..datasource.AbstractDriverBasedDataSource import AbstractDriverBasedDataSource

class JaydebeDataSource(AbstractDriverBasedDataSource):
    """	
    SimpleDriverDataSource
    """
    def __init__(self):
        super().__init__()
        self.jar = None
        self.jclassname = None

    def getConnectionFromDriver(self, username=None, password=None):
        return jaydebeapi.connect(
                self.jclassname,
                self.url,
                [username, password],
                self.jar)

    def setJarPath(self, jar):
        self.jar = jar
    def getJarPath(self):
        return self.jar
	
    def setJClassName(self, name):
        self.jclassname = name
    def getJClassName(self):
        return self.jclassname
