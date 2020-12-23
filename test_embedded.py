import pandas as pd
from embedded.EmbeddedDatabaseFactory import EmbeddedDatabaseFactory
from embedded.EmbeddedDatabaseBuilder import EmbeddedDatabaseBuilder
from embedded.EmbeddedDatabaseType import EmbeddedDatabaseType
from init.ResourceDatabasePopulator import ResourceDatabasePopulator

if __name__ == "__main__":
    builder = EmbeddedDatabaseBuilder()
    ds = builder.setType(EmbeddedDatabaseType.H2).addScripts("test.sql", "test2.sql").build()

    conn = ds.getConnection()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM customers;""")
    records = cur.fetchall()
    df = pd.DataFrame(records)
    print(df)