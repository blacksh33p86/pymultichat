'''
Created on 21.10.2013

@author: developer
'''

import threading
import Queue


class clistener(threading.Thread):
    

    def __init__(self,chash, cmdQ,rQ,sock): 
        threading.Thread.__init__(self)
        self.chash = chash 
        self.cmdQ = cmdQ
        self.rQ = rQ
        self.sock = sock
        self.alive = threading.Event()
        self.alive.set()
        
    def stop(self):
        self.rQ.put([self.chash,"!exited clientSockClose"])
        self.sock.close()
        self.alive.clear()
 
    def run(self): 
        self.sock.send("\nWelcome!\n")
        while self.alive.isSet():
            try:
                # Queue.get with timeout to allow checking self.alive
                data = self.sock.recv(4096)
                if not data:
                    raise Exception("Connection to Client lost")
                self.rQ.put([self.chash,data])
                
                
            except:
                self.sock.close()
                self.rQ.put([self.chash,"!exited clientSockClose"])
                self.alive.clear()
        