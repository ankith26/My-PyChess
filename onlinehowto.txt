===============================================================
                        Online Gameplay
                        ---------------
===============================================================
Online Gameplay consists of two elements, client and server.

CLIENT: It is the machine that runs My-PyChess code.
SERVER: It is a machine that accepts connections from different clients(upto 10)

Back when I was actively working on this project, the networking element of this
app was made with security in mind. I had not used the python "pickle" module,
which is normally used in such applications. This has security risks associated.

The server keeps absolutely NO DATA of any user that connects to it.
No names, accounts, emails, IP address, Location - nothing. PRIVACY IS RESPECTED.

The client and server speak over Raw TCP protocol with no sort of encryption.
This means that any bad guys may read the messages that the client and server
send to one another. But the best part is the fact that the client and server DO NOT
EXCHANGE ANY SENSITIVE DATA. This means that the information is practically useless
for the bad guys. So they will not invest their time and efforts to do such things.
If they did so, they would be in major dissapointment.

The public global test server is not being hosted anymore.

==========================================================================
                    SELF-HOSTING MY_PYCHESS SERVER
==========================================================================

HOW TO RUN SERVER:
==================
Run server.py, as simple as that!
Python v3.6 or above has to be used.

HOW TO CONNECT TO THIS SERVER:
==============================
The server and client must be connected to the same router. When the server runs,
it will message it's IP address in the shell. Enter this in the client's menu.
IT IS TO BE NOTED THAT THE IP ADDRESS IT GIVES IS THE PRIVATE IP ADDRESS, NOT PUBLIC

If for some reason, you want the server's PUBLIC IP ADDRESS,
I have covered that part below. This will not be required for most usecases.

HOW TO CONFIGURE THE SERVER (FOR ADVANCED USAGE):
=================================================

On top of server.py, there are two constants - LOG and IPV6.
They are set to False by default.
IT IS RECOMMENDED YOU DO NOT CHANGE THESE.
But if you really need to, then you can change those.

If you set 'LOG = True', the server will log it's output to a file. The file
will be named by the current date and time of logging. This feature is not
recommended because it will consume more CPU power and RAM than when it is not
logging.

If you set 'IPV6 = True', the server will start in IPv6 mode. This means that
any client that is using the IPv6 protocol can connect to the server. Both client
and server must support IPv6 for this to work. By default, the server opens in
IPv4 mode, which is the protocol that is supported by most of the systems of today.

IPv6 is a more modern protocol, that will take time to be widely adopted because
most of the internet runs on IPv4.

MANAGING THE SERVER WHILE IT IS RUNNING
=======================================

When the server is running, it is constantly messaging you whatever is going
on. You can enter commands to the server.

Commands are listed below:
1) report
    Gives the current status of the server with useful information like the
    number of threads the server is running, number of people online etc etc

2) mypublicip
    Enter this command to know the server's public IP Address.

3) lock
    This will put the server in a "locked" state. After this, anyone will not
    be able to connect to the server. This will not affect anyone who is
    aldready connected to the server.

4) unlock
    This will "unlock" the server, the server that is locked will be "unlocked",
    then anybody can connect to the server. This is the default state of the
    server.

3) kickall
    Kick EVERYONE connected to the server.

4) kick <id1> [<id2> <id3> ...]
    Kick a particular player (whose id is <id1>).
    Can specify more than one id.
    example: 'kick 3294', 'kick 9492 2839 5138', 'kick 9327 4392', etc

5) quit
    Enter this to stop the server and quit. Recommended way of closing server.

IF YOU WANT TO CLOSE THE SERVER WHILE IT IS RUNNING, ENTER "quit" IN SHELL.
TRYING TO FORCE CLOSE THE SERVER MAY GIVE UNEXPECTED RESULTS TO CLIENTS
CONNECTED.

WHAT IS AN ID, WHAT IS A KEY?
=============================
When the clients connect to server, the server issues the client a unique
4-digit number as their 'ID' or 'key'.