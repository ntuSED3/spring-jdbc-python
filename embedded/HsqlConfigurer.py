import threading
from .EmbeddedDatabaseConfigurer import EmbeddedDatabaseConfigurer

class HsqlConfigurer(EmbeddedDatabaseConfigurer):
    __instance = None
    @staticmethod
    def getInstance():
        if HsqlConfigurer.__instance is None:
            with threading.Lock():
                if HsqlConfigurer.__instance is None:
                    HsqlConfigurer()
        return HsqlConfigurer.__instance

    def __init__(self):
        if HsqlConfigurer.__instance is not None:
            raise Exception("Creating another class from a Singleton")
        else:
            HsqlConfigurer.__instance = self

    def configure(self, cp, databaseName):
        cp.setJClassName("org.hsqldb.jdbc.JDBCDriver")
        cp.setUrl("jdbc:hsqldb:mem:{}".format(databaseName))
        cp.setJarPath("embedded/jar/hsqldb.jar")
        
