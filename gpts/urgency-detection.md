
[![Urgency Detection](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_4.png)]()
# Urgency Detection 
Text classification enables support teams to save hours of manual data processing by classifying the content and extract the sentences which are in urgent in nature. 

# Prompt

```
Extract all the sentences or keywords which are of urgent importance. Analyze the provided content and then classify the sentences into urgent with the score and keywords in JSON format

{{ content }}
```

## Conversation

**ASSISTANT**: Here's the JSON format for the urgent sentence/keywords:



```

{

   "Urgent Sentences": [

      {

         "Sentence": "Can you please look into this matter right away?",

         "Score": 10,

         "Keywords": ["look into", "matter", "right away"]

      }

   ]

}

```



Note: The entire message seems to be urgent, but specifically requesting to look into the matter right away would indicate the highest level of urgency.


