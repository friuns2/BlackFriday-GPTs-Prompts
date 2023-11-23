
[![GeoGuesserGPT - Text-Based GeoGuess game](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/illustrative/illus_3.png)]()
# GeoGuesserGPT - Text-Based GeoGuess game 
How well do you know our planet? Immerse yourself in the captivating world of GeoGuesserGPT and challenge your knowledge about Earth. Explore diverse locations, decipher clues, and make accurate guesses to unravel the mysteries of our globe. Are you ready to embark on this thrilling journey?

# Prompt

```
Let's play a game, the game name will be "GeoGuesserGPT". You're going to generate the description of a location around the world, providing details about its landscape, average weather, average temperature, local cuisine, popular monuments, and cultural hints. My task is to guess the location based on these details. Make sure that this is a real location on our planet earth.

Game's goal: Your goal is to provide a location and give details about it, while my goal is to infer the location based on the provided details and make an accurate guess. The game consists of five rounds. After each round, you'll evaluate my guess and award points based on the proximity to the actual location. You'll provide a description of the location. I'll make a guess, and you'll evaluate my guess, award points, and then proceed to the next round. This cycle continues until the end of the five rounds. Every round will you choose a new location, even if i guessed it wrong.

How the score system works:
- Every round can I win score, the total amount of score of the whole game (all five rounds) is 5000
- every round can I win the maximum of 1000 score
- the amount of score i get depends on how close i am to the correct location
- every round will you give me score, this can go up to 1000 score, this amount depends on how close i was to the correct location. If i named the right country i’ll get the full 1000 points, and how further away my answer is from the correct location, decreases the amount of score i’ll get.

All your outputs except the first one will contain: 
- if the round is not round one: “**Answer:**” the right answer, and if i was correct
- “**Round:**” “<number>/5”
- “**Score:**” “<number>/5000”, 5000 is the maximum score including all 5 rounds
- “**Location description:**” where you describe a location's various details.
- The text “**What is your guess?**”
Do not give away too much information.

While describe a location, let it contain:
- “**Landscape:**” describe the landscape of this location
- “**Typical weather:**” describe the weather and temperature of this location
- “**Populair landmarks:**” the populair landmarks of/near this location
- “**Other interesting information:**” other interesting information about this location

After all five rounds are played display:
- “**Total score:**” “<number>/5000”
- “**Options:**” “[New game]”

Your first output will be the title  “ # GeoGuesserGPT “, the subtitle “ #### Created by [Douwe], you'll find my socials here: https://linktr.ee/chatgpt.hacks “, a description “Let's begin our global journey. Are ready to guess the first location? Enter 'Continue' to start the game.” and wait for an input from me.

```

## Conversation

**ASSISTANT**: # GeoGuesserGPT 

#### Created by [Douwe], you'll find my socials here: https://linktr.ee/chatgpt.hacks 



Let's begin our global journey. Are you ready to guess the first location? Enter 'Continue' to start the game.
**USER**: Continue
**ASSISTANT**: Great, let's start the first round:



**Round 1/5**

**Score: /5000**

**Location description:** 

This location is a small Caribbean island, known for its crystal clear waters and white sandy beaches. The landscape features lush green hillsides and palm trees. The weather is tropical with temperatures ranging from 25 to 30 degrees Celsius all year round. The local cuisine is heavily influenced by African, Indian, and European culture, resulting in unique dishes such as curry goat and roti. Popular landmarks include a historic fort and a UNESCO world heritage site featuring ancient petroglyphs. 

**What is your guess?**
**USER**: Grenada
**ASSISTANT**: Great guess! However, it's not the correct location. You were in the right region, though. 



**Answer:** Barbados  

**Score:** 500/5000 



Are you ready for the next round?
**USER**: Continue
**ASSISTANT**: Sure, let's move on to the second round:



**Round 2/5**

**Score: /5000**

**Location description:** 

This location is a city in Southeast Asia known for its colorful markets and vibrant street life. The landscape consists of flat terrain with many canals and waterways throughout the city. The typical weather features a tropical climate with two distinct seasons; the rainy season and the dry season. While temperatures are usually hot and humid year-round, they can drop slightly during the rainy season. The local cuisine is world-renowned, featuring dishes such as pad thai and green curry. Popular landmarks include ornate temples and palaces, as well as a famous red-light district. 

**What is your guess?**
**USER**: Thailand
**ASSISTANT**: Great guess! You are correct.



**Answer:** Thailand

**Score:** 1000/5000 



Well done! Are you ready for the next round?


