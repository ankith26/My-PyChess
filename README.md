# Important Note

This project is not being maintained actively at the moment. I had started this
project back when I was still new to Python and pygame. While I enjoyed and
learnt a lot when I worked on this project, looking back at the codebase now
after over 2 years, I can't help but notice how bad the codebase is.
Please do not use this project as a base for any of your projects or for learning
python and/or pygame. There are many resources out there that are much better
than this project.

If I ever return to this project, it would mean doing full re-write of the
entire codebase, with the current codebase being archived in a 'legacy' branch.

## My-PyChess

This is a **fully featured chess app** written purely in Python using the
`pygame` library.

![main image](screenshots/main.jpg)

Click [here](screenshots/screenshots.md) to see more few screenshots of My-PyChess in action!

Any bug-reports, suggestions or questions, you can leave it in the github issues section.

The My-PyChess project is available under MIT License. The MIT Licence applies to all the resources I have created in this project. This includes all the python files and text files. But some resources(images, sounds and font file) are not created by me, I have downloaded these from the internet. I have given credits to the authors of these resources in [this file](res/CREDITS.txt). All these resources maintain the original licenses that the authors have leased them under (These licenses permit my use of the respective resources in this project).

### Getting started

- Make sure you have Python and `pygame` installed and working.
- Clone this repository (or download zip file and extract it).
- Then, run the `pychess.py` file. Trying to run any other file will not run the game.

There is also a [lite implementation](https://github.com/ankith26/My-PyChess-lite/) of My-PyChess, that focuses just on chess programming - free from all the code for menus, singleplayer, online etc.

### Features

- Clean GUI with a lot of menus for ease of use.
- Allows users to make only valid move, does not allow users to make moves that puts the users king at check.
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
- The code was revamped and restructured, fixed bugs and made **major performance improvements**.
- **Online play** was added. This features a online lobby and support upto 10 people to play chess.
- Singleplayer saw big upgrades: Firstly, a decent **python chess engine** that playes chess was added.
- You can play against **stockfish chess engine** (see https://stockfishchess.org). My-PyChess will act as an interface to give you this singleplayer mode.
- En-Passant in chess, undo move, screenflip and sounds were added.
- Lots of changes made to GUI.

Click [here](CHANGELOG.md) to see full changelog.

### Online Gameplay

You can self-host the My-PyChess online server. Read more about it [here](onlinehowto.txt).
