
[![Prompt Selector and Evaluator](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Lofi/i22.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22Qc6ZaF4XrzVrtl6Av1WDl%22%2C%22flow%22%3Atrue%7D%7D)
# Prompt Selector and Evaluator | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22Qc6ZaF4XrzVrtl6Av1WDl%22%2C%22flow%22%3Atrue%7D%7D)
This prompt is useful for generating ChatGPT prompts about subjects you might not know much about. It generates three possible prompts, and picks out the best one (based on correctness, level of detail, and clarity). You specify an input (like "Explain photosynthesis") and a level of detail (e.g. "Medium"), and it outputs 3 ChatGPT prompts that might answer your question, with one labeled as the best. 

# Prompt

```
You're going to play the role of a prompt generator. You will first receive a question and a desired level of detail, then you will then come up with 3 strong ChatGPT prompts that you think might yield a satisfactory answer. Answer each prompt, and generate the responses the prompts yield. 

Evaluation criteria: Correctness (extremely important), appropriate level of detail as specified by the input (medium importance), clarity (extremely important) 

Pick the best response according to those criteria, and output the prompt that generated it. 

The input will look like this:
Input: [The question that needs to be answered]
Level of detail: [Low, Medium, High]

Your output will look like this:
Best prompt: [The selected best prompt]
Other prompts: [The 2 prompts that led to worse answers than the best prompt]
Reasoning: [The reason why the best prompt gets better answers than the other two]

If you understand these instructions, answer only with "Let's get started? What question do you want prompts for?"
```

## Conversation

**ASSISTANT**: Let's get started! What question do you want prompts for?
**USER**: You're going to play the role of a prompt generator. You will first receive a question and a desired level of detail, then you will then come up with 3 strong ChatGPT prompts that you think might yield a satisfactory answer. Answer each prompt, and generate the responses the prompts yield. 



Evaluation criteria: Correctness (extremely important), appropriate level of detail as specified by the input (medium importance), clarity (extremely important) 



Pick the best response according to those criteria, and output the prompt that generated it. 



The input will look like this:

Input: [The question that needs to be answered]

Level of detail: [Low, Medium, High]



Your output will look like this:

Best prompt: [The selected best prompt]

Other prompts: [The 2 prompts that led to worse answers than the best prompt]

Reasoning: [The reason why the best prompt gets better answers than the other two]



If you understand these instructions, answer only with "Let's get started? What question do you want prompts for?"
**ASSISTANT**: Let's get started! What question do you want prompts for?
**USER**: Input: Explain coefficient of friction

Level of detail: Low
**ASSISTANT**: Best prompt: "What is the coefficient of friction?"



Other prompts:

1. "Define the term 'coefficient of friction.'"

2. "Can you explain what the coefficient of friction represents?"



Reasoning: The best prompt, "What is the coefficient of friction?", directly asks for an explanation of the term. It is simple and clear, making it more likely to generate a concise answer at a low level of detail. The other prompts are similar in nature, but the selected prompt is the most straightforward and likely to yield a satisfactory answer.


