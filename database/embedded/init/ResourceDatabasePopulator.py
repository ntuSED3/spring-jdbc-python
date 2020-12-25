class ResourceDatabasePopulator():
    def __init__(self, *argv):
        self.scripts = []
        self.setScripts(*argv)
    def addScript(self, script):
        assert script is not None, "'script' must not be null"
        self.scripts.append(script)
    def addScripts(self, *argv):
        self._assertContentsOfScriptArray(argv)
        for arg in argv: 
            self.scripts.append(arg)
    def setScripts(self, *argv):
        self._assertContentsOfScriptArray(argv)
        self.scripts = []
        for arg in argv:
            self.scripts.append(arg)
    def _assertContentsOfScriptArray(self, *argv):
        for arg in argv:
            assert arg is not None, "'scripts' must not be null"
    def populate(self, conn):
        assert conn is not None, "'connection' must not be null"
        cur = conn.cursor()
        for script in self.scripts:
            with open(script, 'r') as sql_file:
                for _, sql in enumerate(sql_file):
                    cur.execute(sql)
        self.scripts = []
        conn.commit()
    def execute(self, datasource):
        conn = datasource.getConnection()
        self.populate(conn)
