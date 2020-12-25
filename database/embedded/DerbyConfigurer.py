import threading
from .AbstractDatabaseConfigurer import AbstractDatabaseConfigurer

class DerbyConfigurer(AbstractDatabaseConfigurer):
    __instance = None
    @staticmethod
    def getInstance():
        if DerbyConfigurer.__instance is None:
            with threading.Lock():
                if DerbyConfigurer.__instance is None:
                    DerbyConfigurer()
        return DerbyConfigurer.__instance

    def __init__(self):
        if DerbyConfigurer.__instance is not None:
            raise Exception("Creating another class from a Singleton")
        else:
            DerbyConfigurer.__instance = self

    def configure(self, cp, databaseName):
        cp.setJClassName("org.apache.derby.jdbc.EmbeddedDriver")
        cp.setUrl("jdbc:derby:memory:{};create=true".format(databaseName))
