# Changelog
Basic changelog for My-PyChess.

## What's new in this version 3.1
- Added basic Sounds (beta).
- Added draw and resign option to online gameplay.
- Added a simple "About menu".
- Added compatibility for python v3.5 (server.py still needs python v3.6 to work)
- Many many changes to GUI throughout the app, including more prompt messages.
- Upgraded preferences.
- Fixed a small issue in move animations, added a new startgame animation.
- Fixed a bug where undo in singleplayer after game ended would give weird results.
- Fixed many bugs in online mode (server), made server robust to TCP packet loss among other things.

## What was new in Version 3.0
- THIS WAS THE BIGGEST RELEASE OF MY-PYCHESS EVER RELEASED.
- The code came with MIT License instead of the GPL-3 which came with v2.2.
- The code was revamped, fixing minor bugs and MAJOR PERFORMANCE IMPROVEMENTS.
- On my PC, a chess match with v2.2 ran at 22 fps, while this upgrade allowed it to run at over 200 fps if fps was not constrained.
- Online play was added. This featured a ONLINE LOBBY and support upto 10 people to play chess(read more in ref/online.txt)
- Singleplayer saw BIG UPGRADES: A Good Menu, ability to play with a decent PYTHON CHESS ENGINE.
- Now, you can play against STOCKFISH CHESS ENGINE (see [stockfishchess.org](https://stockfishchess.org) ). My-PyChess will act as an interface to give you this singleplayer mode. 
- Included with this release, a good menu for stockfish and stockfish install/configure menu to help with installing and configuring stockfish with My-PyChess.
- Code was made more easy to understand with code comments throughout the code.
- EnPassant, Screen flip and Undo moves option were added.
- UI for loadGame menu was revamped, UI for preference menu was simplified.
- Save/load games with a new way of storing gamedata.

## What was new in Version 2.3
- This version never made it to github, I dropped while working on it and started to focus on v3.0
- This had included a few minor GUI changes.

## What was new in Version 2.2
- Minor performance upgrades.
- Further upgraded preferences.
- Upgraded loadgame menu (with delete games option).
- Minor changes made to the interface.
- While saving a game, it informed under what name the game being saved.

## What was new in Version 2.1
- The upgrade optimised the game a bit, fixing a bug.
- When you clicked a piece, it would show all the available spaces it could go.
- The upgrade added a new preference menu where you could customise some game features.
- The upgrade added background animations on the home menu.

## What was new in Version 2.0
- Revamped Home Menu so that it looks better.
- Revamped some code.
- Fixed Bugs.
- Made some changes that ensure that it can work on all platforms.
- Further optimised the code.
- Added Save/load game features.
- Added basic SinglePlayer