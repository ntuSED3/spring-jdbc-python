import threading
from .AbstractDatabaseConfigurer import AbstractDatabaseConfigurer

class H2Configurer(AbstractDatabaseConfigurer):
    __instance = None
    @staticmethod
    def getInstance():
        if H2Configurer.__instance is None:
            with threading.Lock():
                if H2Configurer.__instance is None:
                    H2Configurer()
        return H2Configurer.__instance

    def __init__(self):
        if H2Configurer.__instance is not None:
            raise Exception("Creating another class from a Singleton")
        else:
            H2Configurer.__instance = self

    def configure(self, cp, databaseName):
        cp.setJClassName("org.h2.Driver")
        cp.setUrl("jdbc:h2:mem:{};DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=false".format(databaseName))
