# Version 3 of Dungeon_Game


# Import and Global Variables
import random
user_name = input("What is your name, traveler? ")
game_enemy = "The Shadow Beast"
game_role = "Dungeon Escaped Prisoner"
game_goal = "freedom"


class Room:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name.title()


class Player:
    
    def __init__(self, player_name, lives, map_dungeon):
        self.player_name = player_name
        self.lives = lives
        self.map = map_dungeon
        # starting position (top-left)
        self.row = 0
        self.col = 0

    def move(self, direction):

        if self.lives <= 0:
            print("You have no lives left! GAME OVER!")
            return False

        if direction == "up":
            if self.row > 0:
                self.row -= 1
            else:
                print("\nYou bump into a cold stone wall.")
        #down
        elif direction == "down":
            if self.row < len(self.map) - 1:
                self.row += 1
            else:
                print("\nA deep pit blocks your path.")
        #right
        elif direction == "right":
            if self.col < len(self.map[0]) - 1:
                self.col += 1
            else:
                print("\nRusty iron bars prevent you from going that way.")
        #left
        elif direction == "left":
            if self.col > 0:
                self.col -= 1
            else:
                print("\nYou can't squeeze through the cracks in the wall.")
        else:
            print("\nThat direction doesn't exist in this dungeon...")
            return False

        self.lives -= 1 
        print(f"{self.player_name} moves to {self.current_room().name}. Lives left: {self.lives}")
        return True


    def current_room(self):
        return self.map[self.row][self.col]


#Room descriptions
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


# Create the player
player = Player(user_name, lives = 10, map_dungeon = map_dungeon)


# Introduction message
print(f"\nWelcome, {game_role} {user_name}.")
print(f"\nYou are stuck in a dungeon with 3 floors each containing 3 unique rooms.")
print(f"You must escape the dungeon by making your way down to the first floor.")
print("You have 10 lives. Each move costs you 1 life so choose wisely")
print(f"HURRY! before {game_enemy} finds you...\n")


# Show entrance room
current = player.current_room()
print(f"You wake up in in the first room of the 3rd floor: {current.name}")
print(current.description)



while True:

    # Update current room inside of the loop at the start
    current = player.current_room()

    # Check if player ran out of lives
    if player.lives <= 0:
        print("\nYou have run out of lives! The dungeon claims you...")
        break

    # Check if player reached the exit
    if current == exit_room:
        if player.lives >= 1:
            player.lives -=1
            print(f"\nYou spend one life to open the exit door...and escape!")
            print(f"Lives remaining:{player.lives}")
            print(f"Congratulations! You survived the dungeon and attained {game_goal}!")
            break
        else:
            print("\nYou don't have enough lives to escape! You await your fate as the Shadow Beast approaches.")
            break

    # main movement code
    print("\n Dungeon Movement")
    print("Move: up, down, left, right")
    print("Type 'quit' to stop your escape")
    move = input("What would you like to do? ").lower()
    if move == "quit":
        print("You sit down and await your fate... the Beast approaches...")
        break
    elif move in ["up", "down", "left", "right"]:
        moved = player.move(move) 
        if moved:
            # Show current room
            current = player.current_room()
            print(f"\nYou are now in: {current.name}")
            print(current.description)
    else:
        print("\nThat direction doesn't exist in this dungeon...")
        
        
        
        
