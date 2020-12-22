import jaydebeapi
from DataSource import DataSource

class JaydebeDataSource(DataSource):
    """	
    SimpleDriverDataSource
    AbstractDriverDataSource
    """
    def __init__(self):
        self.url = None
        self.jar = None
        self.jclassname = None
        self.username = None
        self.password = None

    def getConnection(self, username=None, password=None):
        if username is None: username = self.username
        if password is None: password = self.password
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
