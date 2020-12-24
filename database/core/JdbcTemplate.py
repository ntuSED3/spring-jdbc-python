from .JdbcAccessor import JdbcAccessor
from ..datasource.DataSource import DataSource
# interface
# Maybe we should use abc.ABCMeta and abc.abstractmethod to prevent us from instantiating this class
class StatementCallback:
    def doInStatement(self, conn):
        raise NotImplementedError
    # ignore SqlProvider interface, I think it is useless
    def getSql(self) -> str:
        raise NotImplementedError

class JdbcTemplate(JdbcAccessor):
    def __init__(self, dataSource: DataSource=None):
        super().__init__()
        self.SetDataSource(dataSource)
    def _execute(self, action: StatementCallback, closeResources: bool):
        assert action is not None
        # get connection somewhere
        con = self.GetDataSource().getConnection()
        try:
            result = action.doInStatement(con)
            return result
        except Exception as e:
            print(e)
            # from original JdbcTemplate
            # Release Connection early, to avoid potential connection pool deadlock
			# in the case when the exception translator hasn't been initialized yet.
            if closeResources:
                con.close()
            #TODO: exception translation
        finally:
            if closeResources:
                #TODO: close connection by JdbcUtils(exception handling)
                con.close()

    def execute(self, sql: str, closeResource=True):
        class ExecuteStatementCallback(StatementCallback):
            def doInStatement(self, conn):
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                #return [row for row in cursor]
                # return cursor.fetchall()

            def getSql(self):
                return sql

        return self._execute(ExecuteStatementCallback(), closeResource)

    def query(self, sql: str, closeResource=True) -> list:
        class QueryStatementCallback(StatementCallback):
            def doInStatement(self, conn):
                try:
                    cursor = conn.cursor()
                    cursor.execute(sql)
                    return cursor.fetchall()
                except:
                    pass
            def getSql(self):
                return sql
        return self._execute(QueryStatementCallback(), closeResource)

    def update(self, sql: str, closeResource=True) -> int:
        assert sql is not None, "SQL must not be null"
        class UpdateStatementCallback(StatementCallback):
            def doInStatement(self, conn) -> int:
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                return cursor.rowcount
            def getSql(self) -> str:
                return sql
        return self._execute(UpdateStatementCallback(), closeResource)
        
    def batchUpdate(self, *sql: str, closeResource=True) -> list:
        class BatchUpdateStatementCallback(StatementCallback):            
            def doInStatement(self, conn):
                cursor = conn.cursor()
                rowAffected = [0] * len(sql)
                # if JdbcUtils.supportBatchUpdates...
                # ...
                # ...
                # else
                
                for i, cur in enumerate(sql):
                    #print(sql[i])
                    #print(i,cur)
                    cursor.execute(cur)
                    conn.commit()
                    results = cursor.rowcount 
                    if results:
                        rowAffected[i] = results
                    else:
                        # throw new InvalidDataAccessApiUsageException("Invalid batch SQL statement: " + cur);
                        return None
                return rowAffected
            
            def _appendSql(self,sql,stmt):
                pass
            def getSql(self):
                return self.cur
        return self._execute(BatchUpdateStatementCallback(), closeResource)
