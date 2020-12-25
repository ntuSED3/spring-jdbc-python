import jaydebeapi
import threading
from ..datasource.AbstractDriverBasedDataSource import AbstractDriverBasedDataSource

class JaydebeDataSource(AbstractDriverBasedDataSource):
    """	
    SimpleDriverDataSource
    """
    #-----------------------------------------------------------------------------------
    # hard-coded jar used for JDBC connection,
    # because `jaydebeapi` needs all jars set at once for multiple connection calls
    # see: [jaydebeapi github issue #1](https://github.com/baztian/jaydebeapi/issues/1)
    #-----------------------------------------------------------------------------------
    jar_list = [
        "database/embedded/jar/h2-1.4.200.jar",
        "database/embedded/jar/hsqldb.jar",
        "database/embedded/jar/derby.jar",
    ]
    def __init__(self):
        super().__init__()
        self.jclassname = None

    def getConnectionFromDriver(self, username=None, password=None):
        #print("connecting vai jaydebeapi:")
        #print("\turl\t", self.url)
        #print("\tjclassname\t", self.jclassname)
        return jaydebeapi.connect(
                self.jclassname,
                self.url,
                [username, password],
                self.jar_list)
	
    def setJClassName(self, name):
        self.jclassname = name
    def getJClassName(self):
        return self.jclassname
