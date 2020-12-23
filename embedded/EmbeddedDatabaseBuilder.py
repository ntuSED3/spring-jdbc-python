from embedded.EmbeddedDatabaseFactory import EmbeddedDatabaseFactory
from init.ResourceDatabasePopulator import ResourceDatabasePopulator
class EmbeddedDatabaseBuilder():
    def __init__(self):
        self.databaseFactory = EmbeddedDatabaseFactory()
        self.databasePopulator = ResourceDatabasePopulator()

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
    
    def addScript(self, script: str):
        self.databasePopulator.addScript(script)
        return self
    
    def addScripts(self, *argv: str):
        for arg in argv:
            self.addScript(arg)
        return self




