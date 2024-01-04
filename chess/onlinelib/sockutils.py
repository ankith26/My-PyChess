'''
This file is a part of My-PyChess application.
In this file, we define a few utility funtions and wrappers for socket related
stuff.
'''
import queue
import socket

q = queue.Queue()
isdead = True

# Define a background thread that continuously runs and gets messages from
# server, formats them and puts them into a queue (IO buffer).
def bgThread(sock):
    global isdead
    isdead = False
    while True:
        try:
            msg = sock.recv(1024).decode("utf-8").strip()
        except:
            break
        
        if not msg or msg == "close":
            break
        
        if msg != "........":
            q.put(msg)
    isdead = True

# Returns wether background thread is dead and IO buffer is empty.
def isDead():
    return q.empty() and isdead

# A function to read messages sent from the server, reads from queue.
def read():
    if isDead():
        return "close"
    return q.get()

# Check wether a message is readable or not
def readable():
    if isDead():
        return True
    return not q.empty()

# Flush IO Buffer. Returns False if quit command is encountered. True otherwise.
def flush():
    while readable():
        if read() == "close":
            return False
    return True
 
# A function to message the server, this is used instead of socket.send()
# beacause it buffers the message, handles packet loss and does not raise
# exception if message could not be sent
def write(sock, msg):
    if msg:
        buffedmsg = msg + (" " * (8 - len(msg)))
        try:
            sock.sendall(buffedmsg.encode("utf-8"))
        except:
            pass
    
# A function to query the server for number of people online, returns a list
# of players connected to server if all went well, None otherwise.
def getHistory(sock):
    if not flush():
        return None
    write(sock, "his")
    msg = read()
    if msg.startswith("xnum"):
        data = []
        for i in range(int(msg[4:6])):
            newmsg = read()
            if newmsg == "close":
                return None
            else:
                data.append(newmsg)
        return tuple(data)
    
def getPlayers(sock):
    if not flush():
        return None
    
    write(sock, "pStat")
    
    msg = read()
    if msg.startswith("enum"):
        data = []
        for i in range(int(msg[-1])):
            newmsg = read()
            if newmsg == "close":
                return None
            else:
                data.append(newmsg)
        return tuple(data)