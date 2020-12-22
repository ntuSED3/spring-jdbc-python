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
        resDataSource = getTargetDataSource()
        assert resDataSource is not None
        return resDataSource

    def afterPropertiesSet(self):
        if (getTargetDataSource() is None):
            raise NameError("Property 'targetDataSource' is required")

    def getConnection():
        return obtainTargetDataSource().getConnection()

    def getConnection(username: str, password: str):
        return obtainTargetDataSource().getConnection(username, password)