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
    myDb = None

    def __init__(self,rQ, userlist, cSocks):
        threading.Thread.__init__(self)
        self.rQ = rQ
        self.ul= userlist
        self.myDb = idb()
        self.cSocks = cSocks
        
        self.alive = threading.Event()
        self.alive.set()
        
        
        
        
    def sendMsgToAll(self,u,cmd):
        
        for user in self.ul:
            user.sendMessage(u+ ": "+" ".join(cmd))
               
    
    def isNicknameinBlacklist(self, nic):
        return self.myDb.isNicknameonBlacklist(nic)
    
    def login(self,u,cmd):
        
        if len(cmd) == 2 and not self.myDb.isNicknameonBlacklist(cmd[0]):
            user = cmd[0].strip()
            pw = cmd[1].strip()
            userdata = self.myDb.login(user,pw, u.address) # returned [id,privilege] or None
            if not userdata:
                return False
            else:
                u.nickname = user
                u.uid = userdata[0]
                u.privilege = int(userdata[1])
                u.loggedin = True
                return True
        elif len(cmd) == 1 and cmd[0].strip() == "guest":
            nick = self.myDb.loginGuest(u.address)
            cmd[0] = cmd[0].strip()
            if len(nick) == 2:
                u.nickname = nick[0]
                u.uid = int(nick[1])
                u.privilege = 0
                u.loggedin = True
                self.myDb.addActivity("login", u.address, u.uid, "Nickname: "+u.nickname)
                u.sendMessage("/nickname "+u.nickname)
                return True
        u.sendMessage("/exit")
        return False
        # return true or false
        
    def remUser(self,chash,cmd):
        remk = None
        for k in self.ul:
            if k.chash == chash:
                remk = k
            
                
        remk.socket.close()       
        if remk.uid != None:
            self.myDb.setOnline(remk.uid, 0, remk.nickname)
        if remk.uid != None:
            self.myDb.addActivity("logout", remk.address, remk.uid, "Nickname: "+remk.nickname)
        else:
            self.myDb.addActivity("logout", remk.address, -1, "Nickname: "+remk.nickname)
         
        if remk:
            self.cSocks.remove(remk.socket)
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
                if len(cmd)>=2:
                    chash = cmd[0]
                    cmd = eval(cmd[1].strip())
                    #cmd = cmd.split(" ")
                    #cmd[0]=cmd[0].strip()
                    user = self.getUserBycHash(chash)
                    if user:
                        if user.loggedin:
                            
                            if cmd[0]== "/send":
                                self.sendMsgToAll(user.nickname, cmd[1:])
                            
                            
                                
                            if user.privilege >=1: # registered
                                pass
                            if user.privilege >=2: # channeladmin
                                pass
                            if user.privilege >=3: # moderator
                                pass
                            if user.privilege >=4: # admin
                                pass
                                
                        else:
                            if cmd[0]== "/login" and ((len(cmd) == 2 and cmd[1].strip()=="guest" ) or len(cmd) == 3 ):
                                if not self.login(user, cmd[1:]):
                                    self.remUser(chash, cmd)
                                else:
                                    print(user.nickname+" just successfully logged in")
                            
                                
                        if cmd[0]== "/logout":
                                self.logout(chash, cmd[1:])
                        elif cmd[0]== "!exited":
                                self.remUser(chash, cmd[1:])
                    
                self.rQ.task_done()
            except Exception as ex:
                if len(ex.args)>0:
                    print(ex.args)
                    self.rQ.task_done()
                continue