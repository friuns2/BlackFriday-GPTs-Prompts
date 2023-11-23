
[![NER Extractor](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/minimalist/mini_2.png)]()
# NER Extractor 
This prompt is all about the extraction of the Named Entities from the specified content

# Prompt

```
Extract the NER with the score in JSON format from the following content

{{ content }}
```

## Conversation

**ASSISTANT**: Here is the Named Entity Recognition (NER) entities and their scores in JSON format from the given content:



```

{

  "entities": [

    {

      "entity": "GPT models",

      "type": "ORG",

      "score": 0.89

    },

    {

      "entity": "DevOps",

      "type": "MISC",

      "score": 0.82

    },

    {

      "entity": "GPT-J",

      "type": "ORG",

      "score": 0.98

    },

    {

      "entity": "CPU",

      "type": "PRODUCT",

      "score": 0.89

    },

    {

      "entity": "GPU",

      "type": "PRODUCT",

      "score": 0.92

    },

    {

      "entity": "NVIDIA",

      "type": "ORG",

      "score": 0.95

    },

    {

      "entity": "RTX A6000",

      "type": "PRODUCT",

      "score": 0.97

    },

    {

      "entity": "A40",

      "type": "PRODUCT",

      "score": 0.94

    }

  ]

}

```


