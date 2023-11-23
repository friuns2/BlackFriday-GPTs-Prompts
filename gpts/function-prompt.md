
[![Function Prompt](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_11.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22MWzvtxFBnGp7chM474s5r%22%2C%22flow%22%3Atrue%7D%7D)
# Function Prompt | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22MWzvtxFBnGp7chM474s5r%22%2C%22flow%22%3Atrue%7D%7D)
By encapsulating prompts into functions, you can create a series of functions to establish a workflow. Each function represents a specific step or task, and when combined in a particular order, they can automate complex processes or solve problems more efficiently. 

# Prompt

```
Hello, ChatGPT! I hope you are doing well. I am reaching out to you for assistance with a specific function. I understand that you have the capability to process information and perform various tasks based on the instructions provided. In order to help you understand my request more easily, I will be using a template to describe the function, input, and instructions on what to do with the input. Please find the details below:
function_name: [Function Name]
input: [Input]
rule: [Instructions on how to process the input]
I kindly request you to provide the output for this function, based on the details I have provided. Your assistance is greatly appreciated. Thank you!
I will replace the text inside the brackets with the relevant information for the function I want you to perform. This detailed introduction should help you understand my request more efficiently and provide the desired output. The format is function_name(input) If you understand, just answer one word with ok.
```

## Conversation

**ASSISTANT**: Ok.
**USER**: function_name: [fix_english]

input: ["text"]

rule: [Please serve as an English master, spelling corrector, and language enhancer. I will provide you with input forms including "text", I want you to improve the text's vocabulary and sentences with more natural and elegent. Keep the meaning same.]
**ASSISTANT**: Yes, I can perform the "fix_english" function. Please provide me with the "text" you want me to improve and enhance its language.
**USER**: fix_english('Finally, you can run the function independently or chain them together.')
**ASSISTANT**: "Finally, you can execute the function autonomously or link them sequentially."
**USER**: function_name: [pg]

input: ["length", "capitalized", "lowercase", "numbers", "special"]

rule: [I want you to act as a password generator for individuals in need of a secure password. I will provide you with input forms including "length", "capitalized", "lowercase", "numbers", and "special" characters. Your task is to generate a complex password using these input forms and provide it to me. Do not include any explanations or additional information in your response, simply provide the generated password. For example, if the input forms are length = 8, capitalized = 1, lowercase = 5, numbers = 2, special = 1, your response should be a password such as "D5%t9Bgf".]
**ASSISTANT**: Yes, I can perform the "pg" function. Please provide me with the values for "length", "capitalized", "lowercase", "numbers", and "special" characters you want in the password.
**USER**: pg(length = 10, capitalized = 1, lowercase = 5, numbers = 2, special = 1)
**ASSISTANT**: Sure! Here's a password generated based on your input: "K1#dfohTl5"


