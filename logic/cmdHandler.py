'''
Created on 21.10.2013

@author: developer
'''
import threading


'''Databaseinterface'''
from dbinterfaces.mysqldb import idb
#from dbinterfaces.couchdb import idb NOT IMPLEMENTED YET


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
        
        
        
        
    def sendMsgToAll(self,u,cmd):
        
        for user in self.ul:
            user.sendMessage(u+ ": "+" ".join(cmd))
            
           
    
    def login(self,chash,cmd):
        user = cmd[1]
        pw = cmd[2]
        
    def remUser(self,chash,cmd):
        remk = None
        for k in self.ul:
            if k.chash == chash:
                remk = k
                if not remk.th == None:
                    remk.th.join()
       
               
        
        
        # dblogout /chanlogout
        self.ul.remove(remk)
        
    def logout(self,chash,cmd):
        self.remUser(chash, cmd)
    
    def getUsernameBycHash(self,chash):
        
        for a in self.ul:
            
            if a.chash == chash:
                return a.nickname
           
        return "<missing>"
    
    def getUserBycHash(self,chash):
        for a in self.ul:
            
            if a.chash == chash:
                return a
           
        return None
        
    def run(self): 
        while self.alive.isSet():
            try:
                cmd = self.rQ.get(True,0.1)
                print(cmd)
                chash = cmd[0]
                cmd = cmd[1]
                cmd = cmd.split(" ")
                
                user = self.getUserBycHash(chash)
                
                if user.loggedin:
                    
                    if cmd[0]== "/send":
                        self.sendMsgToAll(user.nickname, cmd[1:])
                    elif cmd[0]== "!exited":
                        self.remUser(chash, cmd[1:])
                    elif cmd[0]== "/logout":
                        self.logout(chash, cmd[1:])
                        
                    if user.privilege >=1: # registered
                        pass
                    if user.privilege >=2: # channeladmin
                        pass
                    if user.privilege >=3: # moderator
                        pass
                    if user.privilege >=4: # admin
                        pass
                        
                else:
                    if cmd[0]== "/login" and ((len(cmd) == 2 and cmd[1]=="guest" ) or len(cmd) == 3 ):
                        self.login(user, cmd[1:])
                    else:
                        self.remUser(chash, cmd)
                
                self.rQ.task_done()
            except Exception as ex:
                if len(ex.args)>0:
                    print(ex.args)
                continue