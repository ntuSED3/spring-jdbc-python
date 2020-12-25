from database.core.JdbcTemplate import JdbcTemplate
from database.embedded.EmbeddedDatabaseBuilder import EmbeddedDatabaseBuilder
from database.embedded.EmbeddedDatabaseType import EmbeddedDatabaseType

builder = EmbeddedDatabaseBuilder()

print('=====test builder/HSQL=====')
hsql_ds = (builder
    .setType(EmbeddedDatabaseType.HSQL)
    .addScript("test.sql")
    .addScript("test2.sql")
    .generateUniqueName(True)
    .build()
)
jdbcTemplate = JdbcTemplate(hsql_ds)
print(jdbcTemplate.query("SELECT * FROM customers;"))
hsql_ds.shutdown()
print('=====end=====\n')

print('=====test builder/H2=====')
h2_ds = (builder
    .setType(EmbeddedDatabaseType.H2)
    .addScript("test.sql")
    .addScript("test2.sql")
    .generateUniqueName(True)
    .build()
)
jdbcTemplate = JdbcTemplate(h2_ds)
print(jdbcTemplate.query("SELECT * FROM customers;"))
h2_ds.shutdown()
print('=====end=====\n')

print('=====test Derby======')
derby_ds = (builder
    .setType(EmbeddedDatabaseType.DERBY)
    .addScript("test-derby.sql")
    .build()
)
jdbcTemplate.SetDataSource(derby_ds)
print(jdbcTemplate.query("SELECT * FROM customers"))
derby_ds.shutdown()
print('=====end=====\n')
