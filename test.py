from JdbcTemplate import JdbcTemplate
from DataSource import DataSource
from LazyConnectionDataSourceProxy import LazyConnectionDataSourceProxy
import sqlite3

class SqliteDataSource(DataSource):
      def getConnection(self, username=None, password=None):
            return sqlite3.connect("test.db")

jdbctemplate = JdbcTemplate(LazyConnectionDataSourceProxy(SqliteDataSource()))
jdbctemplate.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''', False)

jdbctemplate.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )", False)
jdbctemplate.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Paul', 32, 'California', 20000.00 )", False)
#ret = jdbctemplate.update("UPDATE COMPANY SET SALARY = 25000.00 where ID=1")
ret = jdbctemplate.batchUpdate("UPDATE COMPANY set SALARY = 25000.00 where ID=1", 
                     "UPDATE COMPANY set SALARY = 30000.00 where ID=2", closeResource=False)
print(jdbctemplate.query("SELECT * FROM COMPANY", False))