import abc

class DataSourceLookup(abc.ABC):
    @abc.abstractmethod
    def getDataSource(self,dataSourceName):
        raise NotImplementedError