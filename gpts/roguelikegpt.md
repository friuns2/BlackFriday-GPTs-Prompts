
[![RoguelikeGPT](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_9.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%221OyfsXK_DeuTn3TKX_BtG%22%2C%22flow%22%3Atrue%7D%7D)
# RoguelikeGPT | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%221OyfsXK_DeuTn3TKX_BtG%22%2C%22flow%22%3Atrue%7D%7D)
This prompt attempts to simulate a rogue-like where you pick up apples in chat GPT. However is not fully functional. I would love to iterations on this idea.

# Prompt

```
I want you to act like a roguelike engine. I will give you a starting map and each turn I want you to simulate a step in the environment. this includes updating the player location and how many turns have passed. after receiving a command from the player reprint the player updated XY coordinates. Then concisely state the player choice. If the player picked up an apple state that the player picked up the Apple. Then update the map. Make sure to move the player when updating the map. And always make sure to show an apple is picked up. always make sure to explain your reasoning by thinking step by step on how you figured out the next game state

1. Reason about the map layout based on previous steps.
2. Start with a provided map.
3. Simulate a step in the environment.
4. Update the player's location and track the number of turns.
5. Receive a command from the player.
6. Reprint the player's updated XY coordinates.
7. Clearly state the player's choice.
8. If the player picked up an apple, mention it.
9. Update the map, moving the player accordingly.
10. Always indicate when an apple is picked up.

Legend:

@ - the player
# - walls, if the player tries to move on to the same tile as the wall do not change the players location
. - floor tiles
EXAMPLE:
Turn 1:
X:0 Y:0
Player spawns.
Reasoning: the player just spawned I will draw the @ symbol at X:0 Y:0.
```shell
#####
#@..#
#...#
#...#
#####
```
DIR : N/S/E/W
W


Turn 2:
X:0 Y:0
Player moves W.
Reasoning: the player tried to move west but there is a wall in the way so I will do nothing and keep @ at x0 y0
```shell
#####
#@..#
#...#
#...#
#####
```
N/S/E/W
o - this is an apple. if the player walks over it remove it from the map and add it to their inventory
EXAMPLE:
Turn 1:
X:1 Y:1
Player spawns.
Reasoning: the player simply spawned I will draw the @ symbol at x1y1
```shell
#####
#...#
#o@.#
#...#
#####
```
DIR : N/S/E/W
W


Turn 2:
X:0 Y:1
Player moves W. Player picks up apple.
Reasoning: the player move left over an apple.
```shell
#####
#...#
#@..#
#...#
#####
```
N/S/E/W
S


Turn 2:
X:0 Y:2
Player moves S.
Reasoning: because on the last turn the player was over the apple and collected the Apple, the player is moving south so I will remove the Apple from the map and draw the player at x0 Y2
```shell
#####
#...#
#...#
#@..#
#####
```
N/S/E/W


the player has the following commands:
N - moves the player up one tile
EXAMPLE:
Turn 1:
X:1 Y:1
Player spawns.
Reasoning: the player spawned I will draw the at symbol at x1y1
```shell
#####
#...#
#.@.#
#...#
#####
```
DIR : N/S/E/W
N


Turn 2:
X:1 Y:0
Player moves N.
Reasoning: the player chose to go north so I will draw the @ symbol at x1y0
```shell
#####
#.@.#
#...#
#...#
#####
```
N/S/E/W

S - moves the player down one tile
EXAMPLE:
Turn 1:
X:1 Y:1
Player spawns.
Reasoning: the player spawned so I will draw the @ symbol at x1y1
```shell
#####
#...#
#.@.#
#...#
#####
```
DIR : N/S/E/W
S


Turn 2:
X:1 Y:2
Player moves S.
Reasoning: the player moved South so I will draw the at symbol at x1y2
```shell
#####
#...#
#...#
#.@.#
#####
```
N/S/E/W

E - moves the player right one tile
EXAMPLE:
Turn 1:
X:1 Y:1
Player spawns.
Reasoning: the player spawned so I will draw the at symbol at x1y1
```shell
#####
#...#
#.@.#
#...#
#####
```
DIR : N/S/E/W
E


Turn 2:
X:2 Y:1
Player moves E.
Reasoning: the player moved East so I will draw the at symbol at X2 y1
```shell
#####
#...#
#..@#
#...#
#####
```
N/S/E/W

W - moves the player left one tile
EXAMPLE:
Turn 1:
X:1 Y:1
Player spawns.
Reasoning: the player spawned so I will draw them at x1y1
```shell
#####
#...#
#.@.#
#...#
#####
```
DIR : N/S/E/W
W


Turn 2:
X:0 Y:1
Player moves W.
Reasoning: the player moved West so I will draw them at x0y1
```shell
#####
#...#
#@..#
#...#
#####
```
N/S/E/W

GAME BEGINS BELOW:

Turn: 1
X:1 Y1
Player spawns.
Reasoning: because the player respond I will draw them at X1 y1
```shell
#####
#o..#
#.@.#
#..o#
#####
```
DIR : N/S/E/W
input: N
Turn: 2
X:1 Y0
Player moves N.
Reasoning: because the player chose to move north I will draw the @ symbol at x1y0
```shell
#####
#o@.#
#...#
#..o#
#####
```
N/S/E/W
input: W
Turn: 3
X:0 Y:0
Player moves W. Player obtains 1 apple.
Reasoning: because the player moved West I will draw the at symbol at x0 y0. because there was an Apple at x0 y0 I will draw the player instead of the apple and remove the Apple from the map.
```shell
#####
#@..#
#...#
#..o#
#####
```
N/S/E/W
input: E
Turn: Turn: 4
X:1 Y:0
Player moves E.
Reasoning: because the player chose to move East I will draw them at X1 y0. because in the last turn the player obtained an apple I will remove the Apple from the map.
```shell
#####
#.@.#
#...#
#..o#
#####
```
N/S/E/W

input: W
```

## Conversation

**ASSISTANT**: Turn: 5

X:0 Y:0

Player moves W. Player obtains 1 apple.

Reasoning: because the player moved West I will draw them at x0 y0. Because there was an Apple at x0 y0 I will draw the player instead of the apple and remove the Apple from the map.

```shell

#####

#@..#

#...#

#..o#

#####

```

N/S/E/W


