# dungeon-master-challenge
Dungeon Master Challenge
ClusterFights Challenge: Dungeon Master {#clusterfights_challenge_dungeon_master}
---------------------------------------

### Goal

-   Escape the dungeon, and become the DUNGEON\_MASTER!

### Terms

-   dungeon level \-- an archive, which when unzipped contains another
    set of zip files
-   dungeon entrance \-- the outermost zip file
-   room \-- any zip file (a room might contain an exit)
-   room key \-- the password to any zip file
-   dungeon exit \-- a file in one of the zip files in this dungeon
    level (DUNGEON\_EXIT)
-   dungeon map \-- reference dataset
-   dungeon generator

### Dungeon Generator {#dungeon_generator}

-   The dungeon generator must output two files, one is a dungeon
    entrance, and one contains an md5 hash of the path through the
    dungeon

<!-- -->

-   get the [DungeonMasterGenerator repo
    here](https://bitbucket.org/di0/dungeonmastergenerator)!!

### Prefight

-   a new dungeon is generated and all fighters are provided with the
    dungeon entrance zip file
-   each fighter is provided a \"new dungeon map\" (this is a large text
    dataset)
-   each fighter is provided the list of possible challenges and
    constraints for room keys based on the dungeon map (Ex:
    Md5Challenge)

### How to Win {#how_to_win}

-   the dungeon map must be checked for the key to the room according to
    each challenge stated in PreFight (ex: Md5Challenge)
-   If you find a DUNGEON\_EXIT, it will include the password for the
    zip holding the next dungeon level
-   NOTE: Not every dungeon level leads to the final dungeon exit
    (DUNGEON\_MASTER)
-   Wins are confirmed by the fighter confirming the md5 hash of the
    complete path through the dungeon
