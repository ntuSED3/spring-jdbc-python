from .EmbeddedDatabaseConfigurer import EmbeddedDatabaseConfigurer

class HsqlConfigurer(EmbeddedDatabaseConfigurer):
    def configure(self, cp, databaseName):
        cp.setJClassName("org.hsqldb.jdbc.JDBCDriver")
        cp.setUrl("jdbc:hsqldb:mem:{}".format(databaseName))
        cp.setJarPath("embedded/hsqldb-2.5.1/hsqldb/lib/hsqldb.jar")
        
