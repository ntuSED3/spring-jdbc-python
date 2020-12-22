import uuid
from .EmbeddedDatabaseConfigurerFactory import EmbeddedDatabaseConfigurerFactory
from .JaydebeDataSourceFactory import JaydebeDataSourceFactory


class EmbeddedDatabaseFactory():
    def __init__(self):
        self.databaseName = "testdb"
        self.dataSource = None
        self.databaseConfigurer = EmbeddedDatabaseConfigurerFactory.getConfigurer("HSQL")
        self.dataSourceFactory = JaydebeDataSourceFactory()
        self.generateUniqueDatabaseName = False


    def setDatabaseName(self, name):
        self.databaseName = name

    def setDatabaseConfigurer(self, cnf):
        self.databaseConfigurer = cnf

    def setDataSourceFactory(self, factory):
        self.dataSourceFactory = factory

    def setGenerateUniqueDatabaseName(self, flag: bool):
        self.generateUniqueDatabaseName = flag

    def _initDatabase(self):
        if self.generateUniqueDatabaseName:
            self.setDatabaseName(str(uuid.uuid1()))

        self.databaseConfigurer.configure(
                self.dataSourceFactory.getConnectionProperties(),
                self.databaseName)

        self.dataSource = self.dataSourceFactory.getDataSource()

    def getDatabase(self):
        if self.dataSource is None:
            self._initDatabase()
        return self.dataSource

