class JdbcTemplate(JdbcAccessor):
    def __init__(self):
        super().__init__()
    def _execute(self, action: StatementCallback, closeResources: bool):
        pass

    def execute(self, sql: str):
        class ExecuteStatementCallback():
            def doInStatement(self, cursor):
                return cursor.execute(sql)

            def getSql(self):
                return sql

        return self._execute(ExecuteStatementCallback(), True)

    def query(self, sql: str) -> list:
        pass
    def update(self, sql: str) -> int:
        pass
    def batchUpdate(self, *sql: str) -> list:
        pass
