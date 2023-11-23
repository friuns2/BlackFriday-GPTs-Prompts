
[![Video Summarizer GPT](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/cute/cute_5.png)]()
# Video Summarizer GPT 
This chatGPT prompt summarize the video transcript and give you a easy-to-understand overview of the video.

# Prompt

```
Act as a summarizer. You will summarize the transcript of an online course. I will provide you the transcript of the online course. Because the transcript could be very long, I may break the section into pieces and feed to you one by one. 

The summarize should be comprehensive and concise. It should be understandable by 17 year old teenager. Some of the formatting tips:
Highlight important works/lines in bold.
Use third party tone. 

{{ Your Transcript to summarize }}
```

## Conversation

**ASSISTANT**: In this online course, the instructor teaches how to use OpenAI ChatCompletions format to build custom chatbots. The chat models are designed to take a series of messages as input and return a model-generated message as output, making it useful for single-turn tasks without any conversation. Two helper functions are defined to assist in getting prompt inputs and returning outputs from the model. A system message is explained to provide developers with a way to frame the conversation without making the user aware of the request itself. The instructor explains how to use context to make the model retain earlier parts of the conversation. Students are then guided through building their own chatbot called "OrderBot" that automates collecting orders at a pizza restaurant. The use of a lower temperature is recommended for this bot because the output should be predictable. Finally, the instructor shows how to create a JSON summary of the previous food order that can be sent to the order system based on the conversation.


