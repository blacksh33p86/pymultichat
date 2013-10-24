'''
Created on 23.10.2013

@author: developer
'''

import MySQLdb
import hashlib

class idb(object):
   
    connection = None
    cursor = None
    salt = None
    

    def __init__(self):
        self.dbhost = "localhost"
        self.dbuser = "chatadmin"
        self.dbpw = "test"
        self.dbname = "chatsrv"
        self.connection = MySQLdb.connect(self.dbhost,self.dbuser, self.dbpw, self.dbname)
        self.cursor = self.connection.cursor() 
        self.salt = "b70915cd1cae7d84b997d1248c857f0a"
        
        
    def isNicknameonBlacklist(self,nic):
        count = self.cursor.execute("SELECT id FROM cs_nicknameblacklist WHERE nickname LIKE '%"+nic+"%'")
        if count>0:
            return True
        else:
            return False
        
    def login(self,user,pw, address):
        m = hashlib.md5()
        m.update(pw+self.salt)
        saltedpw = m.hexdigest()
        
        self.cursor.execute("SELECT id,privilege FROM cs_users WHERE nickname='"+user+"' AND password='"+saltedpw+"'")
        
        for row in self.cursor:
            self.setOnline(row[0],1) # set online
            self.addActivity("login", address, row[0], "Nickname: "+user)# set activity
            return row
                
        return None
    
    def setOnline(self,uid,value):
        #conn = MySQLdb.connect(self.dbhost,self.dbuser, self.dbpw, self.dbname)
        #cur = conn.cursor() 
        self.cursor.execute("UPDATE cs_users SET onlinestatus="+str(value)+" WHERE id="+str(uid))
        self.connection.commit()
        #print("UPDATE cs_users SET onlinestatus="+str(value)+" WHERE id="+str(uid))
        #conn.close()
    
    def addActivity(self,action, con, uid, val):
        query = "INSERT INTO cs_activities (action,connection,userid,value) VALUES ('%s','%s',%i,'%s')" % (action,con,uid,val)
        self.cursor.execute(query)
        self.connection.commit()
        