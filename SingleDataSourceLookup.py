
from DataSourceLookup import DataSourceLookup

class SingleDataSourceLookup(DataSourceLookup):
    def __init__(self,dataSource=None):
        assert dataSource, "DataSource must not be null"
        self.dataSource = dataSource

    def getDataSource(self, dataSourceName):
        return self.dataSource