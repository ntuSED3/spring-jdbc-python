import uuid
from .EmbeddedDatabaseConfigurerFactory import EmbeddedDatabaseConfigurerFactory
from .JaydebeDataSourceFactory import JaydebeDataSourceFactory
from .EmbeddedDatabaseType import EmbeddedDatabaseType


class EmbeddedDatabaseFactory():
    def __init__(self):
        self.databaseName = "testdb"
        self.dataSource = None
        self.databaseConfigurer = None

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

    def setDatabaseType(self, embedded_type):
        self.databaseConfigurer = EmbeddedDatabaseConfigurerFactory.getConfigurer(embedded_type)

    def _initDatabase(self):
        if self.generateUniqueDatabaseName:
            self.setDatabaseName(str(uuid.uuid1()))

        if self.databaseConfigurer is None:
            self.databaseConfigurer = EmbeddedDatabaseConfigurerFactory \
                                       .getConfigurer(EmbeddedDatabaseType.HSQL)

        self.databaseConfigurer.configure(
                self.dataSourceFactory.getConnectionProperties(),
                self.databaseName)

        self.dataSource = self.dataSourceFactory.getDataSource()

    def getDatabase(self):
        if self.dataSource is None:
            self._initDatabase()
        return self.dataSource

