from database.core.JdbcTemplate import JdbcTemplate
from database.datasource.DataSource import DataSource
from database.datasource.LazyConnectionDataSourceProxy import LazyConnectionDataSourceProxy
import sqlite3
from database.embedded.EmbeddedDatabaseBuilder import EmbeddedDatabaseBuilder
from database.embedded.EmbeddedDatabaseType import EmbeddedDatabaseType
from database.datasource.UserCredentialsDataSourceAdapter import UserCredentialsDataSourceAdapter

class SqliteDataSource(DataSource):
      def getConnection(self, username=None, password=None):
            return sqlite3.connect("test.db")



#jdbctemplate = JdbcTemplate(LazyConnectionDataSourceProxy(SqliteDataSource()))
ds = EmbeddedDatabaseBuilder().setType(EmbeddedDatabaseType.H2).build()
jdbctemplate = JdbcTemplate(LazyConnectionDataSourceProxy(ds))
#jdbctemplate.execute('''DROP TABLE IF EXISTS COMPANY;''')
jdbctemplate.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''', False)
print(jdbctemplate.execute("""SHOW TABLES;""", False))

jdbctemplate.execute("""
INSERT INTO COMPANY VALUES (1, 'Paul', 32, 'California', 20000.00 );""", False)
jdbctemplate.execute("INSERT INTO COMPANY \
      VALUES (2, 'Paul', 32, 'California', 20000.00 );", False)
#ret = jdbctemplate.update("UPDATE COMPANY SET SALARY = 25000.00 where ID=1")
ret = jdbctemplate.batchUpdate("UPDATE COMPANY set SALARY = 25000.00 where ID=1", 
                     "UPDATE COMPANY set SALARY = 30000.00 where ID=2;", closeResource=False)
print(jdbctemplate.query("SELECT * FROM COMPANY;", False))
