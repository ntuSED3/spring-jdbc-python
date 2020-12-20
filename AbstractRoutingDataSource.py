import abc
from DataSource import DataSource
class AbstractRoutingDataSource(abc.ABC,DataSource):
    def __init__(self):
        # Map<Object, Object>
        self.targetDataSources = None

        # Object 
        self.defaultTargetDataSource = None

        self.lenientFallback = True

        # replace JndiDataSourceLookup() to ?
        # self.dataSourceLookup = DataSourceLookup()

        # Map<Object, DataSource>
        self.resolvedDataSources = None

        # DataSource
        self.resolvedDefaultDataSource = None
    
    # Setter
    def setTargetDataSources(self,targetDataSources):
        self.targetDataSources = targetDataSources
    
    def setDefaultTargetDataSource(self,defaultTargetDataSource):
        self.defaultTargetDataSource = defaultTargetDataSource
    
    def setLenientFallback(self,lenientFallback):
        self.lenientFallback = lenientFallback
    
    def setDataSourceLookup(self,dataSourceLookup):
        # replace JndiDataSourceLookup() to ?
        self.dataSourceLookup = dataSourceLookup #if dataSourceLookup else DataSourceLookup()

    def afterPropertiesSet(self):
        if self.targetDataSources == None:
            # throw IllegalArgumentException("Property 'targetDataSources' is required")
            raise Exception("Property 'targetDataSources' is required")
        self.resolvedDataSources = {}
        for key,value in self.targetDataSources.items():
            lookupKey = self.resolveSpecifiedLookupKey(key)
            dataSource = self.resolveSpecifiedDataSource(value)
            self.resolvedDataSources[lookupKey] = dataSource
        
        if self.defaultTargetDataSource :
            self.resolvedDefaultDataSource = self.resolveSpecifiedDataSource(self.defaultTargetDataSource)
    
    def resolveSpecifiedLookupKey(self,lookupKey):
        return lookupKey
    
    def resolveSpecifiedDataSource(self,dataSource):
        if isinstance(dataSource,DataSource):
            return dataSource
        elif isinstance(dataSource, str):
            # return self.dataSourceLookup.getDataSource(dataSource)
            pass
        else:
            # throw new IllegalArgumentException(
			#		"Illegal data source value - only [javax.sql.DataSource] and String supported: " + dataSource);
            raise Exception("Illegal data source value - only [javax.sql.DataSource] and String supported: " + dataSource)
    # Getter
    def getResolvedDataSources(self):
        assert self.resolvedDataSources, "DataSources not resolved yet - call afterPropertiesSet"
        return self.resolvedDataSources.copy()
    
    def getResolvedDefaultDataSource(self):
        return self.resolvedDefaultDataSource         
    
    def getConnection(self,username=None,password=None):
        return self.determineTargetDataSource().getConnection(username,password)
    
    def determineTargetDataSource(self):
        assert self.resolvedDataSources, "DataSource router not initialized" 
        lookupKey = self.determineCurrentLookupKey()
        dataSource = self.resolvedDataSources[lookupKey]
        if dataSource == None and (self.lenientFallback or lookupKey == None):
            dataSource = self.resolvedDefaultDataSource
        if dataSource == None:
            # throw new IllegalStateException("Cannot determine target DataSource for lookup key [" + lookupKey + "]")
            raise Exception("Cannot determine target DataSource for lookup key [" + lookupKey + "]")
             
        return dataSource
    
    
    @abc.abstractmethod
    def determineCurrentLookupKey(self):
        pass