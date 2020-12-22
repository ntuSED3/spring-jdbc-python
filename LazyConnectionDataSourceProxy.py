from DelegatingDataSource import DelegatingDataSource
class LazyConnectionDataSourceProxy(DelegatingDataSource):
   def __init__(self, targetDataSource = None):
      if targetDataSource != None:
         super().setTargetDataSource(targetDataSource)
         super().afterPropertiesSet()
         self.defaultAutoCommit = None
         self.defaultTransactionIsolation = None
   
   def setDefaultAutoCommit(self, defaultAutoCommit):
      self.defaultAutoCommit = defaultAutoCommit
   
   def DefaultAutoCommit(self):
      return self.defaultAutoCommit

   def setDefaultTransactionIsolation(self, defaultTransactionIsolation):
      self.defaultTransactionIsolation = defaultTransactionIsolation

   def DefaultTransactionIsolation(self):
      return self.defaultTransactionIsolation

   def afterPropertiesSet(self):
      super.afterPropertiesSet()

      if self.defaultAutoCommit == None or self.defaultTransactionIsolation == None:
         try:
            con = super().obtainTargetDataSource().getConnection()
            if con:
               try:
                  self.checkDefaultConnectionProperties(con)
               except:
                  pass
         except:
            # TODO: this should be some kind of SQLException
            print("Could not retrieve default auto-commit and transaction isolation settings")
   
   # TODO: Make this syncronized: http://theorangeduck.com/page/synchronized-python
   def checkDefaultConnectionProperties(self, con):
      # defaultAutoCommit and defaultTransactionIsolation should be con.isolation_level for sqlite3
      if self.defaultAutoCommit == None:
         self.defaultAutoCommit = False

      if self.defaultTransactionIsolation == None:
         self.defaultTransactionIsolation = False

   def getConnection(self):
      return LazyConnectionDataSourceProxy.LazyConnectionInvocationHandler(self)

   class LazyConnectionInvocationHandler(object):
      
      def __init__(self, outer_instance, username = None, password = None):
         self.outer_instance = outer_instance
         self.target = None
         self.autoCommit = outer_instance.DefaultAutoCommit()
         self.transactionIsolation = outer_instance.DefaultTransactionIsolation()
         self.username = username
         self.password = password

         self.closed = False

      def __getattr__(self, method):
         
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
         attr = target.__getattribute__(method)

         def newAttr(*args, **kwargs):  # 包装
            res = attr(*args, **kwargs)
            return res

         return newAttr

      def hasTargetConnection(self):
         return (self.target != None)

      def getTargetConnection(self, method):
         target = self.target
         if target == None:
            print("Connecting to database for operation '" + method + "'")
            # Fetch physical Connection from DataSource.
            if self.username and self.password:
               self.target = self.outer_instance.obtainTargetDataSource().getConnection(self.username, self.password)
            else:
               self.target = self.outer_instance.obtainTargetDataSource().getConnection()
         return self.target
         # TODO: set other connection metadata
     