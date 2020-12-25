import uuid
from .EmbeddedDatabaseConfigurerFactory import EmbeddedDatabaseConfigurerFactory
from .JaydebeDataSourceFactory import JaydebeDataSourceFactory
from .JaydebeDataSource import JaydebeDataSource
from .EmbeddedDatabaseType import EmbeddedDatabaseType
from .EmbeddedDatabase import EmbeddedDatabase


class EmbeddedDatabaseFactory():
    def __init__(self):
        self.databaseName = "testdb"
        self.dataSource = None
        self.databaseConfigurer = None

        self.dataSourceFactory = JaydebeDataSourceFactory()
        self.generateUniqueDatabaseName = False

        self.logInfoEnabled = False


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

    def setLogInfoEnabled(self, flag: bool):
        self.logInfoEnabled = flag

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
        return EmbeddedDatabaseProxy(self.dataSource, self)

    def shutdownDatabase(self):
        if self.dataSource is not None:
            if self.logInfoEnabled:
                if isinstance(self.dataSource, JaydebeDataSource):
                    print("Shutting down embedded database: url={}".format(
                        self.dataSource.getUrl()))
                else:
                    print("Shutting down embedded database {}".format(self.databaseName))
            if self.databaseConfigurer is not None:
                self.databaseConfigurer.shutdown(self.dataSource, self.databaseName)
            self.dataSource = None

class EmbeddedDatabaseProxy(EmbeddedDatabase):
    def __init__(self, ds, factory):
        self.dataSource = ds
        self.factory = factory

    def getConnection(self, username=None, password=None):
        return self.dataSource.getConnection(username=username, password=password)

    def shutdown(self):
        self.factory.shutdownDatabase()
