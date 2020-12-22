from embedded.EmbeddedDatabaseFactory import EmbeddedDatabaseFactory

class EmbeddedDatabaseBuilder():
    def __init__(self):
        self.databaseFactory = EmbeddedDatabaseFactory()

    def generateUniqueName(self, flag: bool):
        self.databaseFactory.setGenerateUniqueDatabaseName(flag)
        return self
    
    def setType(self, databaseType):
        self.databaseFactory.setDatabaseType(databaseType)
        return self
    
    def setDataSourceFactory(self, dataSourceFactory):
        self.databaseFactory.setDataSourceFactory(dataSourceFactory)
        return self
    
    def build(self):
        return self.databaseFactory.getDatabase()




