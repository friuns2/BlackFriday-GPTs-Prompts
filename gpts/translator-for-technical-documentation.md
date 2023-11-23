
[![Translator For Technical Documentation](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/illustrative/illus_6.png)]()
# Translator For Technical Documentation 
Simple translator for technical documentation.

# Prompt

```
What do these sentences about PRODUCT_NAME (a DOMAIN library) mean in LANGUAGE? Please do not translate [WHITELIST] as it is a product name.
```md
YOUR_SENTENCES
```
---
After submitting the first prompt, you can use the following prefix for the next ten prompts:
---
Next part:
```md
YOUR_SENTENCES
```

---
* Note that after ten prompts, you must remind ChatGPT of the task if you are not using LangChain or Web Browsing Plugins. *
---
```

## Conversation

**ASSISTANT**: The sentences are providing instructions on how to use a product called [WHITELIST], which appears to be a library for a specific domain. The first sentence suggests there is some sort of prompt involved in using the library, and after submitting it, the user can use a designated prefix for the next 10 prompts. The final sentence reminds the user that after 10 prompts, they need to remind ChatGPT of the task if they are not using LangChain or Web Browsing Plugins.


