from .HsqlConfigurer import HsqlConfigurer
from .H2Configurer import H2Configurer

class EmbeddedDatabaseConfigurerFactory():
    def getConfigurer(name):
        if name == "HSQL":
            return HsqlConfigurer()
	#elif name == "Derby":
	#    return DerbyConfigurer()
        elif name == "H2":
            return H2Configurer()

        else:
            raise NotImplementedError
