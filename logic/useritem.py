
import Queue
import hashlib

"""
Clientbefehle:



"""

class useritem(object):
    
    
    
    def __init__(self,socket,address,rQ):
        self.socket = socket
        self.address = address
        self.rQ = rQ
        
        self.nickname = "<missing>"
        self.uid = None
        
        m = hashlib.md5()
        m.update(self.address)
        
        self.chash = m.hexdigest()
        
        self.privilege = 0
        self.loggedin = False
       # self.th = ""
        
        
        
    def sendMessage(self,msg):
        self.socket.send(msg)
    
    
        