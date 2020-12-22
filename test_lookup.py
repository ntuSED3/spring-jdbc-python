from MapDataSourceLookup import MapDataSourceLookup
from SingleDataSourceLookup import SingleDataSourceLookup
from DataSource import DataSource
import sqlite3

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
print("#######")
print("Test SingleDataSourceLookup") 

DS1 = DataSource_1()
DS2 = DataSource_2()
DS3 = DataSource_3()
singleDS = SingleDataSourceLookup(DS1)
print(singleDS.getDataSource("") == DS1)
print("#######")
print("Test DataSources getter and setter")  

dictDS = {name1 : DS1,name2 : DS2,name3 : DS3}
print(dictDS)
mapDS = MapDataSourceLookup()
mapDS.setDataSources(dictDS)
dictDSfromMap = mapDS.getDataSources()
for k,v in dictDSfromMap.items():
    print(dictDSfromMap[k] == dictDS[k])


print("#######")
print("Test MapDataSourceLookup Constructer with DataSources")  

mapDS = MapDataSourceLookup(dictDS)
dictDSfromMap = mapDS.getDataSources()
for k,v in dictDSfromMap.items():
    print(dictDSfromMap[k] == dictDS[k])

print("#######")
print("Test MapDataSourceLookup Constructer with One DataSource")  
mapDS = MapDataSourceLookup(dataSourceName=name1,dataSource=DS1)
dictDSfromMap = mapDS.getDataSources()
print(dictDSfromMap)

print("#######")
print("Test MapDataSourceLookup add DataSource")
mapDS.addDataSource(name2,DS2)
dictDSfromMap = mapDS.getDataSources()
print(dictDSfromMap)

print("#######")
print("Test MapDataSourceLookup get DataSource")

getDS = mapDS.getDataSource(name1)
print(getDS==DS1)

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