from .EmbeddedDatabaseConfigurer import EmbeddedDatabaseConfigurer

class H2Configurer(EmbeddedDatabaseConfigurer):
    def configure(self, cp, databaseName):
        cp.setJClassName("org.h2.Driver")
        cp.setUrl("jdbc:h2:mem:{}".format(databaseName))
        cp.setJarPath("embedded/h2-1.4.200.jar")
