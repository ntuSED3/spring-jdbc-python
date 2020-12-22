from DataSource import DataSource

class DelegatingDataSource(DataSource):
    _targetDataSource = None

    def __init__(self, targetDataSource: DataSource):
        if (targetDataSource is not None):
            setTargetDataSource(targetDataSource)
    
    def setTargetDataSource(self, targetDataSource: DataSource):
        self._targetDataSource = targetDataSource

    def getTargetDataSource(self) -> DataSource:
        return self._targetDataSource

    def obtainTargetDataSource(self) -> DataSource:
        resDataSource = self.getTargetDataSource()
        assert resDataSource is not None
        return resDataSource

    def afterPropertiesSet(self):
        if (self.getTargetDataSource() is None):
            raise NameError("Property 'targetDataSource' is required")

    def getConnection(self):
        return self.obtainTargetDataSource().getConnection()

    def getConnection(self, username: str, password: str):
        return self.obtainTargetDataSource().getConnection(username, password)