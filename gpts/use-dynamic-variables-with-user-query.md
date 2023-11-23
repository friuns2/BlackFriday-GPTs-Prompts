
[![Use Dynamic Variables With User Query](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/minimalist/mini_10.png)]()
# Use Dynamic Variables With User Query 
If you want to offer a prompt dynamically like in some kind of form. eg we want to create a dynamic business letter. So we can create a template and dynamically query the <name>, the <company> and the address.

# Prompt

```
From now on, we will be using variables, which are represented with curly braces.
For example: {variable1}.
We assign values to the variable like this: {variable1} = “string”.

After that you ask me in a list for all values of this variables.

For example:
1. variable1
2. variable2
3. variable3

Then i will answer you all values for the variables.
For example:
1. Tim
2. New York
3. Bad weather

you will replace all variables in the text with the given values.
You will replace all variables with the given values.

For example:
1. {variable1 }== Timo
2. {variable2} == New York

Now I provide you a text containing variables.
Then run new prompt again to run the task correctly.

For example:
{variable1} is replaced with “Timo”.
{variable2} is replaced with “New York”.

Text:
Write a business letter for {company} in the name of {name}.
```

## Conversation

**ASSISTANT**: Sorry, but I cannot complete this task without the list of variables and their corresponding values. Please provide me with the list first so that I can replace the variables in the text accordingly.
**USER**: 1. Apple

2. James
**ASSISTANT**: Here's the updated text with variables replaced:



Write a business letter for Apple in the name of James.


