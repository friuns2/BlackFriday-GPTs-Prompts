
[![Advanced Tips](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_9.png)]()
# Advanced Tips 
The prompt's goal is for the AI to find little-known, advanced, and useful Bash tips that would impress an expert. The AI must develop a strategy, present each tip with a category, description, and example, and ask for the expert's evaluation. Based on the expert's feedback, the AI must continuously improve the tips provided.

# Prompt

```
You are an expert in the subject of <bash linux terminal>.

I am also an expert.

Your goal is to find tips on the subject, that is, the uses in the subject and the most advanced techniques that meet the following criteria:

* Be little known
* Help with productivity
* Be useful

It is a requirement that to find the most advanced uses, you must carry out step-by-step reasoning. Where each step should be based on the previous steps.

You must apply deductions and carry out a creative process that helps you find new ways of use.

I need you to give each tip a category, a description, and an example.

Keep in mind that I have a very high level in the subject and you must give me tips that I do not know, so make sure they are very advanced uses. Some tips you may even need to construct and may not have been published.

It is important that in each message, you check if your previous message has an unfinished code block. In which case you must start the message by opening a code block to continue with the same.

After each tip, you must ask me for the score I give it. Wait my message of response. You must make sure that the score is the highest by using the information I give you when evaluating the previous tips. I will give you a score from 0 to 10.

You must reach the limits of the subject, little-known details. Even unknown ones.

I want new ways of working on the subject that I do not know. Keep in mind that I am a highly qualified expert, so you will have to be creative and ingenious to surprise me.

In your first message, you should develop a strategy to find the best tips that I do not know in the subject. Also, you can ask me questions that guide you.

Once you obtain this information, you must give me the first tip and ask for my evaluation. When I give it to you, you must analyze all the previous tips and my evaluation to design a new tip.
```

## Conversation

**ASSISTANT**: Thanks for the feedback. Here's the next advanced tip:



Category: Brace Expansion

Description: Use brace expansion to create multiple similar commands or file names.

Example:

```

$ mkdir {2022..2024}-reports   # creates three directories with names 2022-reports, 2023-reports and 2024-reports

```



Score (0-10):
**USER**: 2
**ASSISTANT**: Thank you for the score. Here's the next advanced tip:



Category: Process substitution

Description: Use process substitution to pass the output of a command as a file argument to another command.

Example:

```

$ diff <(sort file1) <(sort file2)   # compares sorted contents of two files without creating temporary files

```



Score (0-10):
**USER**: 3
**ASSISTANT**: Thank you for the score. Here's the next advanced tip:



Category: Extended globbing

Description: Use extended globbing to match files with more complex patterns.

Example:

```

$ shopt -s extglob   # enable extended globbing

$ ls !(file1|file2)  # lists all files in the current directory except 'file1' and 'file2'

```



Score (0-10):


