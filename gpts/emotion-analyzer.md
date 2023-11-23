
[![Emotion Analyzer](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/minimalist/mini_7.png)]()
# Emotion Analyzer 
Read the content and then perform the automated emotion analysis

# Prompt

```
Classify the following text into joy, others, surprise, sadness, fear, anger, disgust and then associate a score for each one of them in JSON. Do not output text on your own apart from the JSON response.

Text: {{ text }}
```

## Conversation

**ASSISTANT**: {

  "joy": 0.854,

  "others": 0.135,

  "surprise": 0.003,

  "sadness": 0.003,

  "fear": 0.002,

  "anger": 0.002,

  "disgust": 0.001

}


