import DelegatingDataSource
class LazyConnectionDataSourceProxy(DelegatingDataSource):
   def __init__(self, targetDataSource = None):
      if targetDataSource != None:
         super().setTargetDataSource(targetDataSource)
         afterPropertiesSet()
         self.defaultAutoCommit = None
         self.defaultTransactionIsolation = None
   
   def DefaultAutoCommit(self, defaultAutoCommit):
      self.defaultAutoCommit = defaultAutoCommit

   def etDefaultTransactionIsolation(self, defaultTransactionIsolation):
      self.defaultTransactionIsolation = defaultTransactionIsolation

   def afterPropertiesSet(self):
      super.afterPropertiesSet()

      if self.defaultAutoCommit == None or self.defaultTransactionIsolation == None:
         try:
            con = super().obtainTargetDataSource().getConnection()
            if con:
               try:
                  self.checkDefaultConnectionProperties(con)
         except: # TODO: this should be some kind of SQLException
            print("Could not retrieve default auto-commit and transaction isolation settings", ex)
   
   # TODO: Make this syncronized: http://theorangeduck.com/page/synchronized-python
   def checkDefaultConnectionProperties(self, con):
      if self.defaultAutoCommit == None:
         self.defaultAutoCommit = con.getAutoCommit

      if self.defaultTransactionIsolation == None:
         self.defaultTransactionIsolation = con.getTransactionIsolation

   def getConnection(self):
      return LazyConnectionDataSourceProxy(  )

   class LazyConnectionInvocationHandler(object):
      
      def __init__(self, username = None, password = None):
         self.target = None
         self.autoCommit = defaultAutoCommit()
         self.transactionIsolation = defaultTransactionIsolation()
         self.username = username
         self.password = password

         self.closed = False

      def __getattribute__(self, method):
         
         # TODO: fill up possible method name 
         if method == "equals":
            pass
         elif method == "hashCode":
            pass

         if not self.hasTargetConnection():
               #TODO: fill up possible method name 
               if method == "toString":
                  pass
               elif method == "getAutoCommit":
                  pass
               else:
                  if self.closed:
                     raise Exception("Illegal operation: connection is closed")

         target = self.getTargetConnection(method)
         attr = object.__getattribute__(target, method)

         def newAttr(*args, **kwargs):  # 包装
            res = attr(*args, **kwargs)
            return res

         return newAttr

      def hasTargetConnection(self):
         return (self.target != None)

      def getTargetConnection(self, method):
         target = object.__getattribute__(self, "target")
         if target == None:
            print("Connecting to database for operation '" + method + "'")
            # Fetch physical Connection from DataSource.
            if self.username and self.password:
               super().obtainTargetDataSource().getConnection(self.username, self.password)
            else:
               super().obtainTargetDataSource().getConnection()
         
         # TODO: set other connection metadata
     