import abc
class DataSource(abc.ABC):
    @abc.abstractmethod
    def getConnection(self,username=None, password=None):
        raise NotImplementedError

