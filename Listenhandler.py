import socket
import threading
import Queue
from logic.useritem import useritem
from logic.cmdHandler import cmdHandler
from logic.clistener import clistener

if __name__ == "__main__":
    
    userlist = []
    cSocketlist = []
    rQueue = Queue.Queue()
    exitflag=True
    
    cmdH = cmdHandler(rQueue,userlist,cSocketlist)
    cmdH.start()
    
    
    
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 3232
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
    
    cSockH = clistener(server_socket,rQueue,userlist,cSocketlist)
    cSockH.start()
    
    cmdH.join()
    
   
        
        
       
        
        
        