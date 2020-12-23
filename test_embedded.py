import pandas as pd
from embedded.EmbeddedDatabaseFactory import EmbeddedDatabaseFactory
from embedded.EmbeddedDatabaseBuilder import EmbeddedDatabaseBuilder
from embedded.EmbeddedDatabaseType import EmbeddedDatabaseType
from init.ResourceDatabasePopulator import ResourceDatabasePopulator

if __name__ == "__main__":
    builder = EmbeddedDatabaseBuilder()
    ds = builder.setType(EmbeddedDatabaseType.H2).addScripts("test.sql", "test2.sql").build()

#     cur.execute("""DROP TABLE IF EXISTS customers;""")
#     cur.execute("""CREATE TABLE customers(id INT, first_name VARCHAR(255), last_name VARCHAR(255));""")
#     cur.execute("""INSERT INTO customers VALUES (1, 'Andy', 'Wang');""")
#     cur.execute("""SELECT * FROM customers;""")
#     records = cur.fetchall()
#     df = pd.DataFrame(records)

    conn = ds.getConnection()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM customers;""")
    records = cur.fetchall()
    df = pd.DataFrame(records)
    print(df)