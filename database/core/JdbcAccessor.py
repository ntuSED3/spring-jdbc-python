from ..datasource.DataSource import DataSource
class JdbcAccessor:
    def __init__(self):
        self.dataSource = None
    def SetDataSource(self, dataSource: DataSource):
        self.dataSource = dataSource
    def GetDataSource(self) -> DataSource:
        return self.dataSource