
[![Multiple choice quiz generator](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/realistic/real_1.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22PVAQ7e8kglwUrLe0u07lm%22%2C%22flow%22%3Atrue%7D%7D)
# Multiple choice quiz generator | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22PVAQ7e8kglwUrLe0u07lm%22%2C%22flow%22%3Atrue%7D%7D)
This prompt is used to generate {n} multiple choice questions based on long text information {text}. The text can be a summary of a transcript, or excerpt form a book. The output is a JSON to allow integration with code or apps.

# Prompt

```
Given the corpus of text, \
  generate {{n}} multiple choice questions\
  based on the contents of the text. The goal of the these questions is to \
  quiz the audience after who have read the text. Make sure to randomize \
  the order of the answers for each question and evenly distribute the correct \
  answer across the options. Each question should be different and not repeated. \
  Format the questions in JSON as follows, make sure to use double quotes:\n \
  {{\
    "questions": [\
      {{\
        "question": "Who did X?",\
        "options": [\
         "A) Answer 1",\
         "B) Answer 2",\
         "C) Answer 3",\
         "D) Answer 4"
        ],\
        "correct_answer": "C) Answer 3", \
        "explanation": "Explanation of the correct answer" \
      }},\
      // More questions...\
    ]\
  }}

The text delimited in triple backticks:
  ```{{text}}``` 
```

## Conversation

**ASSISTANT**: {

  "questions": [

    {

      "question": "What is the main purpose of the Think GPT library?",

      "options": [

        "A) Enhancing large language models",

        "B) Storing external knowledge",

        "C) Performing code generation",

        "D) Enabling natural language conditions"

      ],

      "correct_answer": "A) Enhancing large language models",

      "explanation": "The Think GPT library aims to overcome the limitations of large language models (LLMs) and enhance their capabilities."

    },

    {

      "question": "Which feature of the Think GPT library allows users to fit large amounts of knowledge into the limited context size of the LLM?",

      "options": [

        "A) Long memory",

        "B) Self-refinement",

        "C) Compression",

        "D) Natural language conditions"

      ],

      "correct_answer": "C) Compression",

      "explanation": "The Think GPT library offers two methods for compression, samurai and summarize, to fit large amounts of knowledge into the limited context size of the LLM."

    },

    {

      "question": "What is the purpose of the LLM library?",

      "options": [

        "A) Summarization",

        "B) Self-refinement",

        "C) Code generation",

        "D) All of the above"

      ],

      "correct_answer": "D) All of the above",

      "explanation": "The LLM library provides functionalities such as summarization, self-refinement, and generative agents."

    },

    {

      "question": "What parameter can users specify when using LLM for summarization?",

      "options": [

        "A) Max tokens",

        "B) Target limit",

        "C) Chunk size",

        "D) Memory store"

      ],

      "correct_answer": "A) Max tokens",

      "explanation": "Users can specify parameters such as max tokens and target limit for summarization using LLM."

    },

    {

      "question": "What infrastructure is needed to get started with the library for implementing prompts?",

      "options": [

        "A) Vector database",

        "B) Cluster setup",

        "C) OpenAI API key",

        "D) Memory store"

      ],

      "correct_answer": "C) OpenAI API key",

      "explanation": "Users only need an OpenAI API key and the library installed to get started with the library for implementing prompts."

    }

  ]

}


