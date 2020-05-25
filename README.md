# My-PyChess
This is a fully featured chess app written purely in Python using Pygame Library.

[Click here](/screenshots.md) to see a few screenshots of My-PyChess!

Interested in pygame game development but think that MyPychess code is too hard for you to understand, no problem. I have released a [lite implementation](http://github.com/ankith26/My-PyChess-lite/) of My-PyChess, that focuses just on chess programming - Free from all the code for menus, singleplayer, online etc. 

But if you are just interested in chess, download this app.

IMPORTANT NOTE: This game is best played on a 720p screen, 768p screen or 1080p screen. If you are on a 4K screen, you will get a very small window. In the next update, I will hopefully fix the resolution.

This app needs the **pygame** library to be intalled in your machine.

To install, simply run 'pip3 install pygame' in the command line.
Pip command needs to be on your machine for this to work.

Then, run the **pychess.py** file. Trying to run any other file will not run the game.

## How to customise the game Using Preferences
- In the main game menu, click preferences.
- Hover over each name to know more about them
- Here you have a few settings(more coming soon).
1) Placeholder: Coming Soon!
2) Flip: When this is True, it shows the chess board from the perspective of the player who is playing, otherwise shows a constant board with white at the bottom.
3) SlideShow: When this is True, it will show a slideshow of images on main menu (recommended to be True, look better).
4) Show moves: When this is True, it will show all legal move options for a selected piece during gameplay (recommended to be True, highly helpful for beginners (my favourite feature)).
5) Undo: When this is True, it allows users to undo

- You can also open res/preferences.txt and edit the file there (not recommended to do unless you know what you are doing, it might spoil the app if you do it the wrong way).

## Features
- Clean GUI with a lot of menus for ease of use.
- It allows users to make only valid moves.
- It does not allow users to make moves that puts the user's king at check.
- It detects check, checkmate, stalemate and informs user.
- It supports things like castling, pawn promotion, enpassent etc.
- It supports saving and loading games.
- It has single player mode with two different modes.
- It has online player mode.
- It has a preference menu where, you can customize the game to meet your needs.

## What's new in this version 3.0
- THIS IS THE BIGGEST RELEASE OF MY-PYCHESS EVER RELEASED.
- The code now comes with MIT License instead of the GPL-3 which came with v2.2
- The code was revamped and restructured, fixing minor bugs and MAJOR PERFORMANCE IMPROVEMENTS.
- On my PC, v2.2 ran at 25 fps, while this upgrade allows it to run at over 200 fps if fps is not constrained.
- Code is now more easy to understand with code comments throughout the code.
- EnPassant was added (finally).
- Undo moves option was added.
- UI for loadGame menu was revamped, UI for preference menu was simplified.
- Screen flip was added (so that both players get to play from their perspective).
- Save/load games with a new way of storing gamedata.

## BIG CHANGES THAT CAME IN VERSION 3.0

- Online play was added. This features a ONLINE LOBBY and support upto 10 people to play chess (read more in ref/online.txt)
- Singleplayer saw BIG UPGRADES: A Good Menu, ability to play with a decent PYTHON CHESS ENGINE.
- Now, you can play against STOCKFISH CHESS ENGINE (see stockfishchess.org). My-PyChess will act as an interface to give you this singleplayer mode. Included with this release, a good menu for stockfish and stockfish install/configure menu to help with installing and configuring stockfish with My-PyChess. Remember, stockfish is the best chess engine in the world, even though it's playing strength is limited, it still playes a very hard level of chess. Chess beginners may choose the PYTHON CHESS ENGINE written by me over stockfish.

Changlog has been moved to CHANGELOG.md

## What's Next

- Athough most of the features I had wanted in My-PyChess have been implemented in v3.0, there is still lot of room for improvement
- Some of those are listed here
1) Online Gamemode: This mode is newly introduced, has a lot of room for upgrades and maybe a few bugfixes.

2) Implement a game timer in chess.

3) Improvise the GUI in many places.

4) Improve the TextBox in the online menu.

5) Save games in PGN format.

- There are many more in this list, but if you have any ideas, bug-reports or suggestions, feel free to use the issues section to communicate with me.
