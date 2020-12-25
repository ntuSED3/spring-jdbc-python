from database.core.JdbcTemplate import JdbcTemplate
from database.datasource.DataSource import DataSource
import sqlite3

class SqliteDataSource(DataSource):
      def getConnection(self, username=None, password=None):
            return sqlite3.connect("test.db")

jdbcTemplate = JdbcTemplate(SqliteDataSource())
jdbcTemplate.execute("DROP TABLE IF EXISTS COMPANY;")
jdbcTemplate.execute('''
        CREATE TABLE COMPANY(
        ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);
        ''')
jdbcTemplate.execute('''
INSERT INTO COMPANY VALUES (1, 'Paul', 32, 'California', 20000.00 );
''')
jdbcTemplate.execute('''
INSERT INTO COMPANY VALUES (2, 'Amy', 23, 'New York', 20000.00 );
''')
print(jdbcTemplate.query("SELECT * FROM COMPANY;"))

jdbcTemplate.batchUpdate(
"UPDATE COMPANY set SALARY = 25000.00 where ID=1;", 
"UPDATE COMPANY set SALARY = 30000.00 where ID=2;")
print(jdbcTemplate.query("SELECT * FROM COMPANY;"))
