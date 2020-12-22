from UserCredentialsDataSourceAdapter import UserCredentialsDataSourceAdapter

import threading
import time

ucdsa = UserCredentialsDataSourceAdapter()

def handleReq(username, password):
    ucdsa.setCredentialsForCurrentThread(username, password)
    print(ucdsa.JdbcUserCredentials.username, ucdsa.JdbcUserCredentials.password)
    assert ucdsa.JdbcUserCredentials.username == username and \
        ucdsa.JdbcUserCredentials.password == password

for i in range(100):
    t = threading.Thread(target = handleReq, args = ("User" + str(i), "Pwd" + str(i),))
    t.start()