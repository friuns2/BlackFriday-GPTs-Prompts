
[![Topic Extractor](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_5.png)]()
# Topic Extractor 
This prompt is all about the extraction of the topics from the specified content

# Prompt

```
Extract the topics with the score in JSON format from the following content

{{ content }}
```

## Conversation

**ASSISTANT**: {

  "topics": [

    {

      "topic": "GPT models weakness",

      "score": 0.8

    },

    {

      "topic": "Efficiently running GPT models in production",

      "score": 0.9

    },

    {

      "topic": "Advanced DevOps knowledge",

      "score": 0.7

    },

    {

      "topic": "Hardware requirements for running GPT-J efficiently",

      "score": 0.9

    },

    {

      "topic": "Using GPUs for running GPT-J efficiently",

      "score": 0.8

    }

  ]

}


