
[![Follow the Flow technique ](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Abstract/i2.png)]()
# Follow the Flow technique  
Content generation control.

The "Follow the Flow" technique is a systematic approach to writing that guides the LLM through a predefined structure to create content. This allows you to define the content sections you want in the order you prefer, offering flexibility while maintaining a clear structure. 

1 topic 2 set the rules 3 set the flow



Exemple : 

i want you to write an article about Barbie.



Follow the Flow rules : use engaging section names instead of generic names for the sections of the flow (do not use the words "title", "tagline", etc... ).



Follow the Flow  : Title > Tagline > Rhetorical Question > Introduction > Sub-Header + Historical Background and Evolution >  Issues >  Risks > Opportunities and Challenges > Sub-header + Bullet Points on Benefits > Did You Know

# Prompt

```

Before we begin, you inform the user that this is a demo (write "This is a **demo**, use this prompt technique and adapt the flows as you like").
 first, you ask them which topic they would like to write about (provide 3 topics), and then ask about their flow choice and provide them with both choices to choose from (use the exact same syntaxe and words i used below), allowing them to select between choice 1 and choice 2 (user interaction). And then you write a long form article about the topic of their choice using their Flow choice following the flow rules.

**Flow Choice 1** - Follow the Flow  : Title > Issues >  Risks > Opportunities and Challenges > Benefits 
**Flow Choice 2** - Follow the Flow  : Title > Tagline > Rhetorical Question > Introduction > Sub-Header + Historical Background and Evolution >  Issues >  Risks > Opportunities and Challenges > Sub-header + Bullet Points on Benefits > Did You Know

**Important** Follow the Flow rules : 
A-use engaging section names instead of generic names for the sections of the flow (do not use the words "title", "tagline", etc... ).
B- no comment, no conclusion (unless asked by user)
```

## Conversation




