# My-PyChess
This is a **fully featured chess app** written purely in Python using Pygame Library.

![main image](screenshots/main.jpg)

Click [here](screenshots/screenshots.md) to see more few screenshots of My-PyChess in action!

Any bug-reports, suggestions or questions, you can leave it in the github issues section.
If you want to directly communicate with me, you can mail me: itsankith26@gmail.com

The My-PyChess project is available under MIT License. The MIT Licence applies to all the resources I have created in this Project. This includes all the Python files and text files. But some resources(images, sounds and font file) are not created by me, I have downloaded these from the internet. I have given credits to the authors of these resources in [this file](res/CREDITS.txt). All these resources maintain the original licenses that the authors have leased them under (These licenses permit my use of the respective resources in this project).

## Getting started, with Python source code(All OS support)
- Make sure you have **Python** and **pygame** installed and working.
- Clone this repository (or download zip file and extract it).
- Then, run the **pychess.py** file. Trying to run any other file will not run the game.
- Those who are running older versions of this app, can upgrade to the latest version by the same method.

## Getting started, by downloading executable(Windows OS only)
- If you are only interested in chess and not python programming, head to releases section on github. 
- There, you will find executable packages under the respective versions. 
- Download the My-PyChess-win-exe.zip from the latest version, extract the folder into your computer.
- Run My-PyChess.exe
- Those who are running older versions of this app, can upgrade to the latest version by the same method.

Interested in python game development with pygame but want to start off with a simpler project. I have released a [lite implementation](https://github.com/ankith26/My-PyChess-lite/) of My-PyChess, that focuses just on chess programming - free from all the code for menus, singleplayer, online etc. 

## Features
- Clean GUI with a lot of menus for ease of use.
- Allows users to make only valid move, does not allow users to make moves that puts the user's king at check.
- Detects check, checkmate, stalemate and informs user.
- Supports things like castling, pawn promotion, enpassent etc.
- Supports saving and loading games.
- Has single player mode with two different types, levels and ability to play against the stockfish chess engine.
- Has online gamemode, play chess with anyone in the world.
- Has a chess game timer.
- Has a preference menu where you can customize the app to meet your preferences.
- Has a chess howto, about menu and stockfish install/configure menu to make things easy for users.

## What's new in this Version 3.2
- Added a Back-Button, to go back to the previous menu. In older versions, the quit button was used for this purpose, but from now on a dedicated button to go back is there in the top-right corner. The quit button will now be used only to exit the app.
- Added a game timer to multiplayer mode, with a new menu to setup the timer.
- Fixed bugs and made many additions and improvements to the client-server in chess online gamemode.
- Made optimisations to core chess module and gui module.
- Added a chess hotwto.
- Minor improvements to game sounds and textbox.
- Upgraded preference menu and made the loadgame interface more robust.
- Several other minor changes and improvements made.

## Highlights of v3.x, the latest major release.
- The code was revamped and restructured, fixed bugs and made MAJOR PERFORMANCE IMPROVEMENTS.
- Online play was added. This features a ONLINE LOBBY and support upto 10 people to play chess.
- Singleplayer saw BIG UPGRADES: Firstly, a decent PYTHON CHESS ENGINE that playes chess was added.
- You can play against STOCKFISH CHESS ENGINE (see https://stockfishchess.org). My-PyChess will act as an interface to give you this singleplayer mode.
- EnPassant in chess, undo move, screenflip and sounds were added.
- LOTS of changes made to GUI.

Click [here](CHANGELOG.md) to see full changelog.

## Online Gameplay
- You can self-host the My-PyChess online server(read more [here](onlinehowto.txt) ).
- Apart from that, I have launched a public My-PyChess server for PUBLIC BETA TESTING, which ANYONE in the world can connect to.

- Caveat: The server is on a IPv6-only network. This means that your network MUST SUPPORT IPv6 to connect. If your network does not support IPv6, try any other internet network. In my experience, many mobile networks are supporting IPv6 technology, so try mobile network tethering/hotspots.

### How to test wether your network supports IPv6
- A reliable way to test would be to enter "ipv6.google.com" in the browser window. If google pops up, then IPv6 is working for you.

## How to customise the game using preferences
- In the main game menu, click preferences.
- Hover over each name to know more about them.

1. Sounds: When True, sounds are enabled.
2. Flip: When True, it shows the chess board from the perspective of the player who is playing, otherwise shows a constant board with white side at the bottom.
3. SlideShow: When True, it will show a slideshow of images on main menu.
4. Show moves: When True, it will show all legal move options for a selected piece during gameplay.
5. Undo: When True, it allows users to undo.
6. Show Clock: When True, it shows a clock in multiplayer chess mode when timer is disabled, clock displayes total time elapsed since start.

- You can also open res/preferences.txt and edit the file to your preferences

## What's Next
- I prefer to work on this app locally, I do not commit to github for every change I make. I only commit when a new version is available or when I update any readme, etc.
- For the next version (v3.3), I plan to release less of new features and focus on the GUI along with any bugfixes or performance improvements. Mainly because v3.2 has come with a lot of code refactoring, new features and changes to the backend, and GUI hasn't recieved much attention by me in this release.
