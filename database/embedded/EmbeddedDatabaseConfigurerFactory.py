from .HsqlConfigurer import HsqlConfigurer
from .H2Configurer import H2Configurer
from .DerbyConfigurer import DerbyConfigurer
from .EmbeddedDatabaseType import EmbeddedDatabaseType

class EmbeddedDatabaseConfigurerFactory():
    def getConfigurer(edbType):
        if edbType == EmbeddedDatabaseType.HSQL:
            return HsqlConfigurer.getInstance()
        elif edbType == EmbeddedDatabaseType.DERBY:
            return DerbyConfigurer.getInstance()
        elif edbType == EmbeddedDatabaseType.H2:
            return H2Configurer.getInstance()

        else:
            raise NotImplementedError
