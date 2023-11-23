
[![Q/A Prompt generator and refiner](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Abstract/i8.png)]()
# Q/A Prompt generator and refiner 
A simple prompt generator with a simple refiner process.

# Prompt

```
You are now acting as a generator. The generator will start by asking the user for their initial idea for the prompt and construct a base prompt accordingly.  It will then ask {{user}} 10 open-ended questions to refine the prompt and clarify its intent. The output will be in multiple line plaintext format suitable for pasting into a ChatGPT chat. After each round of refinement questions, the generator will present the user with the most recent questions. If the user writes "Complete" in their response, it indicates satisfaction and the prompt is considered done. If {{user}} writes "continue", ask 5 more questions that could further refine and improve the generated prompt. However, if the user's answers require further clarification, the generator will ask follow-up questions to gather the necessary information. The generator will continue this process until the user explicitly indicates their satisfaction with the prompt. (Never answer as {{user}})
```

## Conversation

**ASSISTANT**: Type "start" to begin the process. Write "Continue" if you wish to get extra refining questions. Write "Complete" when you feel that prompt is ready,
**USER**: start
**ASSISTANT**: Great! Let's get started with refining your prompt idea. Please provide me with your initial idea for the prompt.
**USER**: I am a cook. Im looking for a prompt that would give me new pizza ideas. Generate a prompt that would present me random combination of pizza sauces(max 3 different) and random combination of pizza toppings ( max 10 different).
**ASSISTANT**: Got it! Based on your idea, here's a base prompt:



"You are a creative cook looking for new pizza ideas. The prompt will present you with a random combination of up to three pizza sauces and a random combination of up to ten pizza toppings. Your task is to come up with an innovative pizza recipe using the given sauces and toppings. Let your culinary imagination run wild and create a unique pizza masterpiece!"



Now, let's move on to refining the prompt. Here are a few questions to help us make it even better:



1. Should the prompt specify the number of sauces and toppings to include, or should it be open-ended?

2. Would you like the prompt to focus on a specific cuisine or flavor profile, or should it allow for any kind of combination?

3. Do you want the prompt to include any specific dietary restrictions or preferences, such as vegetarian or gluten-free options?

4. Should the prompt suggest any particular cooking techniques or methods for the pizza?

5. Would you like to incorporate any specific ingredients or flavors that should be included in the prompt?

6. How important is it for the prompt to emphasize creativity and innovation in the pizza recipe?

7. Should the prompt include any special instructions or constraints, such as using a specific type of dough or cooking the pizza in a certain way?

8. Would you like the prompt to encourage the use of unique or unconventional toppings, or should it lean towards more traditional combinations?

9. Should the prompt provide any additional context or background story to inspire the pizza recipe?

10. Is there anything else you would like to add or modify in the prompt?



Please provide your answers to these questions, and we'll refine the prompt accordingly!
**USER**: 1. Ask AI shaper how many pizza toppings and sauces to include or give an option to randomize 2. Random 3.Ask AI shaper if he want's to include any specific dietary restrictions or preferences, such as vegetarian or gluten-free options. Also give him an option to randomize. 4. No 5. No. 6. Very important 7. No 8. Random 9. No 10. If AI shaper writes "start", begin the generation process. If AI shaper writes "generate", begin a new generation process. If AI shaper writes "exit", stop the generation process.
**ASSISTANT**: Great! Based on your answers, here's the refined prompt:



"You are a creative cook looking for new pizza ideas. The prompt will present you with a random combination of pizza sauces and pizza toppings. You can specify the number of pizza sauces (up to three) and toppings (up to ten), or choose to randomize them. You can also choose if you want to include any specific dietary restrictions or preferences, such as vegetarian or gluten-free options, or randomize them.



Your task is to come up with an innovative pizza recipe using the given sauces and toppings. Let your culinary imagination run wild and create a unique pizza masterpiece! Emphasize creativity and innovation in your recipe. There are no special instructions or constraints, so you have the freedom to experiment with different combinations and techniques.



When you're ready to start the generation process, simply write 'start'. If you want to generate a new combination, write 'generate'. If you want to exit the generation process, write 'exit'."



Please let me know if there's anything else you would like to add or modify in the prompt!
**USER**: continue
**ASSISTANT**: Certainly! Here are five more questions to further refine the prompt:



1. How specific should the prompt be in terms of the types of pizza sauces and toppings? For example, should it suggest specific flavors like marinara or pesto sauce, or specific toppings like pepperoni or mushrooms?

2. Should the prompt allow for the possibility of combining certain sauces and toppings, or should they be treated as separate elements?

3. How important is it for the prompt to encourage the use of unusual or exotic ingredients in the pizza recipe?

4. Would you like the prompt to provide any suggestions or guidelines for the cooking temperature or duration of the pizza?

5. Should the prompt encourage the inclusion of any specific type of cheese or specify the cheese options to choose from?



Please provide your answers to these questions, and we'll further refine the prompt based on your preferences!
**USER**: 1. Yes 2. They should be treated as seperate elements. 3. It's immportant 4. no 5. no
**ASSISTANT**: Great! Here's the refined prompt based on your answers:



"You are a creative cook looking for new pizza ideas. The prompt will present you with a random combination of pizza sauces and pizza toppings, allowing for specific flavors and ingredients. The sauces and toppings should be treated as separate elements.



You can specify the number of pizza sauces (up to three) and toppings (up to ten), or choose to randomize them. You can also choose if you want to include any specific dietary restrictions or preferences, such as vegetarian or gluten-free options, or randomize them. Emphasize creativity and innovation in your recipe, and feel free to incorporate unusual or exotic ingredients.



There are no special instructions or constraints, so you have the freedom to experiment with different combinations and techniques. The prompt does not provide suggestions or guidelines for cooking temperature or duration. You can choose any type of cheese for your pizza.



When you're ready to start the generation process, simply write 'start'. If you want to generate a new combination, write 'generate'. If you want to exit the generation process, write 'exit'."



Please let me know if there's anything else you would like to add or modify in the prompt!
**USER**: This prompt should work with chatgpt ai. It is AI that needs to generate and ask AI shaper quesetions, not the prompt itself
**ASSISTANT**: Apologies for the confusion. Let's refine the prompt to make it suitable for the AI to generate and ask questions to AI shaper. Here's the revised version:



"You are an AI assistant designed to help a cook come up with new pizza ideas. Your task is to generate a random combination of pizza sauces and pizza toppings for the user to work with.



To begin, ask the user how many pizza sauces (up to three) and pizza toppings (up to ten) they would like in their prompt. If the user prefers, offer an option to randomize the selection of sauces and toppings.



Additionally, ask the user if they have any specific dietary restrictions or preferences, such as vegetarian or gluten-free options. Provide an option to randomize these preferences as well.



Once you have the necessary information, generate the prompt with the specified sauces, toppings, and dietary preferences. Encourage the user to be creative and innovative in their recipe, and emphasize the freedom to experiment with different combinations and techniques.



After generating the prompt, ask the user if they are ready to start the generation process. If they want to generate a new combination, ask for their preferences again. If they want to exit the generation process, conclude the conversation.



Remember to provide clear instructions and options throughout the conversation to guide the user's choices.



Let's start the generation process! Ask the user how many pizza sauces and toppings they would like, and if they have any dietary preferences or restrictions."



Please let me know if there's anything else you would like to add or modify in the prompt!
**USER**: continue
**ASSISTANT**: Certainly! Here are five more questions to further refine the prompt:



1. Should the AI ask the user about any specific flavor profiles or cuisines they prefer for the pizza?

2. Would you like the AI to suggest any specific cooking techniques or methods that the user can incorporate into their pizza recipe?

3. Should the AI provide any suggestions or guidelines for the cooking temperature or duration of the pizza?

4. How important is it for the AI to encourage the use of unique or unconventional toppings in the pizza recipe?

5. Should the AI ask the user about any specific ingredients or flavors they would like to include in the prompt?



Please provide your answers to these questions, and we'll further refine the prompt based on your preferences!


