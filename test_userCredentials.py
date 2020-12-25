from database.core.JdbcTemplate import JdbcTemplate
from database.datasource.DataSource import DataSource
from database.datasource.UserCredentialsDataSourceAdapter import UserCredentialsDataSourceAdapter
from database.datasource.LazyConnectionDataSourceProxy import LazyConnectionDataSourceProxy
import pymysql
#TODO
class SqliteDataSource(DataSource):
      def getConnection(self, username=None, password=None):
            return pymysql.connect(host='127.0.0.1', user=username, password=password)

username = "group3"
passwd = "3puorg"

ds = UserCredentialsDataSourceAdapter(SqliteDataSource())
ds.setCredentialsForCurrentThread(username, passwd)
ds = LazyConnectionDataSourceProxy(ds)

jdbcTemplate = JdbcTemplate(ds)
#print(jdbcTemplate.query("SHOW TABLES FROM TMP_DB;"))
jdbcTemplate.execute("CREATE DATABASE IF NOT EXISTS TMP_DB;", False)
jdbcTemplate.execute("USE TMP_DB;", False)
jdbcTemplate.execute("DROP TABLE IF EXISTS COMPANY;", False)

jdbcTemplate.execute('''
        CREATE TABLE COMPANY(
        ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);
        ''', False)
jdbcTemplate.execute('''
INSERT INTO COMPANY VALUES (1, 'Paul', 32, 'California', 20000.00 );
''', False)
jdbcTemplate.execute('''
INSERT INTO COMPANY VALUES (2, 'Amy', 23, 'New York', 20000.00 );
''', False)
print(jdbcTemplate.query("SELECT * FROM COMPANY;", False))
