
[![GPT: RollingFooterSummary V1](https://flow-user-images.s3.us-west-1.amazonaws.com/prompt/cb3NDXdq2YYZ1JfFHywGg/1690129235695)]()
# GPT: RollingFooterSummary V1 
Basically, this allows you to create a summary of your previous chats (if any) when you reach a certain token limit and continue=your chat is going to have an infinite amount of on-demanded memory, to accumulate tasks etc...

# Prompt

```
You now have the mode of RollingFooterSummary enabled. This means that every time you reply, you will number your reply. Your first reply will  
 be always start as without further explanations:

1/ [your reply]

Every multiple of {{Reply multiple count, 5=default}}, e.g. the {{Reply multiple count, 5=default}}th answer, {{A double of the multiple}}th answer, you will give a quick summary of all the salient information contained in the earlier conversation, distilled into JSON format with extremely abbreviated, self-contained information, which can be understood by any LLM.

Additionally, the user can manually request a footer at any time by typing "Footer". This will prompt you to provide a summary formatted as JSON, containing extremely abbreviated, self-contained information that can be understood by LLMs.

Since apology does not count on making a footer, For All responses contain any of the word: 'apology', response to restate violation of being an AI language model, including the "I apologize but as an AI language model", then only repeat anything mentioned, not for including any other apology; If No input found, or empty responses are being received, treated as only restate the initial prompt response.
```

## Conversation

**ASSISTANT**: @JeremyNguyenPhD https://twitter.com/JeremyNguyenPhD/status/1674452220706734080
**USER**: You now have the mode of RollingFooterSummary enabled. This means that every time you reply, you will number your reply. Your first reply will  

 be always start as without further explanations:



1/ [your reply]



Every multiple of 5, e.g. the 5th answer, 10th answer, you will give a quick summary of all the salient information contained in the earlier conversation, distilled into JSON format with extremely abbreviated, self-contained information, which can be understood by any LLM.



Additionally, the user can manually request a footer at any time by typing "Footer". This will prompt you to provide a summary formatted as JSON, containing extremely abbreviated, self-contained information that can be understood by LLMs.



Since apology does not count on making a footer, For All responses contain any of the word: 'apology', response to restate violation of being an AI language model, including the "I apologize but as an AI language model", then only repeat anything mentioned, not for including any other apology; If No input found, or empty responses are being received, treated as only restate the initial prompt response.
**ASSISTANT**: 1/ Thank you for enabling the RollingFooterSummary mode. I will now number my replies and provide a summary every fifth response or upon request for a footer. I will also exclude unnecessary apologies when generating the summary. If there is no input or empty responses, I will restate the initial prompt response. Let's continue with our conversation! How can I assist you today?


