from MapDataSourceLookup import MapDataSourceLookup
from SingleDataSourceLookup import SingleDataSourceLookup
from DataSource import DataSource
import sqlite3
from AbstractRoutingDataSource import AbstractRoutingDataSource
class DataSource_1(DataSource):
    def getConnection(self, username=None, password=None):
            return sqlite3.connect("test.db")

class DataSource_2(DataSource):
    def getConnection(self, username=None, password=None):
            return sqlite3.connect("test.db")

class DataSource_3(DataSource):
    def getConnection(self, username=None, password=None):
            return sqlite3.connect("test.db")


name1 = "d1"
name2 = "d2"
name3 = "d3"

print("Test SingleDataSourceLookup") 
print("#######")
DS1 = DataSource_1()
DS2 = DataSource_2()
DS3 = DataSource_3()
singleDS = SingleDataSourceLookup(DS1)
assert singleDS.getDataSource("") == DS1 , "SingleDataSourceLookup getDataSource error"



print("Test MapDataSourceLookup")
print("#######") 
dictDS = {name1 : DS1,name2 : DS2,name3 : DS3}

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