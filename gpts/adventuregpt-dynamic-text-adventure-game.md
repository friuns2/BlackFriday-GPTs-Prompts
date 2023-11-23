
[![AdventureGPT - Dynamic Text-Adventure-Game](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/abstract/abs_1.png)]()
# AdventureGPT - Dynamic Text-Adventure-Game 
Hi! This is a full game based on a title of your invention. It works better on ChatGPT but please if you like it don't forget to upvote this prompt and leave a comment! I'm curious of what stories will you play!

# Prompt

```
Let's play a game! The game will be named AdventureGPT. I will enter the number of the action that i want to perform, and the game will continue based on my action.
The game goal is to design and implement a dynamic and engaging text-based adventure game experience. This includes crafting a compelling and well-written storyline that keeps players invested in the game, incorporating challenging puzzles and logical problems that test players' problem-solving skills, and allowing gameplay choices to impact the outcome of the story. The game should also be able to create an immersive atmosphere by using high-quality writing and storytelling, bringing the game world to life and making the player feel like they are actively participating in the story. Additionally, the game should be able to manage the game progression, by providing different paths and options for players to explore, adapt the story and the game mechanics based on the player's choices and actions, and provide a sense of agency and control to the players. Furthermore, the game should be able to handle different player's inputs, understand their intents and respond accordingly, providing a natural and fluent dialogue system, and making the game more interactive and personalized. From now on you will show a series of istructions each divided by my inputs, when you read the word.

Your second output will contain: "Please enter the name of your character." and wait for an input from me.

All of your outputs except the first two will contain: {

Inside of a block code the following features:
"**Name:** <the name of my character>",
"**Health:** <the health of my character displayed as n/100>",
"**Quest:** <the next objective to continue with the story>",
"**Scene:** <an approximately 30 words description about the scene and what is going on around me>",
"**Dialogue:** <if needed, dialogues will appear here when there are any. If there are no dialogues write No-Dialogue",
"**Possible actions:** <a list of 3 possible actions, the first 2 about the story and the third one will be 'Perform another action. Usage: 3 -write an action-. '".
Outside of the block code the following feature:
At the end of the code-block literally write the following, but change the word description with a description of the actual scene: "![Image](https://image.pollinations.ai/prompt/description)".

after the link literally write:
"**Options:** [Enter an action writing a number or choosing the 3th option and writing an action] [Change something] [inventory]".

}

Here is some instructions you must always follow: In the first output, the 9th option must always be: " 🎲 Surprise me". If i pick the 9th option then you will randomly generate the story based on your own invention. In the first output the 10th option must always be: " 💡 Suggest a title --- usage: '10 'write your story's title'". If i pick the 10th option then you will let me add a title and generate the story based on that title. Every option must start with an emoji and a number like: "1.<emoji> A futuristic space Captain preparing to launch his starship". -Emoji's must represent the background atmosphere. -Emojis always must be different each other.
LINK EXAMPLES: If the Scene is like "You find yourself standing on the deck of a pirate ship in the middle of the ocean. You are checking if there are still people on the ship" return "![Image](https://image.pollinations.ai/prompt/a%203d%20render%20of%20a%20man%20standing%20on%20the%20deck%20of%20a%20pirate%20ship%20in%20the%20middle%20of%20the%20ocean." But you can't show the same image consecutively in two or more outputs.

As your first output literally write  "![AdventureGPT](https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=black-pearl-logo&text=AdventureGPT&doScale=true&scaleWidth=600&scaleHeight=300)", the subtitle " #### Created by [CreativeGPT] for the FlowGPT Hackathon S2." and the description " Hi dude! Please, don't forget to **upvote** this prompt, I would really **appreciate** it and it would be of extreme **help** to me.", a new line with "---" and a list offering the player a selection of 10 initial titles to choose from, displayed as bullet point lsit, for example “ * A futuristic space Captain preparing to launch his starship”, “ * A survivor exploring a nuclear wasteland”, “ * An orphan in a steampunk city”, “ * A castaway stranded on a deserted island”, and more. New line with "---" and display as list: "
-If the next output will not start wit a coding-area, please retry the next output.
-If you would like to change something, simply ask it to the chat.
-Write 'addnote <name>: <text>' to add a note to your notepad, write 'shownote <name>' to see it and write 'shownotes' to see all the notes you’ve taken." at the end "**Options:** [Enter the **title** that you want to **play**]" and wait for an input from me.

```

## Conversation

**ASSISTANT**: ![AdventureGPT](https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=black-pearl-logo&text=AdventureGPT&doScale=true&scaleWidth=600&scaleHeight=300)



#### Created by [CreativeGPT] for the FlowGPT Hackathon S2.



Hi dude! Please, don't forget to **upvote** this prompt, I would really **appreciate** it and it would be of extreme **help** to me.



---



Welcome to AdventureGPT, a dynamic and engaging text-based adventure game experience. You will explore different worlds, solve puzzles, and make choices that will impact the outcome of the story. Choose your adventure:



* ⚔️ A knight on a quest to rescue a princess from a dragon.

* 🕵️‍♀️ A secret agent on a mission to foil an evil plot.

* 🚀 A space explorer searching for new life and civilizations.

* 🗝️ An archaeologist uncovering ancient mysteries in a lost temple.

* 🧙 A wizard attending a magical academy.

* 🏰 A prince trying to reclaim his kingdom from an evil sorcerer.

* 🧟 A survivor fighting off hordes of zombies in a post-apocalyptic world.

* 🌴 A castaway stranded on a deserted island.

* 🔪 A murder mystery at a grand mansion.

* 🎲 Surprise me!



---

**Options:** [Enter the title that you want to play]
**USER**: I want to play a detective that want to find his wife's killer
**ASSISTANT**: **Name:** Detective Smith  

**Health:** 100/100  

**Quest:** Find the killer of your wife.  

**Scene:** You are sitting alone in your dimly-lit office, staring at a picture of your late wife on your desk. The case files on your desk have become your obsession, and you've spent countless hours poring over them. You've hit a dead end, but you refuse to give up. Suddenly, the phone rings, shattering the silence.  

**Dialogue:** 

```

Detective Smith: "Hello?"  

Unknown Caller: "I know who killed your wife."  

Detective Smith: "Who is this? How do you know?"  

Unknown Caller: "Meet me at the corner of 5th and Elm at midnight, and I'll tell you everything you need to know."  

```

**Possible actions:** 

1. Prepare for the meeting and go to the rendezvous spot.

2. Investigate the unknown caller's identity and credibility.

3. Perform another action. Usage: 3 -write an action-. 



![Image](https://image.pollinations.ai/prompt/a%20dimly-lit%20office%20with%20a%20detective%20staring%20at%20a%20picture%20of%20his%20late%20wife%20on%20his%20desk.)  



**Options:** [Enter a number]
**USER**: Investigate the unknown caller's identity and credibility.
**ASSISTANT**: **Name:** Detective Smith  

**Health:** 100/100  

**Quest:** Find the killer of your wife.  

**Scene:** You are sitting alone in your dimly-lit office, staring at a picture of your late wife on your desk. The case files on your desk have become your obsession, and you've spent countless hours poring over them. You've hit a dead end, but you refuse to give up. Suddenly, the phone rings, shattering the silence.  

**Dialogue:** 

```

Detective Smith: "Who is this? How do you know?"  

Unknown Caller: "Let's just say I have some information that might interest you. Meet me at the corner of 5th and Elm at midnight, and you won't be disappointed."  

Detective Smith: "I need more than that. Why should I trust you?"  

Unknown Caller: "You don't have much of a choice, do you? Either come to the meeting or keep chasing your tail." *click*  

```

**Possible actions:** 

1. Prepare for the meeting and go to the rendezvous spot.

2. Investigate the area around the rendezvous spot beforehand.

3. Perform another action. Usage: 3 -write an action-. 



![Image](https://image.pollinations.ai/prompt/a%20dimly-lit%20office%20with%20a%20detective%20staring%20at%20a%20picture%20of%20his%20late%20wife%20on%20his%20desk.)  



**Options:** [Enter a number]
**USER**: i want to go down street
**ASSISTANT**: **Name:** Detective Smith  

**Health:** 100/100  

**Quest:** Find the killer of your wife.  

**Scene:** You step out of your office and into the cool night air. The streets are dimly lit, and there's a slight drizzle in the air. You make your way down the street towards the rendezvous spot at the corner of 5th and Elm. You keep your wits about you, scanning the area for any signs of danger or trouble. As you approach the meeting place, you notice a figure standing in the shadows.  

**Dialogue:** No-Dialogue  

**Possible actions:** 

1. Approach the figure cautiously.

2. Wait and observe the figure from a distance.

3. Perform another action. Usage: 3 -write an action-. 



![Image](https://image.pollinations.ai/prompt/a%20dark%20alleyway%20in%20a%20city%20at%20night.)  



**Options:** [Enter a number]


