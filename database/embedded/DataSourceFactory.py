class DataSourceFactory(object):
    def getConnectionProperties(self):
        raise NotImplementedError

    def getDataSource(self):
        raise NotImplementedError
