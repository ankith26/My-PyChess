"""
This file is a part of My-PyChess application.
To run the online server, run this script.

For more information, see ref/online.txt

Level of development = BETA

IMPORTANT NOTE:
    Server.py needs atleast Python v3.6 to work.
"""

import random
import socket
import threading
import time
from urllib.request import urlopen

# Initialise a few global variables
VERSION = "v3.1.0"
START_TIME = time.perf_counter()

players = []
busyPpl = set()
lock = False
total = 0

# Initialize the main socket
print("SERVER: INITIALIZING...")
mainSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainSock.bind(("0.0.0.0", 26104))
mainSock.listen(16)
print("SERVER: Successfully Started.")
print("SERVER: Accepting connections on port 26104.\n")

# Determine the local IP and print to shell some useful info
IP = socket.gethostbyname(socket.gethostname())
if IP == "127.0.0.1":
    print("SERVER: This machine does not appear to be connected to a network.")
    print("SERVER: With this limitation, you can only serve the clients ")
    print(" who are on THIS machine. Use IP address 127.0.0.1", "\n")

else:
    print("SERVER: This machine has a local IP address -", IP)
    print("SERVER: USE THIS IP IF THE CLIENT IS ON THE SAME NETWORK.\n")

    print("SERVER: IF YOU WANT CLIENTS FROM OUTSIDE YOUR NETWORK TO CONNECT,")
    print(" USE THE SERVER'S PUBLIC IP OR DOMAIN NAME (IF APPLICABLE).")
    print(" PORT FORWARDING MUST BE ENABLED FOR THIS TO WORK, READ MORE IN")
    print(" ref/online.txt", "\n")

# A function to display elapsed time in desired format.
def getTime():
    sec = round(time.perf_counter() - START_TIME)
    minutes, sec = divmod(sec, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return f"{days} days, {hours} hours, {minutes} minutes, {sec} seconds"

# Used instead of socket.recv, because it returns the decoded message, handles
# TCP packet loss and other useful stuff
def read(sock, timeout=None):
    sock.settimeout(timeout)
    try:
        msg = sock.recv(8).decode("utf-8")
        if "X" in msg:
            return read(sock, timeout)

        if msg:
            return msg.strip()
    except:
        pass
    return "quit"

# Handle TCP packet loss by sending emergency buffer. Recurse the fuction as
# packet loss could happen with emergency buffer too.
def send_error_buffer(sock, bufsize):
    sent = sock.send(("X" * bufsize).encode("utf-8"))
    if sent < bufsize:
        send_error_buffer(sock, bufsize - sent)

# A function to message the server, this is used instead of socket.send()
# beacause it buffers the message, handles packet loss and does not raise
# exception if message could not be sent and returns message in desired format
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

# Generates a random four digit number that is unique, based on the list of
# players
def genKey():
    key = random.randint(1000, 9999)
    for player in players:
        if player[1] == key:
            return genKey()
    return key

# Given a players key, returns the sock object for the player
# Returns None if player does not exist
def getByKey(key):
    for player in players:
        if player[1] == int(key):
            return player[0]

# Given key, removes the player from player list.
def rmKey(key):
    global players
    players.remove((getByKey(key), key))

# Makes a player busy, ie puts the player's key in a list of busy people
def mkBusy(*keys):
    global busyPpl
    for key in keys:
        busyPpl.add(int(key))

# Makes a player active, ie removes the player's key from the list of busy
def rmBusy(*keys):
    global busyPpl
    for key in keys:
        busyPpl.discard(int(key))

# The function that is called when player quits, does cleanup
def onQuit(sock, key):
    write(sock, "close")
    rmKey(key)
    rmBusy(key)
    sock.close()

    print(f"SERVER: PLAYER{key} has Quit")

# This simple function handles the chess match. Returns after game ended
# Returns True if player abandoned the match, false otherwise.
def game(sock1, sock2):
    while True:
        msg = read(sock1)
        write(sock2, msg)
        if msg == "quit":
            return True

        elif msg in ["draw", "resign", "end"]:
            return False

# This is the function that is used as a Thread assigned to every player.
# It handles the player's communiction with server.
def player(sock, key):
    try:
        while True:
            msg = read(sock)

            if msg == "quit":
                onQuit(sock, key)
                return

            elif msg == "pStat":
                print(f"Player{key}: Made request for players Stats.")
                data = list(zip(*players))[1], list(busyPpl)
                if len(data[0]) - 1 in range(10):
                    write(sock, "enum" + str(len(data[0]) - 1))

                for i in data[0]:
                    if i != key:
                        if i in data[1]:
                            write(sock, str(i) + "b")
                        else:
                            write(sock, str(i) + "a")

            elif msg.startswith("rg"):
                print(f"Player{key}: Made request to play with Player{msg[2:]}")
                oSock = getByKey(msg[2:])
                if oSock is not None:
                    if int(msg[2:]) not in busyPpl:
                        mkBusy(key, msg[2:])
                        write(sock, "msgOk")
                        write(oSock, "gr" + str(key))
                        newMsg = read(sock)
                        if newMsg == "ready":
                            print(f"SERVER: Player{key} is in a game")
                            if game(sock, oSock):
                                onQuit(sock, key)
                                return
                            else:
                                rmBusy(key)
                                print(f"SERVER: Player{key} finished the game")

                        elif newMsg == "quit":
                            onQuit(sock, key)
                            write(oSock, "quit")
                            return

                    else:
                        print(f"SERVER: Player{key} requested busy player")
                        write(sock, "errPBusy")
                else:
                    print(f"SERVER: Player{key} Sent invalid key")
                    write(sock, "errKey")

            elif msg.startswith("gmOk"):
                print(f"Player{key}: Accepted Player{msg[4:]} request")
                oSock = getByKey(msg[4:])
                write(oSock, "start")
                print(f"SERVER: Player{key} is in a game")
                if game(sock, oSock):
                    onQuit(sock, key)
                    return
                else:
                    rmBusy(key)
                    print(f"SERVER: Player{key} finished the game")

            elif msg.startswith("gmNo"):
                print(f"Player{key}: Rejected Player{msg[4:]} request")
                oSock = getByKey(msg[4:])
                write(oSock, "nostart")
                rmBusy(key, msg[4:])

    except Exception as e:
        print(f"SERVER: An error occured in the thread managing player{key}.")
        print("SERVER: Here is the error message if you are interested")
        print("SERVER(ERROR):", e)
        print(f"SERVER: KICKING PLAYER{key}")
        onQuit(sock, key)

# This is a Thread that runs in background to collect user input commands
def adminThread():
    global mainSock, players, lock
    while True:
        try:
            msg = input().strip()

            if msg == "report":
                print("SERVER: ")
                print(f" {len(players)} players are online right now,")
                print(f" {len(players) - len(busyPpl)} are active.")
                print(f" Server is running {threading.active_count()} threads,")
                print(f" So far, {total} connections have been made.")
                print(f" Time elapsed since last reboot: {getTime()}")
                if players:
                    print(" LIST OF PLAYERS:")
                    for cnt, (_, player) in enumerate(players):
                        if player not in busyPpl:
                            print(f" {cnt+1}. Player{player}, Status: Active")
                        else:
                            print(f" {cnt+1}. Player{player}, Status: Busy")

            elif msg == "mypublicip":
                print("SERVER: Determining public IP, please wait....")
                try:
                    PUBIP = urlopen("http://api.ipify.org/").read().decode()
                    print("SERVER: This machine has a public IP address", PUBIP)
                except:
                    print("SERVER: An error occurred while determining IP")
                    
            elif msg == "lock":
                if lock:
                    print("SERVER: Aldready in locked state")
                else:
                    lock = True
                    print("SERVER: Locked server, no one can join now.")
                    
            elif msg == "unlock":
                if lock:
                    lock = False
                    print("SERVER: Unlocked server, all can join now.")
                else:
                    print("SERVER: Aldready in unlocked state.")

            elif msg.startswith("kick "):
                k = int(msg[5:].strip())
                sock = getByKey(k)
                if sock is not None:
                    write(sock, "close")
                    sock.close()
                    print(f"SERVER: KICKED player{k}")
                else:
                    print(f"SERVER: Player{k} does not exist")

            elif msg == "kickall":
                lock = True
                print("SERVER: Attempting to KICK everyone, please wait.")
                latestplayers = list(players)
                for sock, key in latestplayers:
                    write(sock, "close")
                    sock.close()
                    
                while threading.active_count() > 2 or players or busyPpl:
                    time.sleep(0.1)
                    
                print("SERVER: All Clients kicked")
                lock = False

            elif msg == "quit":
                lock = True
                print("SERVER: Attempting to KICK everyone, please wait.")
                latestplayers = list(players)
                for sock, key in latestplayers:
                    write(sock, "close")
                    sock.close()
                    
                while threading.active_count() > 2 or players or busyPpl:
                    time.sleep(0.1)
                    
                print("SERVER: All Clients kicked. Closing port now.")
                mainSock.close()
                print("SERVER: Exiting application - Bye") 
                return

            else:
                print(f"SERVER: Invalid command entered ('{msg}')")

        except Exception as e:
            print("SERVER: An unknown error occured in Thread-1 (Admin input")
            print(" thread), silencing the issue as this is most probably")
            print(" caused by an invalid command.")
            print("SERVER: Here is the error message if you are interested -")
            print("SERVER(ERROR):", e)


threading.Thread(target=adminThread).start()
while True:
    try:
        newSock, _ = mainSock.accept()
    except:
        break

    total += 1
    print("SERVER: CLIENT ATTEMPTING TO CONNECT")

    if read(newSock, 3) == VERSION:
        if len(players) < 10:
            if not lock:
                key = genKey()
                players.append((newSock, key))
                print(f"SERVER: Connection Successful, assigned key - {key}")
                write(newSock, "GTag" + str(key))
                threading.Thread(target=player, args=(newSock, key)).start()
                
            else:
                print("SERVER: Server is locked, rejected connection")
                write(newSock, "errLock")
                newSock.close()
        else:
            print("SERVER: Server is busy, rejected connection")
            write(newSock, "errBusy")
            newSock.close()
    else:
        print("SERVER: Version error occured, rejected connection")
        write(newSock, "errVer")
        newSock.close()

mainSock.close()
