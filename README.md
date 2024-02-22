# Important Note

    The project still has some unfinished features, which will be added later.

## My-PyChess

This is a **fully featured chess app** written purely in Python using the
`pygame` library.

![main image](screenshots/main.jpg)

Click [here](screenshots/screenshots.md) to see more few screenshots of My-PyChess in action!

Any bug-reports, suggestions or questions, you can leave it in the github issues section.

The My-PyChess project is available under MIT License. The MIT Licence applies to all the resources I have created in this project. This includes all the python files and text files. But some resources(images, sounds and font file) are not created by me, I have downloaded these from the internet. I have given credits to the authors of these resources in [this file](res/CREDITS.txt). All these resources maintain the original licenses that the authors have leased them under (These licenses permit my use of the respective resources in this project).

### Getting started
- `pip3 install -r requirement.txt`
- Make sure you have Python and `pygame` installed and working.
- Clone this repository (or download zip file and extract it).
- Then, run the `pychess.py` file. Trying to run any other file will not run the game.
- Run server if play online: `g++ server.cpp -o server && ./server`

### Features

- Clean GUI with a lot of menus for ease of use.
- Allows users to make only valid move, does not allow users to make moves that puts the users king at check.
- Detects check, checkmate, stalemate and informs user.
- Supports things like castling, pawn promotion, enpassent etc.
- Supports saving and loading games.
- Has single player mode with two different types, levels and ability to play against the stockfish chess engine.
- Has online gamemode, play chess with anyone in the world using login/ logout.
- Has a chess game timer.
- Has a preference menu where you can customize the app to meet your preferences.
- Has a chess howto, about menu and stockfish install/configure menu to make things easy for users.
- Use the Elo scoring mechanism according to world standards.
- There is a feature to find opponents based on elo point difference


### Online Gameplay

You can self-host the My-PyChess online server. Read more about it [here](onlinehowto.txt).
