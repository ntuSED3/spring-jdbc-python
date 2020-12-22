import pandas as pd
from embedded.EmbeddedDatabaseFactory import EmbeddedDatabaseFactory


if __name__ == "__main__":
    factory = EmbeddedDatabaseFactory()
    factory.setDatabaseType("H2")
    ds = factory.getDatabase()
    conn = ds.getConnection()

    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS customers;""")
    cur.execute("""CREATE TABLE customers(
            id INT, first_name VARCHAR(255), last_name VARCHAR(255));""")
    cur.execute("""INSERT INTO customers VALUES (1, 'Andy', 'Wang');""")
    cur.execute("""SELECT * FROM customers;""")
    records = cur.fetchall()
    df = pd.DataFrame(records)
    print(df)
    
