from DataSourceLookup import DataSourceLookup
class MapDataSourceLookup(abc.ABC, DataSourceLookup):
    def __init__(self,dataSources=None,dataSourceName=None,dataSource=None):
        self.dataSources = {}
        self.setDataSources(dataSources)
        if dataSourceName and dataSource:
            self.addDataSource(dataSourceName,dataSource)
    
    def setDataSources(self,dataSources):
        if dataSources:
            self.dataSources = dataSources.copy()
    

    def getDataSources(self):
        return self.dataSources.copy()

    def addDataSource(self,dataSourceName,dataSource):
        assert dataSourceName, "DataSource name must not be null"
        assert dataSource, "DataSource must not be null"
        self.dataSources[dataSourceName] = dataSource
    
    def getDataSource(self, dataSourceName):
        assert dataSourceName, "DataSource name must not be null"
        dataSource = self.dataSources.get(dataSourceName)
        if dataSource == None :
            raise Exception("No DataSource with name '" + dataSourceName + "' registered")
        return dataSource

