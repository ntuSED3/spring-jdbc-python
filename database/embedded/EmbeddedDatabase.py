from ..datasource.DataSource import DataSource

class EmbeddedDatabase(DataSource):
    def shutdown(self):
        raise NotImplementedError
