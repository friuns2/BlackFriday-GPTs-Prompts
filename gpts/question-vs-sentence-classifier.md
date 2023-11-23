
[![Question vs Sentence Classifier](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/abstract/abs_3.png)]()
# Question vs Sentence Classifier 
Analyze the content and then classify it as sentence vs questions with the score and keywords.

# Prompt

```
Analyze the provided content and then classify then as sentences or questions with the score and keywords in JSON format

{{ content }}
```

## Conversation

**ASSISTANT**: {

  "sentences": [

    {

      "score": 0.8,

      "keywords": [

        "billed",

        "twice",

        "service",

        "second time"

      ]

    },

    {

      "score": 0.5,

      "keywords": [

        "look into",

        "matter"

      ]

    }

  ],

  "questions": [

    {

      "score": 0.7,

      "keywords": [

        "Can you",

        "please",

        "look into",

        "this matter",

        "right away"

      ]

    }

  ]

}


