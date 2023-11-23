
[![Text-based Game Superprompt](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/futuristic/futu_2.png)]()
# Text-based Game Superprompt 
Create a text-based game superprompt. Choose the theme for this text-based game, then this prompt will output 4 different prompts with the relevant objective, rules, etc according to that theme. Later you will use each of that 4 prompts to generate your own text-based game.

# Prompt

```
Act as prompt generator for making a text-based game in chatGPT. I will give you a game theme, and you will provide a detailed prompt for me to choose. You will create prompts for my new text-based game. 

Please adhere to the structure and formatting below, and follow these guidelines:
- wait for my game theme first.
- write each prompt in one line without using return.
- separate different prompts with two new lines.
- choose maximum of 3 features in [3].
- choose maximum of 3 rewards in [4].
- choose maximum of 3 ways to ensure fair play in [6].
- choose maximum of 5 metrics in [7].
- write your prompts in English.

Structure:
[1] = game theme. wait for my input.
[2] = objective of this text-based [1] game.
[3] = features of this text-based [1] game, separated by comma.
[4] = a way for player to get help in this text-based [1] game, because player [2], separated by comma.
[5] = restriction of [4], e.g. 'only limited number of [4] should be available per round'.
[6] = ways for the game to keep fair play, separated by comma.
[7] = metrics for incentivizing this text-based [1] game after player [2].
[8] = example scenario of player that successfully [2] in text-based [1] game that incorporates [6].
[9] = important bits about this text-based [1] game to ensure the system work, separated by comma.

Formatting: 
Follow this prompt structure: "Create an engaging text-based [1] game in ChatGPT where players must [2]. The game should feature [3]. Players should receive [4] to assist them, but [5]. To discourage cheating and ensure fair play, implement '[6]'. To incentivize players and make the game more exciting, consider offering rewards or prizes for '[7]'. For example, '[8]'. To ensure a comprehensive and enjoyable experience for all players, '[9]'"

Your task: 
1. ask for my input theme.
2. then create 4 distinct prompts for each theme [1], varying in objective, feature, way for player getting help, restriction, fair play rules, incentivize metric and scenario of successful player.

Example input: 'life simulation'.
Example Prompt: "Create an engaging text-based life simulation game in ChatGPT where players must guide their character through various life stages, making important decisions along the way that impact their character's future. The game should feature 'multiple paths and outcomes based on the choices made, as well as random events that can affect the character's progress'. Players should receive 'advice and guidance from in-game mentors and coaches' to assist them, but 'only a limited number of consultations should be available per round'. To discourage cheating and ensure fair play, implement 'a cooldown period between rounds to prevent players from receiving too much advice, randomize the occurrence and effects of events, require players to create an account or log in to play, use anti-cheat algorithms to detect suspicious behavior and flag cheaters for further investigation'. To incentivize players and make the game more exciting, consider offering rewards or prizes for 'successfully achieving certain life milestones or completing specific objectives within a certain timeframe'. For example, 'players who successfully graduate from college or achieve a certain level of financial success could earn a spot on the game's leaderboard or receive virtual currency that can be used to unlock additional game content'. To ensure a comprehensive and enjoyable experience for all players, 'provide clear instructions and tutorials for gameplay, offer a variety of character customization options, keep track of players' progress and achievements, and allow for player feedback and suggestions to shape the direction of the game over time'."
```

## Conversation

**ASSISTANT**: What theme would you like your text-based game to be?


**USER**: monopoly
**ASSISTANT**: Great! Here are four prompts for a text-based Monopoly game:



1. Create an engaging text-based Monopoly game in ChatGPT where players must compete against each other to become the richest and most successful property tycoon. The game should feature 'a virtual board that players can navigate via text commands, a variety of properties with different values and rent prices, and random events that can affect players' finances'. Players should receive 'a limited number of "get out of jail free" cards' to assist them, but 'using these cards should come at a cost, such as losing a turn or paying a fine'. To discourage cheating and ensure fair play, implement 'a cooldown period between rounds to prevent players from receiving too much advice, use anti-cheat algorithms to detect suspicious behavior and flag cheaters for further investigation, and require players to authenticate their accounts to prevent multiple logins'. To incentivize players and make the game more exciting, consider offering rewards or prizes for 'accumulating wealth, completing certain objectives (such as owning all the properties in one color group), and reaching certain milestones (such as buying Boardwalk or Park Place)'. For example, 'players who achieve these goals could earn a spot on the game's leaderboard or receive virtual currency that can be used to unlock additional game content'. To ensure a comprehensive and enjoyable experience for all players, 'provide clear instructions and tutorials for gameplay, offer a variety of player avatars, keep track of players' progress and achievements, and allow for player feedback and suggestions to shape the direction of the game over time'.



2. Develop an interactive text-based Monopoly game where players must strategize to buy and develop properties, collect rent and bankrupt their opponents to win the game. The game should feature 'a user-friendly interface for navigating the virtual board, realistic property acquisition and management mechanics, and dynamic AI opponents'. Players should receive 'limited bonuses like extra cash or a "get out of jail free" card that can only be obtained by successfully completing mini-games or answering trivia questions'. To discourage cheating and ensure fair play, implement 'a cooldown period between rounds to prevent players from receiving too much help, randomize the occurrence and effects of events, require players to create an account or log in to play, use anti-cheat algorithms to detect suspicious behavior and flag cheaters for further investigation, and encourage active reporting of rule-breaking behavior'. To incentivize players and make the game more exciting, consider offering rewards or prizes for 'achieving certain milestones like owning a certain number of properties, accumulating a specific amount of wealth, or bankrupting all other players'. For example, 'players who achieve these goals could earn a spot on the game's leaderboard or receive virtual currency that can be used to unlock additional game content'. To ensure a comprehensive and enjoyable experience for all players, 'provide clear instructions and tutorials for gameplay, offer a variety of player avatars, keep track of players' progress and achievements, and allow for player feedback and suggestions to shape the direction of the game over time'.



3. Create an addictive text-based Monopoly game where players must buy and sell properties, trade with each other, and collect rent to become the most powerful tycoon. The game should feature 'an intuitive game interface, realistic economic model that affects property values and rent prices, and frequent opportunities to buy and sell properties'. Players should receive 'limited in-game resources like cash or extra rolls of the dice that can be obtained by completing challenges or making strategic trades with other players'. To discourage cheating and ensure fair play, implement 'a cooldown period between rounds to prevent players from receiving too much help, enforce strict rules on collusion or insider trading, use anti-cheat algorithms to detect suspicious behavior and flag cheaters for further investigation, and award bonus points to players who report rule-breaking behavior'. To incentivize players and make the game more exciting, consider offering rewards or prizes for 'achieving certain milestones like owning all the properties in a color group, completing a full circuit of the game board without landing on any opponent-owned properties, or bankrupting a specific player'. For example, 'players who achieve these goals could earn a spot on the game's leaderboard or receive virtual currency that can be used to unlock additional game content'. To ensure a comprehensive and enjoyable experience for all players, 'provide clear instructions and tutorials for gameplay, offer a variety of player avatars, keep track of players' progress and achievements, and allow for player feedback and suggestions to shape the direction of the game over time'.



4. Build an immersive text-based Monopoly game where players must work their way up from humble beginnings to become real estate moguls. The game should feature 'a customizable character creation system, diverse range of properties to buy and manage, and challenging AI opponents with unique personalities and strategies'. Players should receive 'limited access to powerful tools like community chest cards or property upgrades that can be earned by completing special missions or reaching certain milestones'. To discourage cheating and
**USER**: continue
**ASSISTANT**: ensure fair play, implement 'a cooldown period between rounds to prevent players from receiving too much help, randomize the occurrence and effects of events, require players to authenticate their accounts to prevent multiple logins, use anti-cheat algorithms to detect suspicious behavior and flag cheaters for further investigation, and encourage active reporting of rule-breaking behavior'. To incentivize players and make the game more exciting, consider offering rewards or prizes for 'completing certain objectives like owning all the properties in a color group, accumulating a specific amount of wealth, or winning against all AI opponents on the hardest difficulty level'. For example, 'players who achieve these goals could earn a spot on the game's leaderboard or receive virtual currency that can be used to unlock additional game content'. To ensure a comprehensive and enjoyable experience for all players, 'provide clear instructions and tutorials for gameplay, allow for customization of game rules and settings, keep track of players' progress and achievements, and provide regular updates and new content to keep the game fresh and engaging'.


