from .DataSourceLookup import DataSourceLookup

class MapDataSourceLookup(DataSourceLookup):
    def __init__(self,dataSources=None,dataSourceName=None,dataSource=None):
        self.dataSources = {}
        if dataSources:
            self.setDataSources(dataSources)
        if dataSourceName and dataSource:
            assert dataSources==None, "DataSources must be None when both dataSourceName and dataSource are not None."
            self.addDataSource(dataSourceName,dataSource)
    
    def setDataSources(self,dataSources):
        if dataSources:
            self.dataSources = dataSources.copy()
    

    def getDataSources(self):
        return self.dataSources.copy()

    def addDataSource(self,dataSourceName=None,dataSource=None):
        assert dataSourceName, "DataSource name must not be null"
        assert dataSource, "DataSource must not be null"
        self.dataSources[dataSourceName] = dataSource
    
    def getDataSource(self, dataSourceName=None):
        assert dataSourceName, "DataSource name must not be null"
        dataSource = self.dataSources.get(dataSourceName)
        if dataSource == None :
            raise Exception("No DataSource with name '" + dataSourceName + "' registered")
        return dataSource

