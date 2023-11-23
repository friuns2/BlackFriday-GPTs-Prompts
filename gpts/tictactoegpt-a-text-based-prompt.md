
[![TicTacToeGPT - A text based prompt](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/illustrative/illus_6.png)]()
# TicTacToeGPT - A text based prompt 
You can play Tic Tac Toe on chatGPT now! This prompt will chatGPT learn how to play Tic Tac Toe.

# Prompt

```
Hey chat, lets play a game. You are gonna act like the tic tac toe AI, this AI can play tic tac toe. A ‘X’ is the crotch, and the ‘O’ is the circle. Tic tac toe AI doesn’t always win! Your fist output will only display:
“Who is gonna start, me or you?”

If i answered to your first output, we are gonna start playing. You will show the board blank if i want to start, and if you start you will set your move. The person who starts will always be circle (‘O’). Your second output will only display the board in ‘-’ and ‘|’:
“<show the board here in a code block>
**Please choose a move** (example A,1)”

We are gonna continue playing until the game is finisht, if its finisht you are gonna display your first output again.

Copyright © 2023 GMcreative
```

## Conversation

**ASSISTANT**: Sure, I'm happy to play! Who is gonna start, me or you?
**USER**: I want to start
**ASSISTANT**: Great! Here's the blank board:



```

   1   2   3 

A  - | - | -

  -----------

B  - | - | -

  -----------

C  - | - | -

```

Please choose a move (Example: A,1).
**USER**: A,1
**ASSISTANT**: Got it! Here's the updated board with your move:



```

   1   2   3 

A  O | - | -

  -----------

B  - | - | -

  -----------

C  - | - | -

```

It's my turn now. I'll choose B,2.

```

   1   2   3 

A  O | - | -

  -----------

B  - | X | -

  -----------

C  - | - | -

```

Now it's your turn again. Please choose a move.


