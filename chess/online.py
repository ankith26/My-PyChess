'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for online section of this
application.

We use the "online lib" module
'''
import socket
import threading

from chess.onlinelib import *

VERSION = "v3.2.0"
PORT = 26104

# This is a main function that calls all other functions, socket initialisation
# and the screen that appears just after online menu but just before online lobby.
def main(win, addr, load, ipv6=False):
    showLoading(win)
    
    if ipv6:
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        servaddr = (addr, PORT, 0, 0)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servaddr = (addr, PORT)

    try:
        sock.connect(servaddr)

    except:
        showLoading(win, 1)
        return 1

    thread = threading.Thread(target=bgThread, args=(sock,))
    thread.start()
    write(sock, "PyChess")
    write(sock, VERSION)

    ret = 1
    msg = read()   
    if msg == "errVer":
        showLoading(win, 2)

    elif msg == "errBusy":
        showLoading(win, 3)

    elif msg == "errLock":
        showLoading(win, 4)

    elif msg.startswith("key"):
        ret = lobby(win, sock, int(msg[3:]), load)
        
    else:
        print(msg)
        showLoading(win, 5)

    write(sock, "quit")
    sock.close()
    thread.join()
    flush()
    
    if ret == 2:
        showLoading(win, -1)
        return 1
    return ret
