from .HsqlConfigurer import HsqlConfigurer
from .H2Configurer import H2Configurer
from .DerbyConfigurer import DerbyConfigurer
from .EmbeddedDatabaseType import EmbeddedDatabaseType

class EmbeddedDatabaseConfigurerFactory():
    def getConfigurer(edbType):
        if edbType == EmbeddedDatabaseType.HSQL:
            return HsqlConfigurer()
        elif edbType == EmbeddedDatabaseType.DERBY:
            return DerbyConfigurer()
        elif edbType == EmbeddedDatabaseType.H2:
            return H2Configurer()

        else:
            raise NotImplementedError
