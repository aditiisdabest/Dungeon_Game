# Project Overview
This project is a text-based dungeon escape game. The player takes on the role of a 
Dungeon Escaped Prisoner who must navigate a 3-floor dungeon, avoid enemies, and reach 
the exit to achieve freedom. The game tracks player lives, room locations, and enemy encounters.
**Goal:** Escape the dungeon while surviving encounters with the Shadow Beast.

# Structure
The dungeon consists of **3 floors**, each with **3 unique rooms**:

| MAP    |  Room1   | Room3    | Room3    |
|-----|-----|-----|-----|
| **Floor3**    |  entrance   | Cellblock   |  Armory   |
|-----|-----|-----|-----|
| **Floor2**    |  crypt   | altar   |  library   |
|-----|-----|-----|-----|
| **Floor1**    |  treasure   | collapsed_room   |  exit room   |

**Room Objects:**  
- `Room` class stores name and description.  
- `Player` class tracks position, lives, and movement logic.  
- `Enemy` (and child `Shadow_Beast`) classes handle encounters and damage.
  
# Design

- **Movement:** Player moves up/down/left/right; each move costs 1 life. Walls, pits, and locked paths block movement.  
- **Enemy Encounters:** The Shadow Beast is randomly positioned in the dungeon (excluding start and exit). Encounter reduces lives by 1.  
- **Game Loop:** Continues until player reaches exit or loses all lives. Player can quit at any time.  
- **Map Representation:** A 2D list stores room objects, allowing row/column access for movement and interactions.

# Key Logic
1. **Player Movement**
   - The player can move `up`, `down`, `left`, or `right`.
   - Each move reduces the player's lives by 1.
   - Movement is blocked by walls, pits, or locked paths.
   - Player position is tracked with row and column indices in the dungeon map grid.

2. **Room Interactions**
   - Each room has a unique description and possible events.
   - Some rooms may contain treasures or hazards.
   - Rooms are represented by `Room` objects with `name` and `description`.

3. **Enemy Encounters**
   - The Shadow Beast is randomly positioned in the dungeon (excluding start and exit).
   - Encountering the Shadow Beast reduces player lives.
   - The `Shadow_Beast` class inherits from `Enemy` and adds a fright effect.
     
4. **Game Loop**
   - At each turn:
     1. Player chooses a direction.
     2. Player moves if possible.
     3. Check for enemy encounter.
     4. Check if player reached the exit.
     5. Check if lives are exhausted.
   - Game ends when the player either escapes or runs out of lives.

5. **Randomization**
   - Shadow Beast location is randomized at the start of each game.
   - Ensures different experiences each playthrough.

# Future Improvements and Considerations

1. **Additional Enemies**
   - Introduce multiple enemy types with different behaviors and damage levels.
     
2. **Enhanced Room Interactions**
   - Add puzzles, traps, or hidden passages in rooms.
   - Some rooms could have multiple outcomes depending on player actions.

3. **Difficulty Levels**
   - Easy, medium, and hard modes affecting lives, enemy behavior, or map.










