'''
This file is a part of My-PyChess application.
In this file, we define a few utility funtions and wrappers for socket related
stuff.

Level of development = STABLE
'''
import queue
import socket

q = queue.Queue()

# Define a background thread that continuously runs and gets messages from
# server, formats them and puts them into a Queue.
def bgThread(sock):
    try:
        while True:
            msg = sock.recv(8).decode("utf-8")
            
            if not msg:
                if q.empty():
                    q.put("close")
                return
            
            if "X" not in msg:
                q.put(msg.strip())
    except:
        if q.empty():
            q.put("close")

# A function to read messages sent from the server, read from queue.
def read():
    return q.get()

# Check wether server sent message or not
def readable():
    return not q.empty()

# Flush IO Buffer. Use function sparingly.
def flush():
    while readable():
        read()

# Handle TCP packet loss by sending emergency buffer. Recurse the fuction as
# packet loss could happen with emergency buffer too.
def send_error_buffer(sock, bufsize):
    sent = sock.send(("X" * bufsize).encode("utf-8"))
    if sent < bufsize:
        send_error_buffer(sock, bufsize - sent)

# A function to message the server, this is used instead of socket.send()
# beacause it buffers the message, handles packet loss and does not raise
# exception if message could not be sent
def write(sock, msg):
    if msg:
        buffedmsg = msg + (" " * (8 - len(msg)))
        try:
            sent = sock.send(buffedmsg.encode("utf-8"))
            if sent < 8:
                send_error_buffer(sock, 8 - sent)
                write(sock, msg)
        except:
            pass
    
# A function to query the server for number of people online, returns a list
# of players connected to server if all went well, else None.
def getPlayers(sock):
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