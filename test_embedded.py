import pandas as pd
from database.embedded.EmbeddedDatabaseFactory import EmbeddedDatabaseFactory
from database.embedded.EmbeddedDatabaseBuilder import EmbeddedDatabaseBuilder
from database.embedded.EmbeddedDatabaseType import EmbeddedDatabaseType
from database.embedded.init.ResourceDatabasePopulator import ResourceDatabasePopulator

if __name__ == "__main__":
    builder = EmbeddedDatabaseBuilder()
    ds = builder.setType(EmbeddedDatabaseType.H2).addScripts("test.sql", "test2.sql").build()

    conn = ds.getConnection()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM customers;""")
    records = cur.fetchall()
    df = pd.DataFrame(records)
    print(df)