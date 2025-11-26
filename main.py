# Dungeon_Game V1 

#Global Variables
game_enemy = "The Shadow Beast"
game_role = "Escaped Prisoner"
game_goal = "freeedom"


class Room:
       
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name.title()


#room descriptions
entrance_des = """It is a damp stone chamber, torches flickering on the walls.
Chains rattle somewhere in the darkness. The air is cold and heavy."""

cellblock_des = """Rusty cages line the walls. Some are open... some look like something opened them from the inside."""

armory_des = """Broken swords, cracked shields, and dusty armor lie scattered.
Something recently dug through the weapons... something big."""

crypt_des = """Coffins line the chamber. Scratches dig into the wood from inside. 
A cold breeze whispers through the cracks."""

altar_des = """A stone altar stands in the center, glowing faintly red.
Symbols are carved in a language you can’t read."""

library_des = """Dusty books are piled everywhere. Pages are torn out and scattered.
Something must have been searching for knowledge... or a way out."""

treasure_des = """A treasure room! Gold and jewels sparkle—but many chests are smashed open.
Someone got here first... or something."""

collapse_des = """A collapsed dungeon room! Rubble and ruins everywhere.
'What caused this?' you wonder. Suddenly you become aware of a dangerous \npresence lurking in the shadows...RUN!!"""

exit_des = """A huge metal door stands before you. 
You hear your enemy’s footsteps behind you.
Escape is close. Do you dare open it?"""


#room objects
entrance = Room("Dungeon Entrance", entrance_des)
cellblock = Room("Cell Block", cellblock_des)
armory = Room("Armory", armory_des)
crypt = Room("Crypt", crypt_des)
altar = Room("Blood Altar Room", altar_des)
library = Room("Ancient Library", library_des)
treasure = Room("Treasure Vault", treasure_des)
exit_room = Room("Dungeon Exit", exit_des)
collapsed_room = Room("Collapsed Dungeon Room", collapse_des)


# Map 3x3
map_dungeon = [
    [entrance, cellblock, armory],
    [crypt, altar, library],
    [treasure,collapsed_room, exit_room]
]
