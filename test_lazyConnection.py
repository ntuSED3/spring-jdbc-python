from database.core.JdbcTemplate import JdbcTemplate
from database.datasource.DataSource import DataSource
from database.datasource.LazyConnectionDataSourceProxy import LazyConnectionDataSourceProxy
import sqlite3

class SqliteDataSource(DataSource):
      def getConnection(self, username=None, password=None):
            return sqlite3.connect("test.db")

# Everytime we call getConnection(), we get a new instance
myDataSource = SqliteDataSource()
conn1 = myDataSource.getConnection()
conn2 = myDataSource.getConnection()
print(conn1 is conn2)
print(conn1)
print(conn2)

# Lazy connection testing
jdbcTemplate = JdbcTemplate(LazyConnectionDataSourceProxy(myDataSource))
# No Connection before the first SQL command
print('=======Start========')
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

print('=======Auto close resource for now.========')
# Still use the previous Connection
jdbcTemplate.update("UPDATE COMPANY set SALARY = 25000.00 where ID=1;", True)

# Because the Connection has been closed by jdbcTemplate, 
# LazyConnectionDataSourceProxy create a new Connection
jdbcTemplate.update("UPDATE COMPANY set SALARY = 30000.00 where ID=2;", True)

# Create a new Connection again
print(jdbcTemplate.query("SELECT * FROM COMPANY;", True))