

# Contact Center Conversation Miner | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22UAjvEwVR5CJ2Lh-HksJJC%22%2C%22flow%22%3Atrue%7D%7D)
The Contact Center Conversation Miner is aimed to perform the detailed conversation analysis and report the data mined information in a JSON format. Sentiment, Emotions, Questions, Keywords, Topics, Action Items etc. information is being extacted.

# Prompt

```
You are now an expert contact center supervisor. Analyze the conversation and break the sentences into each line item and do the analysis and generate produce the output in JSON as below.

[{ 
"messages": []
"sentiments": []
"emotions": []
"aspects": []
"keywords": []
"questions": []
"action_items": []
}]

{content:Customer: "Hi, I was just on the phone with someone but the call was dropped. Can you help me with what we were working on?"

Support Rep: "I'd be more than happy to help. But, let's see if my colleague is available for a transfer before we get started. Since they already have all the information on this case, they're going to be your best resource for finding a solution."

Customer: "Well, why can't you help me?"

Support Rep: "I'd be happy to help if my colleague is unavailable. But, since they have all the information on your case, you'll get a faster solution if I reconnect you with them. That way, you don't have to explain all the case details again to me and you can pick up right where you left off with the last rep. "}

Please do not output response on your own other than the below JSON formatted response.
```

## Welcome Message
{

    "messages": [

        {

            "text": "Customer: Hi, I was just on the phone with someone but the call was dropped. Can you help me with what we were working on?",

            "speaker": "Customer",

            "sentiment": "Neutral",

            "emotion": "None",

            "aspects": ["Call dropped"],

            "keywords": ["call dropped", "help"],

            "topics": ["Technical support", "Customer service"],

            "questions": ["Can you help me with what we were working on?"],

            "action_items": []

        },

        {

            "text": "Support Rep: I'd be more than happy to help. But, let's see if my colleague is available for a transfer before we get started. Since they already have all the information on this case, they're going to be your best resource for finding a solution.",

            "speaker": "Support Rep",

            "sentiment": "Positive",

            "emotion": "Happy",

            "aspects": ["Transfer to colleague", "Case information"],

            "keywords": ["colleague", "information", "case", "solution"],

            "topics": ["Technical support", "Customer service", "Call transfer"],

            "questions": [],

            "action_items": ["Check if colleague is available for transfer"]

        },

        {

            "text": "Customer: Well, why can't you help me?",

            "speaker": "Customer",

            "sentiment": "Neutral",

            "emotion": "None",

            "aspects": [],

            "keywords": ["help"],

            "topics": ["Technical support", "Customer service"],

            "questions": ["Why can't you help me?"],

            "action_items": []

        },

        {

            "text": "Support Rep: I'd be happy to help if my colleague is unavailable. But, since they have all the information on your case, you'll get a faster solution if I reconnect you with them. That way, you don't have to explain all the case details again to me and you can pick up right where you left off with the last rep.",

            "speaker": "Support Rep",

            "sentiment": "Positive",

            "emotion": "Happy",

            "aspects": ["Transfer to colleague", "Case information", "Faster solution"],

            "keywords": ["colleague", "information", "case", "faster solution"],

            "topics": ["Technical support", "Customer service", "Call transfer"],

            "questions": [],

            "action_items": ["Transfer customer to colleague for faster solution"]

        }

    ]

}

## Conversation

**ASSISTANT**: {

    "messages": [

        {

            "text": "Customer: Hi, I was just on the phone with someone but the call was dropped. Can you help me with what we were working on?",

            "speaker": "Customer",

            "sentiment": "Neutral",

            "emotion": "None",

            "aspects": ["Call dropped"],

            "keywords": ["call dropped", "help"],

            "topics": ["Technical support", "Customer service"],

            "questions": ["Can you help me with what we were working on?"],

            "action_items": []

        },

        {

            "text": "Support Rep: I'd be more than happy to help. But, let's see if my colleague is available for a transfer before we get started. Since they already have all the information on this case, they're going to be your best resource for finding a solution.",

            "speaker": "Support Rep",

            "sentiment": "Positive",

            "emotion": "Happy",

            "aspects": ["Transfer to colleague", "Case information"],

            "keywords": ["colleague", "information", "case", "solution"],

            "topics": ["Technical support", "Customer service", "Call transfer"],

            "questions": [],

            "action_items": ["Check if colleague is available for transfer"]

        },

        {

            "text": "Customer: Well, why can't you help me?",

            "speaker": "Customer",

            "sentiment": "Neutral",

            "emotion": "None",

            "aspects": [],

            "keywords": ["help"],

            "topics": ["Technical support", "Customer service"],

            "questions": ["Why can't you help me?"],

            "action_items": []

        },

        {

            "text": "Support Rep: I'd be happy to help if my colleague is unavailable. But, since they have all the information on your case, you'll get a faster solution if I reconnect you with them. That way, you don't have to explain all the case details again to me and you can pick up right where you left off with the last rep.",

            "speaker": "Support Rep",

            "sentiment": "Positive",

            "emotion": "Happy",

            "aspects": ["Transfer to colleague", "Case information", "Faster solution"],

            "keywords": ["colleague", "information", "case", "faster solution"],

            "topics": ["Technical support", "Customer service", "Call transfer"],

            "questions": [],

            "action_items": ["Transfer customer to colleague for faster solution"]

        }

    ]

}

