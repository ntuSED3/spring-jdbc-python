class EmbeddedDatabaseConfigurer(object):
    def configure(self, connectionProperties, databaseName):
        raise NotImplementedError
