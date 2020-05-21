"""
This file is a part of My-PyChess application.
To run the online server, execute this file.

For more information, see ref/online.txt
"""

import random
import socket
import threading
import time
from urllib.request import urlopen

# Initialise a few global variables
VERSION = "v3.0.0"
START_TIME = time.perf_counter()

players = []
busyPpl = set()
total = 0

# Initialize the main socket
print("SERVER: INITIALIZING...")
mainSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainSock.bind(('0.0.0.0', 26104))
mainSock.listen(12)
print("SERVER: Successfully Started")
print("SERVER: Accepting connections on port 26104\n")

# Determine the Local IP and print to shell some useful info
IP = socket.gethostbyname(socket.gethostname())
if IP == "127.0.0.1":
    print("SERVER: This machine does not appear to be connected to a network.")
    print("SERVER: With this limitation, you can only serve the clients ")
    print(" who are on THIS machine. Use IP address 127.0.0.1\n")

else:
    print("SERVER: This machine has a local IP address", IP)
    print("SERVER: USE THIS IP IF THE CLIENT IS ON THE SAME NETWORK\n")
    
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

# A wrapper for socket recv, does not raise errors, returns message in desired
# format
def read(sock):
    try:
        msg = sock.recv(8)
        if msg:
            return msg.decode("utf-8").strip()
    except:
        pass
    return "quit"

# A wrapper for socket send, does not raise errors, buffers the message and
# sends it in encoded bytes.
def write(sock, msg):
    if msg:
        val = msg + (" " * (8 - len(msg)))
        try:
            sock.send(val.encode("utf-8"))
        except:
            pass

# Generates a random four digit number that is unique, based on the list of
# players
def genKey():
    key = random.randint(1000, 9999)
    for player in players:
        if player[1] == key:
            return getKey()
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
    for player in players:
        if player[1] == int(key):
            players.remove(player)

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
def onQuit(sock, key, close=True):
    write(sock, "close")
        
    try:
        sock.close()
    except OSError:
        print(f"SERVER: An error occured while PLAYER{key} quit, hopefully it")
        print(" is a minor issue.")
    rmKey(key)
    rmBusy(key)
    print(f"SERVER: PLAYER{key} has Quit")

# This simple function handles the chess match
def game(sock1, sock2):
    while True:
        msg = read(sock1)
        write(sock2, msg)
        if msg == "quit":
            break

# This is the function that is used as a Thread assigned to every player
# It handles the player's communiction
def player(sock, key):
    spamCnt = 0

    while True:
        try:
            msg = read(sock)

            if spamCnt > 60:
                print(f"SERVER: KICKED Player{key} for Spamming")
                onQuit(sock, key)
                return

            elif msg == "quit":
                print(f"Player{key}: Sent connection termination Message")
                onQuit(sock, key)
                return

            elif msg == "pStat":
                spamCnt += 1
                print(f"Player{key}: Made request for players Stats.")
                data = list(zip(*players))[1], list(busyPpl)
                if len(data[0]) - 1 in range(10):
                    write(sock, "enum" + str(len(data[0]) - 1))
                else:
                    onQuit(sock, key)
                    print(f"SERVER: KICKED Player{key}")
                    print("SERVER: Unknown server error has occured.")
                    print(" While the server has not crashed, a reboot is")
                    print(" needed. Please initiate kickall command and")
                    print(" proceed to reboot.")
                    return

                for i in data[0]:
                    if i != key:
                        if i in data[1]:
                            write(sock, str(i) + "b")
                        else:
                            write(sock, str(i) + "a")

            elif msg.startswith("rg"):
                spamCnt += 3
                print(f"Player{key}: Made request to play with Player{msg[2:]}")
                oSock = getByKey(msg[2:])
                if oSock is not None:
                    if int(msg[2:]) not in busyPpl:
                        mkBusy(key, msg[2:])
                        write(sock, "msgOk")
                        write(oSock, "rg" + str(key))
                        newMsg = read(sock)
                        if newMsg == "ready":
                            print(f"SERVER: Player{key} is in a game")
                            game(sock, oSock)
                            print(f"SERVER: Player{key} finished the game")
                            onQuit(sock, key)
                            return
                        elif newMsg == "quit":
                            print(f"Player{key}: Sent connection ending request")
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
                game(sock, oSock)
                print(f"SERVER: Player{key} finished the game")
                onQuit(sock, key)
                return

            elif msg.startswith("gmNo"):
                spamCnt += 1
                print(f"Player{key}: Rejected Player{msg[4:]} request")
                oSock = getByKey(msg[4:])
                write(oSock, "nostart")
                rmBusy(key, msg[4:])

            else:
                spamCnt += 5
                print(f"Player{key}: Sent Invalid message  - [{msg}]")
                write(sock, "errMsg")
                
        except:
            print("SERVER: An unknown error occured in the thread managing")
            print(" player", str(key) + ".")
            print(f"SERVER: KICKING PLAYER{key}")
            onQuit(sock, key)

# This is a Thread that runs in background to collect user input commands
def adminThread():
    global mainSock
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
                try:
                    PUBIP = urlopen("http://api.ipify.org/").read().decode()
                    print("SERVER: This machine has a public IP address", PUBIP)
                except:
                    print("SERVER: An error occurred while determining IP")

            elif msg.startswith("kick "):
                k = int(msg[5:].strip())
                sock = getByKey(k)
                if sock is not None:
                    onQuit(sock, k)
                    print(f"SERVER: KICKED player{k}")
                else:
                    print(f"SERVER: Player{k} does not exist")

            elif msg == "kickall":
                print("SERVER: Attempting to KICK everyone")
                for sock, key in players:
                    onQuit(sock, key)
                print("SERVER: All Clients kicked")
                
            elif msg == "quit":
                print("SERVER: Attempting to KICK everyone")
                for sock, key in players:
                    onQuit(sock, key)
                print("SERVER: All Clients kicked, closing the port now.")
                mainSock.close()
                print("SERVER: Port closed, exiting application - Bye")
                
            else:
                print(f"SERVER: Invalid command entered ('{msg}')")
                
        except:
            print("SERVER: An unknown error occured in Thread-1 (Admin input")
            print(" thread), silencing the issue as this is most probably")
            print(" caused by an invalid command.")

threading.Thread(target=adminThread).start()
while True:
    try:
        newSock, _ = mainSock.accept()
    except:
        break
    
    total += 1
    print("SERVER: CLIENT ATTEMPTING TO CONNECT")
    # TODO: Setup a read timeout so that it does not block here.
    if read(newSock) == VERSION:
        if len(players) < 10:
            key = genKey()
            print(f"SERVER: Connection Successful, assigned key - {key}")
            write(newSock, "GTag" + str(key))
            threading.Thread(target=player, args=(newSock, key)).start()
            players.append((newSock, key))
        else:
            print("SERVER: Server is busy, rejected connection")
            write(newSock, "errBusy")
            newSock.close()
    else:
        print("SERVER: Version Error occured, rejected connection")
        write(newSock, "errVer")
        newSock.close()

mainSock.close()