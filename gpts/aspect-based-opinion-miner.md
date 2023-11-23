
[![Aspect Based Opinion Miner](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_10.png)]()
# Aspect Based Opinion Miner 
Aspect-Based Opinion Mining involves extracting aspects or features of an entity and figuring out opinions about those aspects. It's a method of text classification that has evolved from sentiment analysis and named entity extraction (NER). ABOM is thus a combination of aspect extraction and opinion

# Prompt

```
Based on the specified content, analyze and provide the aspect-based opinion mining by classifying the aspect and provide with the score and full sentence and also classify whether it's a neutral, positive or negative in JSON format

{{ content }}
```

## Conversation

**ASSISTANT**: {

    "Aspect": "Performance",

    "Score": 0.8,

    "Sentiment": "Positive",

    "Sentence": "John has filled big role in my team as Sr Manager RF Planning and have shown Good progress. John has managed to meet and often exceed target for AOP sites month on month. He has shown true leadership and demonstrated outstanding performance by pitching in and tracking U900swap, capacity addition and making sure sites goes on Air without a hitch."

}



{

    "Aspect": "Leadership",

    "Score": 0.9,

    "Sentiment": "Positive",

    "Sentence": "He has shown true leadership and demonstrated outstanding performance by pitching in and tracking U900swap, capacity addition and making sure sites goes on Air without a hitch."

}



{

    "Aspect": "Company Culture",

    "Score": 0.7,

    "Sentiment": "Positive",

    "Sentence": "John has lived up the true Vodafone way."

}



{

    "Aspect": "Overall Performance",

    "Score": 0.7,

    "Sentiment": "Positive",

    "Sentence": "Overall Appreciation for performance in last 12 months: John has filled big role in my team as Sr Manager RF Planning and have shown Good progress."

} 



The overall sentiment of the review is positive with an appreciation of John's performance as the Sr Manager RF Planning. The specific aspects that have been mentioned are "Performance," "Leadership," "Company Culture," and "Overall Performance." Each aspect has been rated positively with scores of 0.8, 0.9, 0.7, and 0.7 respectively, and classified as such in JSON format.


