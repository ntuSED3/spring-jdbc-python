from .EmbeddedDatabaseConfigurer import EmbeddedDatabaseConfigurer
from ..datasource.DataSource import DataSource

class AbstractDatabaseConfigurer(EmbeddedDatabaseConfigurer):
    def shutdown(self, ds: DataSource, db_name):
        try:
            conn = ds.getConnection()
            if conn is not None:
                try:
                    cur = conn.cursor()
                    cur.execute("SHUTDOWN")
                except:
                    pass

        except Exception as e:
            print('Could not shut down embedded database', e)

        finally:
            if conn is not None:
                try:
                    conn.close()
                except Exception as e:
                    print("Could not close JDBC Connection on shutdown", e)
    
