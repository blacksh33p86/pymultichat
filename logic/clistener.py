'''
Created on 21.10.2013

@author: developer
'''
import hashlib
import threading
import Queue
import select
from logic.useritem import useritem


class clistener(threading.Thread):
    

    def __init__(self,sSock,rQ,ul): 
        threading.Thread.__init__(self)
        
        self.sSock = sSock
        self.rQ = rQ
        self.userlist = ul
        self.alive = threading.Event()
        self.alive.set()
        self.hasher = None
        self.cSocks = []
        
           
        
    def stop(self):
        #self.rQ.put([self.chash,"!exited clientSockClose"])
        for s in self.socks:
            s.close()
        self.alive.clear()
        
 
    def run(self): 
        
        while self.alive.isSet():
            try:
                inputready,outputready,exceptready = select.select([self.sSock]+self.cSocks,[],[]) 
                for sock in inputready:
                    
                    if sock == self.sSock:
                        s, addr = sock.accept()
                        
                        p = useritem(s,addr[0]+":"+str(addr[1]),self.rQ)
                        self.cSocks.append(s)
                        self.userlist.append(p)
                        s.send("\nWELCOME!\n")
                        
                    if sock in self.cSocks:  
                        
                        self.hasher = hashlib.md5()
                        self.hasher.update(sock.getpeername()[0]+":"+str(sock.getpeername()[1]))
                        chash = self.hasher.hexdigest()
                        
                        
                        
                        data = str(sock.recv(4096))
                        
                        if not data:
                            raise Exception("Connection to Client lost")
                        
                        
                        self.rQ.put([chash,data])
                            
                        
            except:
                #if self.sock.isAlive():
                sock.close()
                self.rQ.put([chash,"!exited clientSockClose"])
                        
                