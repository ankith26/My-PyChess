'''
This file is a part of My-PyChess application.
In this file, we manage the chess gameplay for online section of this
application.

Level of development = BETA
'''
import threading

from chess.onlinelib import *

VERSION = "v3.1.0"

# This is a main function that controls all other functions, socket initialisation
# and the screen that appears just after online menu but just before online lobby.
def main(win, addr, LOAD):
    if addr is None:
        return

    showLoading(win)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((addr, 26104))
        
    except:
        showLoading(win, 0)
        return

    thread = threading.Thread(target=bgThread, args=(sock,))
    thread.start()
    write(sock, VERSION)
    
    msg = read()
    if msg == "errVer":
        showLoading(win, 1)
        
    elif msg == "errBusy":
        showLoading(win, 2)
        
    elif msg == "errLock":
        showLoading(win, 3)
        
    elif msg.startswith("GTag"):
        lobby(win, sock, int(msg[4:]), LOAD)
        
    sock.close()
    thread.join()
    flush()