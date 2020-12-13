from JdbcAccessor import JdbcAccessor
import sqlite3
# interface
# Maybe we should use abc.ABCMeta and abc.abstractmethod to prevent us from instantiating this class
class StatementCallback:
    def doInStatement(self, cursor):
        pass
    # ignore SqlProvider interface, I think it is useless
    def getSql(self) -> str:
        pass

class JdbcTemplate(JdbcAccessor):
    def __init__(self):
        super().__init__()
    def _execute(self, action: StatementCallback, closeResources: bool):
        assert action is not None
        #TODO: get connection somewhere
        con = sqlite3.connect('db')
        cursor = con.cursor()
        try:
            result = action.doInStatement(cursor)
            return result
        except Exception:
            # from original JdbcTemplate
            # Release Connection early, to avoid potential connection pool deadlock
			# in the case when the exception translator hasn't been initialized yet.
            cursor.close()
            #TODO: exception translation
        finally:
            if closeResources:
                #TODO: close connection by JdbcUtils(exception handling)
                cursor.close()

    def execute(self, sql: str):
        class ExecuteStatementCallback(StatementCallback):
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
        class BatchUpdateStatementCallback(StatementCallback):
            def __init__(self):
                self.cur = ""
            
            def doInStatement(self, cursor):
                rowAffected = [0] * len(sql)
                # if JdbcUtils.supportBatchUpdates...
                # ...
                # ...
                # else
                for i, cur in enumerate(sql):
                    self.cur = cur
                    cursor.execute(self.cur)
                    results = cursor.fetchall()
                    if results:
                        rowAffected[i] = len(results)
                    else:
                        # throw new InvalidDataAccessApiUsageException("Invalid batch SQL statement: " + cur);
                        return None
                return rowAffected
            
            def _appendSql(self,sql,stmt):
                pass
            def getSql(self):
                return self.cur
        return self._execute(BatchUpdateStatementCallback(), True)