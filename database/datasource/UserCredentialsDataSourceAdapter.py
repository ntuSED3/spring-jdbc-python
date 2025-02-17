from .DelegatingDataSource import DelegatingDataSource

import threading

class UserCredentialsDataSourceAdapter (DelegatingDataSource):
    JdbcUserCredentials = threading.local()
    JdbcUserCredentials.username = None
    JdbcUserCredentials.password = None
    _username = None
    _password = None
    _catalog = None
    _schema = None

    def __init__(self, dataSource):
        super().setTargetDataSource(dataSource)
        pass

    def setUsername(self, username: str):
        self._username = username

    def setPassword(self, password: str):
        self._password = password

    def setCatalog(self, catalog: str):
        self._catalog = catalog

    def setCatalog(self, schema: str):
        self._schema = schema

    def setCredentialsForCurrentThread(self, username: str, password: str):
        self.JdbcUserCredentials.username = username
        self.JdbcUserCredentials.password = password

    def removeCredentialsFromCurrentThread(self):
        self.JdbcUserCredentials.username = None
        self.JdbcUserCredentials.password = None

    def getConnection(self, username=None, password=None):
        if username == None or password == None:
            con = self.doGetConnection(self.JdbcUserCredentials.username, self.JdbcUserCredentials.password) \
                    if self.JdbcUserCredentials.username is not None and self.JdbcUserCredentials.password is not None \
                    else self.doGetConnection(self._username, self._password)

            if (self._catalog is not None):
                con.setCatalog(self._catalog)

            if (self._schema is not None):
                con.setSchema(self._schema)
            return con
        else:
            return self.doGetConnection(username, password)

    def doGetConnection(self, username: str, password: str):
        assert super().getTargetDataSource() is not None
        if (username is not None):
            return super().getTargetDataSource().getConnection(username, password)
        else:
            return super().getTargetDataSource().getConnection()
