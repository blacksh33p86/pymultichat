'''
Created on 21.10.2013

@author: developer
'''
import threading
import couchdb

class cmdHandler(threading.Thread):
    '''
    classdocs
    '''
    

    def __init__(self,rQ, userlist):
        threading.Thread.__init__(self)
        self.rQ = rQ
        self.ul= userlist
        
        self.alive = threading.Event()
        self.alive.set()
        
        self.couch = couchdb.Server()
        
        
    def sendMsgToAll(self,u,cmd):
        
        for user in self.ul:
            user.sendMessage(u+ ": "+" ".join(cmd))
            
           
    
    def login(self,chash,cmd):
        user = cmd[1]
        pw = cmd[2]
        
    
    def logout(self,u,cmd):
        pass
    
    def getUsernameBycHash(self,chash):
        
        for a in self.ul:
            
            if a.chash == chash:
                return a.nickname
           
        return "<missing>"
        
    def run(self): 
        while self.alive.isSet():
            try:
                cmd = self.rQ.get(True,None)
                print(cmd)
                chash = cmd[0]
                cmd = cmd[1]
                cmd = cmd.split(" ")
                
                
                if cmd[0]== "/send":
                    self.sendMsgToAll(self.getUsernameBycHash(chash), cmd[1:])
                if cmd[0]== "/login":
                    self.sendMsgToAll(chash, cmd[1:])
                
                self.rQ.task_done()
            except:
                continue