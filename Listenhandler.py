import socket
import threading
import Queue
from logic.useritem import useritem
from logic.cmdHandler import cmdHandler


if __name__ == "__main__":
    
    userlist = []
    rQueue = Queue.Queue()
    exitflag=True
    
    cmdH = cmdHandler(rQueue,userlist).start()
    
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 3232
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
    
    while exitflag:
        
        cSock, addr = server_socket.accept()
        p = useritem(cSock,addr,rQueue)
        p.createListener()
        userlist.append(p)
        
        