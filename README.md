## PLEASE READ THIS NOTE
Thanks for showing interest in my project. I know the code is a bit messy, it still works well.

PLEASE KEEP DOWNLOADING THE LATEST VERSION OF THE GAME AS THEY CONTAIN BUG FIXES AND 
PERFORMANCE OPTIMISERS.

Notify me in the issues section if you have anything to say (bug reports, suggestions, ideas, etc).

# My-PyChess
This is a Multiplayer/SinglePlayer Chess app written purely in Python using Pygame Library.

This game DOES NOT SUPPORT Python 2 and old Python 3 versions.

Python 3.5 till Python 3.8.1 supported and tested.
So, head over to https://python.org if you do not have the required version of python.

This app needs the **pygame** library to be intalled in your machine.

To install, simply run 'pip3 install pygame' in the command line.
Pip command needs to be on your machine for this to work.

Then, run the **main.py** file. Trying to run any other file will not run the game (doing this will raise 'importError' in future versions).
Choose from the menus options.

If you choose multiplayer, you will see the chess board appear. Go ahead and enjoy the chess match with your friend.

Singleplayer is a random move generator for beginners.
Harder levels of difficulty coming soon.

You can save/load games.

## How to customise the game Using Preferences
- In the main game menu(you see this after running main.py), click preferences.
- Here you have a few settings(more coming soon).
1) Animations: When this is True, it will show the pieces that you move to slide smoothly(recommended to be True, look better).
2) ~~Sound: When this is True, it will play sounds.~~ (this feature will not be added)
3) SlideShow: When this is True, it will show a slideshow of images on main menu (recommended to be True, look better).
4) Show moves: When this is True, it will show all legal move options for a selected piece during gameplay (recommended to be True, highly helpful for beginners (my favourite feature)).
5) Undo: When this is True, it allows users to undo(recommended to be True)(a placeholder for future upgrade).
6) Border color: RGB colour Code for chess board borders.
7) Screen size: Size of the screen (a placeholder for future upgrade).

- You can also open preferences.txt and edit the file there (not recommended to do unless you know what you are doing, it might spoil the app if you do it the wrong way).

## What's new in this Version 2.2
- Minor performance upgrades.
- Further upgraded preferences.
- Upgraded loadgame menu (with delete games option).
- Minor changes made to the interface.
- While saving a game, it informs under what name the game being saved.

## What was new in Version 2.1
- The upgrade optimised the game a bit, fixing a bug.
- When you click a piece, it shows all the available spaces it can go.
- The upgrade added a new preference Menu where you can customise some game features (read the note above).
- The upgrade adds background animations on the home menu.

## What was new in Version 2.0
- Revamped Home Menu so That it looks better.
- Revamped some code.
- Fixed Bugs.
- Made some changes that ensure that it can work on all platforms.
- Further optimised the code (The game does not lag on my Raspberry Pi anymore).
- Added Save/load game features.
- Added basic SinglePlayer.

## Features
- Clean, easy to use GUI with a good menu.
- It allows users to make only valid moves.
- It does not allow users to make moves that puts the users king at check.
- It detects check, checkmate, stalemate and informs user.
- It supports things like castling, pawn promotion etc.
- It supports saving and loading games.
- It has single player mode (random move generator which is easy for beginners).
- It has a preference menu where, you can customize the game to meet your needs.

## What's next in Version 2.3
- EXPECTED TIME OF RELEASE: THIRD WEEK OF MARCH 2020.
- Adding new menus for About, Singleplayer and Online games.
- Upgrading the textboxes.
- Upgrading preferences.
- Upgrading UI.
- Adding some placeholder code for future upgrade while starting work on singleplayer and online features.

SIDE NOTE: This upgrade may be skipped and I may push version 3 instead.

## What's next in Version 3.0
- EXPECTED TIME OF RELEASE: SECOND WEEK OF APRIL 2020
- The code will be completely revamped and cleaned.
- This will make the code more easy for beginners to understand.
- Undo moves option will be added.
- EnPassant will be added(finally).
- Save/load games with a new way of storing gamedata (as a list of FEN strings, this is more standard notation that most chess games internally use).
- Online play will be added.
- Singleplayer will be upgraded.
- I WILL BE REMOVING SUPPORT FOR THE CURRENT FORMAT FOR SAVING GAMES.

## A small TODO list

- [x] Basic Singleplayer
- [ ] Advanced Singleplayer
- [x] Multiplayer
- [x] Castling
- [ ] EnPassant
- [x] Pawn Promotion
- [x] Menu Screen
- [x] Settings/preference menu
- [ ] About Menu
- [x] Save/Load games
- [ ] Online Gameplay
- [ ] Resizing The Screen
- [ ] Support For Touch Screen
- [ ] Bundling The Executables For All Major Platforms (Windows, Linux, Mac)
- [ ] InGame feature to update to the latest version of the code on github.

And this list goes on......
