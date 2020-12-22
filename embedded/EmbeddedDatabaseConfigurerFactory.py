from .HsqlConfigurer import HsqlConfigurer

class EmbeddedDatabaseConfigurerFactory():
    def getConfigurer(name):
        if name == "HSQL":
            return HsqlConfigurer()
	#elif name == "Derby":
	#    return DerbyConfigurer()
