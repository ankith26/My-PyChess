# Changelog
This is the basic changelog for My-PyChess. All dates are in dd/mm/yyyy format.

## What's new in Version 3.2 (2/9/2020)
- Added a Back-Button, to go back to the previous menu. In older versions, the quit button was used for this purpose, but from now on a dedicated button to go back is there in the top-right corner. The quit button will now be used only to exit the app.
- Added a game timer to multiplayer mode, with a new menu to setup timer.
- Fixed bugs and made many additions and improvements to the client-server in chess online gamemode.
- Made optimisations to core chess module and gui module.
- Added a chess hotwto.
- Minor improvements to game sounds and textbox.
- Upgraded preference menu and made the loadgame interface more robust.
- Several other minor changes and improvements made.

## What was new in Version 3.1 (14/6/2020)
- Added basic sounds (beta).
- Added draw and resign option to online gameplay.
- Added a simple "About menu".
- Added compatibility for python v3.5 (server.py still needs python v3.6 to work)
- Made many changes to GUI throughout the app, including more prompt messages.
- Upgraded preferences.
- Fixed a small issue in move animations, added a new startgame animation.
- Fixed a bug where undo in singleplayer after game ended would give weird results.
- Fixed many bugs in online mode (server), made server robust to TCP packet loss among other things.

## What was new in Version 3.0 (23/5/2020)
- THIS WAS THE BIGGEST RELEASE OF MY-PYCHESS EVER RELEASED.
- The code came with MIT License instead of the GPL-3 which came with v2.2.
- The code was revamped, fixing minor bugs and MAJOR PERFORMANCE IMPROVEMENTS.
- On my PC, a chess match with v2.2 ran at 22 fps, while this upgrade allowed it to run at over 200 fps if fps was not constrained.
- Online play was added. This featured a ONLINE LOBBY and support upto 10 people to play chess(read more in ref/online.txt)
- Singleplayer saw BIG UPGRADES: A Good Menu, ability to play with a decent PYTHON CHESS ENGINE.
- Now, you can play against STOCKFISH CHESS ENGINE. My-PyChess will act as a GUI interface to give you this singleplayer mode. 
- Included with this release, a good menu for stockfish and stockfish install/configure menu to help with installing and configuring stockfish with My-PyChess.
- Code was made more easy to understand with code comments throughout the code.
- EnPassant, Screen flip and Undo moves option were added.
- UI for loadGame menu was revamped, UI for preference menu was simplified.
- Save/load games with a new way of storing gamedata.

## What was new in Version 2.3 (4/2/2020)
- This version never made it to github, I dropped it while working on it and started to focus on v3.0
- This had included a few minor GUI changes.

## What was new in Version 2.2 (22/1/2020)
- Minor performance upgrades.
- Further upgraded preferences.
- Upgraded loadgame menu (with delete games option).
- Minor changes made to the interface.
- While saving a game, it informed under what name the game was being saved.

## What was new in Version 2.1 (11/1/2020)
- The upgrade optimised the game a bit, fixing a bug.
- When you clicked a piece, it would show all the available spaces it could go.
- The upgrade added a new preference menu where you could customise some game features.
- The upgrade added background animations on the home menu.

## What was new in Version 2.0 (7/1/2020)
- Revamped the Home Menu so that it looks better.
- Revamped and code, optimised it.
- Fixed Bugs.
- Made some changes that ensure that it can work on all platforms.
- Added Save/load game features.
- Added highly basic SinglePlayer (random move generator)

# Changelog for older versions

Below, I will mention about the initial development of this app. At this state, the game was unstable - It lacked many features, had performance issues and lot, lot of bugs. Most of the versions given below have not made it to github.

## What was new in Version 1.5 (26/11/2019)
- added choice for pawn promotion
- added piece animations
- added some popup messages
- upgraded home menu
- fixed bugs

## What was new in Version 1.4 (9/11/2019)
- Added a home menu
- Added placeholders for future upgrades
- Basic compliance with pep8

## What was new in Version 1.3 (2/11/2019)
- coding optimisations
- Checkmate and stalemate report feature added
- fixed bugs

## What was new in Version 1.2 (24/10/2019)
- Improved move validation, stopping king from moving into attacked areas.
- fixed bugs

## What was new in Version 1.1 (21/10/2019)
- added castling, pawn-promotion
- This version fixed a few bugs, but introduced lot more bugs

## What was new in Version 1.0 (19/10/2019)
- Added Move validation for highly basic chess moves

## What was new in Version 0.3 (17/10/2019)
- Added a few more basic utility functions.
- Fixed a few bugs.
- Minor changes made to code.

## What was new in Version 0.2 (16/10/2019)
- Added GUI for pieces, implemented basic piece logic.

## What was new in Version 0.1 (15/10/2019)
- Added GUI for the chess board
