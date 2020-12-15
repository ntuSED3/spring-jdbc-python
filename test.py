import JdbcTemplate

jdbctemplate = JdbcTemplate.JdbcTemplate()
jdbctemplate.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')

jdbctemplate.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")
jdbctemplate.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Paul', 32, 'California', 20000.00 )")

jdbctemplate.batchUpdate("UPDATE COMPANY set SALARY = 25000.00 where ID=1", 
                      "UPDATE COMPANY set SALARY = 30000.00 where ID=2")
ret = jdbctemplate.execute('''SELECT * FROM COMPANY;''')
print(ret)