This folder is used to contain the League of Legends Data Dragon

In Riot's own words: "Data Dragon is our way of centralizing League of Legends game data and assets, including champions, items, runes, summoner spells, and profile icons. All of which can be used by third-party developers." 

For size constraints and reasons of ownership, we do not store Data Dragon in our repository.

To use Data Dragon (and Gibbon Guardian which relies on it) you must follow these instructions every new patch.

1. Read and aknowledge the terms of use which can be found at https://developer.riotgames.com/terms
2. Download dragontail-xx.xx.x.tgz from https://developer.riotgames.com/docs/lol#data-dragon and move it into this folder
3. Extract the contents of dragontail-xx.xx.x.tgz into this folder.  If done correctly dragonhead.js should be at the top level of this folder structure
4. Make sure you are up to date and have the correct Data Dragon for the patch.

An example top level folder structure for patch 10.22.1 is given below:
# 10.22.1
# img
# lolpatch_10.22
# dragonhead.js
# languages.js
# janguages.json