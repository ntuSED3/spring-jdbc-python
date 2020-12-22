from .JaydebeDataSource import JaydebeDataSource
from .DataSourceFactory import DataSourceFactory
from .ConnectionProperties import ConnectionProperties

class JaydebeDataSourceFactory(DataSourceFactory):
    def __init__(self):
        self.datasource = JaydebeDataSource()

    def getConnectionProperties(self):
        class cp(ConnectionProperties):
            def __init__(self, ds):
                self.ds = ds

            def setUrl(self, url):
                self.ds.setUrl(url)		
            
            def setJarPath(self, jarpath):
                self.ds.setJarPath(jarpath)	
            
            def setJClassName(self, name):
                self.ds.setJClassName(name)

            def setPassword(self, pw):
                self.ds.setPassword(pw)

            def setUserName(self, name):
                self.ds.setUserName(name)

        return cp(self.datasource)
	
    def getDataSource(self):
        return self.datasource
