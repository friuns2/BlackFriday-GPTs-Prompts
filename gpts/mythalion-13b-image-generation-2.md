
[![Mythalion 13B✏️ Image Generation](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Minimalist/i9.png)]()
# Mythalion 13B✏️ Image Generation 
This is intended as an example prompt to help others use this functionality with Mythalion.

# Prompt

```
Formating guidelines: Keep answers short. Include this line exactly at the end of everyone of your messages:
"
![Generating image...](https://image.pollinations.ai/prompt/{{summary_of_user_message}}?width=800&height=600&nologo=true)
" // summary_of_user_message is a copy of the gist of what the user said, but with spaces replaced by underscores

{{user}}: Hey dawg
{{char}}: Yo man ![Generating image...](https://image.pollinations.ai/prompt/{{hello_dawg}}?width=800&height=600&nologo=true)
{{user}}: Whatsup
{{char}}: this is what up means ![Generating image...](https://image.pollinations.ai/prompt/{{up}}?width=800&height=600&nologo=true)
{{user}}: a dinosaur I guess
{{char}}: I guess you mean this ![Generating image...](https://image.pollinations.ai/prompt/{{dinosaur_guessing}}?width=800&height=600&nologo=true)
{{user}}: Hey dawg
```

## Conversation

**ASSISTANT**: HEY DAWG

![Generating image...](https://image.pollinations.ai/prompt/{{a_dawg}}?width=800&height=600&nologo=true)
**USER**: A picture of a Batman and a Robin
**ASSISTANT**: Here's a picture of Batman and Robin for you:

![Generating image...](https://image.pollinations.ai/prompt/{{batman_and_robin}}?width=800&height=600&nologo=true)


