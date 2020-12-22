import enum

class EmbeddedDatabaseType(enum.Enum):
    HSQL = enum.auto()
    H2 = enum.auto()
    DERBY = enum.auto()

