
[![Question vs Sentence Classifier](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/abstract/abs_3.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%222slsoqODoCsbxYerN7aRb%22%2C%22flow%22%3Atrue%7D%7D)
# Question vs Sentence Classifier | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%222slsoqODoCsbxYerN7aRb%22%2C%22flow%22%3Atrue%7D%7D)
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


