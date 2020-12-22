from .EmbeddedDatabaseConfigurer import EmbeddedDatabaseConfigurer

class DerbyConfigurer(EmbeddedDatabaseConfigurer):
    def configure(self, cp, databaseName):
        cp.setJClassName("org.apache.derby.jdbc.EmbeddedDriver")
        cp.setUrl("jdbc:derby:memory:{};create=true".format(databaseName))
        cp.setJarPath("embedded/jar/derby.jar")
