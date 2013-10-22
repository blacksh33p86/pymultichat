
import Queue
from logic.clistener import clistener
import hashlib

"""
Clientbefehle:



"""

class useritem(object):
    
    
    
    def __init__(self,socket,address,rQ):
        self.socket = socket
        self.address = address
        self.rQ = rQ
        self.cmdQ = Queue.Queue()
        self.nickname = "<missing>"
        self.uid = None
        
        m = hashlib.md5()
        m.update(address[0]+":"+str(address[1]))
 
        self.chash = m.hexdigest()
        
        self.privilege = 0
        self.loggedin = False
        self.th = None
        
        
        
    def sendMessage(self,msg):
        self.socket.send(msg)
    
    def createListener(self):
        self.th = clistener(self.chash,self.cmdQ,self.rQ,self.socket).start()