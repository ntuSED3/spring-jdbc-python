from database.datasource.DataSource import DataSource
from database.datasource.AbstractRoutingDataSource import AbstractRoutingDataSource
from database.lookup.MapDataSourceLookup import MapDataSourceLookup
from database.lookup.SingleDataSourceLookup import SingleDataSourceLookup
import sqlite3

class SqliteDataSource(DataSource):
      def getConnection(self, username=None, password=None):
            return sqlite3.connect("test.db")


name1, name2, name3 = "d1", "d2", "d3"
DS1, DS2, DS3 = SqliteDataSource(), SqliteDataSource(), SqliteDataSource()
dictDS = {"d1" : DS1,"d2" : DS2,"d3" : DS3}

print("Test SingleDataSourceLookup") 
print("#######")
singleDS = SingleDataSourceLookup(DS1)
assert singleDS.getDataSource("") == DS1 , "SingleDataSourceLookup getDataSource error"


print("Test MapDataSourceLookup")
print("#######") 

mapDS = MapDataSourceLookup()
mapDS.setDataSources(dictDS)
dictDSfromMap = mapDS.getDataSources()
for k,v in dictDS.items():
    assert dictDSfromMap[k] == dictDS[k], "MapDataSourceLookup DataSources getter or setter error"
 

mapDS = MapDataSourceLookup(dictDS)
dictDSfromMap = mapDS.getDataSources()
for k,v in dictDS.items():
    assert dictDSfromMap[k] == dictDS[k], "MapDataSourceLookup Construct with dataSources error"

mapDS = MapDataSourceLookup(dataSourceName=name1,dataSource=DS1)

dictDSfromMap = mapDS.getDataSources()
assert dictDSfromMap[name1] == DS1 , "MapDataSourceLookup Construct with dataSourceName and dataSource error"

# Test add Data
mapDS.addDataSource(name2,DS2)
dictDSfromMap = mapDS.getDataSources()
dic = {name1:DS1, name2:DS2}
for k,v in dic.items():
    assert dictDSfromMap[k] == dic[k], "MapDataSourceLookup addDataSource() Fail"
# Test get DataSource
getDS = mapDS.getDataSource(name1)
assert getDS==DS1 , "MapDataSourceLookup getDataSource() Fail"

"""print("#######")
print("Test MapDataSourceLookup add DataSource 2, it will assert error")
mapDS.addDataSource(None,DS2)
dictDSfromMap = mapDS.getDataSources()
print(dictDSfromMap)"""

"""print("#######")
print("Test MapDataSourceLookup Constructer, it will assert error")  
mapDS = MapDataSourceLookup(dictDS,dataSourceName=name1,dataSource=DS1)
dictDSfromMap = mapDS.getDataSources()
print(dictDSfromMap)"""

"""print("#######")
print("Test MapDataSourceLookup get DataSource, it will assert error")
mapDS = MapDataSourceLookup()
getDS = mapDS.getDataSource(name1)
print(getDS==DS1)"""

class TestRoutingDataSource(AbstractRoutingDataSource):
    def __init__(self):
        super().__init__()
        self.current_lookup_key = "d1"
    def determineCurrentLookupKey(self):
        return self.current_lookup_key

print("Test TestRoutingDataSource")
print("#######")
rDS = TestRoutingDataSource()
rDS.setDataSourceLookup(MapDataSourceLookup(dictDS))
rDS.setTargetDataSources(dictDS)
rDS.setDefaultTargetDataSource(DS1)
rDS.afterPropertiesSet()


dictDSfromMap = rDS.getResolvedDataSources()
for k,v in dictDS.items():
    assert dictDSfromMap[k] == dictDS[k] , "getResolvedDataSources() Fail"

assert rDS.getResolvedDefaultDataSource() == DS1, "getResolvedDefaultDataSource() Fail"
assert rDS.determineTargetDataSource() == DS1, "determineTargetDataSource() Fail"