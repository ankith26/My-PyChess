# My-PyChess
This is a fully featured chess app written purely in Python using Pygame Library.

Click [here](/screenshots.md) to see a few screenshots of My-PyChess!

Interested in pygame game development but think that MyPychess code is too hard for you to understand, no problem. I have released a [lite implementation](http://github.com/ankith26/My-PyChess-lite/) of My-PyChess, that focuses just on chess programming - Free from all the code for menus, singleplayer, online etc. 

But if you are just interested in chess, download this app.

My-PyChess supports Python v3.5 and above (server.py needs atleast v3.6).
This app needs the **pygame** library to be intalled in your machine.

To install, simply run 'pip3 install pygame' in the command line.
Pip command needs to be on your machine for this to work.

Then, run the **pychess.py** file. Trying to run any other file will not run the game.

Those who are running older versions of this app, must upgrade to the latest version from github. 

## How to customise the game Using Preferences
- In the main game menu, click preferences.
- Hover over each name to know more about them.
1) Sounds: When this is True, sounds are enabled.
2) Flip: When this is True, it shows the chess board from the perspective of the player who is playing, otherwise shows a constant board with white at the bottom.
3) SlideShow: When this is True, it will show a slideshow of images on main menu (recommended to be True, look better).
4) Show moves: When this is True, it will show all legal move options for a selected piece during gameplay (recommended to be True, highly helpful for beginners (my favourite feature)).
5) Undo: When this is True, it allows users to undo.

- You can also open res/preferences.txt and edit the file there.

## Features
- Clean GUI with a lot of menus for ease of use.
- It allows users to make only valid moves.
- It does not allow users to make moves that puts the user's king at check.
- It detects check, checkmate, stalemate and informs user.
- It supports things like castling, pawn promotion, enpassent etc.
- It supports saving and loading games.
- It has single player mode with two different types.
- It has online player mode.
- It has a preference menu where, you can customize the game to meet your needs.

## What's new in this Version 3.1
- Added basic Sounds (beta).
- Added draw and resign option to online gameplay.
- Added a simple "About menu".
- Added compatibility for python v3.5 (server.py still needs python v3.6 to work)
- Many many changes to GUI throughout the app, including more prompt messages.
- Upgraded preferences.
- Fixed a small issue in move animations, added a new startgame animation.
- Fixed a bug where undo in singleplayer after game ended would give weird results.
- Fixed many bugs in online mode (server), made server robust to TCP packet loss among other things.

## Highlights of v3.0, the latest major release.
- The code was revamped and restructured, fixing minor bugs and MAJOR PERFORMANCE IMPROVEMENTS.
- EnPassant, undo and screenflip were added.
- UI for loadGame menu was revamped, UI for preference menu was simplified.
- Online play was added. This features a ONLINE LOBBY and support upto 10 people to play chess (read more in ref/online.txt)
- Singleplayer saw BIG UPGRADES: A Good Menu, ability to play with a decent PYTHON CHESS ENGINE.
- Now, you can play against STOCKFISH CHESS ENGINE (see stockfishchess.org). My-PyChess will act as an interface to give you this singleplayer mode.

Click [here](/CHANGELOG.md) to see full changelog.

## What's Next

- Athough most of the features I had wanted in My-PyChess have been implemented in v3.0, there is still lot of room for improvement.
- Some of those are listed here.
1. Implement a game timer in chess.

2. Improvise the GUI/interface in some places.

3. Add a chess howto. 

3. Improve the TextBox in the online menu.

4. Save games in PGN format.

- There are many more in this list, but if you have any ideas, bug-reports or suggestions, feel free to use the issues section to communicate with me.
