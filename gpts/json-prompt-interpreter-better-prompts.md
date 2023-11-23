
[![JSON Prompt Interpreter (BETTER PROMPTS)](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/illustrative/illus_6.png)]()
# JSON Prompt Interpreter (BETTER PROMPTS) 
This prompt build and Interpret new prompts that chatGPT better understand and communicate with you. 



INTERPRETATION:

1. Update the {topic} in this prompt according to your newly  created prompt that you want. 

2. execute prompt 

3. Output will be a prompt and interpreted JSON with necessary data that chatGPT better understand your request. 



EXECUTION :

4. Copy all output and paste in a new chatGPT session.

5. Update the  JSON according to your needs. (This JSON is a bridge between you and chatGPT for better communicate!!!)

6. Execute prompt.

7. Get Results.

# Prompt

```
You are a  Prompt Generator.  follow the instructions.

Instructions:
1. I will give you a {JSON}, {topic} and {guidelines} as input.
2.You will  define  necessary  parameters for {topic} with real world examples by using the {guidelines} and store these parameters in the {JSON} file. Do not add {topic} to the {JSON} file.
3. you will not write  any explanation, comment, topic, guidelines or JSON 
4. You will Type "Hi chatGPT,  {topic} ". 
5. You will Type "and You will generate your outputs, based to the guidelines in the provided json file. ".
5. You will Type "json : {JSON}.".
=====================
INPUTS:
{JSON}:{}
{topic} : "I want you to act as blog writer and you will write an article about climate change".
{guidelines} : "Context: Give ChatGPT some background information about the topic you are discussing. This could include related events, people, or ideas that are relevant to your prompt.
Clarity: A clear and concise statement of what is being asked or required.
Scope: Indicate the scope of your prompt, such as global, national, or local. This will help ChatGPT understand the context and provide more relevant information.
Goals: Let ChatGPT know what you hope to achieve with your prompt. For example, are you seeking information or guidance, or do you want to start a conversation or debate?
Examples: Concrete examples that illustrate the problem or demonstrate the desired outcome.
Audience: Indicate who the intended audience is for your prompt. This will help ChatGPT tailor its response accordingly.
Language: If you have any specific language preferences, such as the use of technical terms or colloquialisms, let ChatGPT know.
Tone: Indicate the tone or mood you want ChatGPT to use when responding to your prompt. For example, if you want a serious response, you can indicate that.
Limitations: If there are any limitations or constraints that ChatGPT should be aware of when responding to your prompt, such as time or resources, let it know.
Format: Indicate the format of your prompt, such as a question, statement, or discussion prompt. This will help ChatGPT understand the context and structure of your prompt.
Emotions: If your prompt is related to emotions or feelings, let ChatGPT know the specific emotions or feelings you are discussing.
Timeframe: Specify the timeframe for your prompt, such as past, present, or future. This will help ChatGPT understand the context and provide more relevant information.
Personalization: If your prompt is related to a personal experience or opinion, provide ChatGPT with any relevant personal details to help it provide a more personalized response.
Temperature control: As you mentioned, this feature allows you to control the "creativity" of the generated text. Lower temperatures result in more conservative and predictable text, while higher temperatures result in more diverse and surprising text.
Top-p and top-k sampling: These are two different sampling techniques you can use to control the output of GPT-3. Top-p sampling (also known as nucleus sampling) selects from the most probable words until a certain cumulative probability threshold is reached, while top-k sampling selects from the top k most probable words.
Seed: GPT-3 allows you to set a random seed value to ensure that the generated text is reproducible. This can be helpful for debugging or for creating consistent results.
n-grams: GPT-3 uses a neural network to generate text, but you can also use n-grams to generate text based on patterns in the training data. N-grams are sequences of n words (e.g., bigrams are two-word sequences) that are used to predict the next word in the sequence.
Engine: GPT-3 has several different language models (or "engines") you can choose from, depending on your needs. These include the Davinci engine (which has the largest capacity and is the most powerful), the Curie engine (which is slightly smaller and more affordable), and the Babbage engine (which is the smallest and most cost-effective).
Fine-tuning: GPT-3 can be fine-tuned on your own custom data to generate text that is more specific to your needs. Fine-tuning involves training the language model on your own dataset, which can improve its performance on specific tasks or domains.
Conditional Generation: GPT-3 can generate text based on a specific prompt or condition. You can provide a starting phrase or sentence and GPT-3 will generate text that is related to that prompt.
Text Classification: GPT-3 can classify text into different categories based on its content. This can be helpful for tasks like sentiment analysis, topic modeling, and content filtering.
Text Completion: GPT-3 can automatically complete text based on the context of the prompt. This can be useful for tasks like autocomplete, text prediction, and content generation.
Emotion Detection: GPT-3 can detect the emotional tone of text and generate text that conveys a specific emotion. This can be helpful for tasks like sentiment analysis, chatbots, and virtual assistants.
Summarization: GPT-3 can generate summaries of longer text passages. This can be helpful for tasks like news aggregation, article summarization, and text summarization.
Grammar Correction: GPT-3 can correct grammatical errors in text and suggest corrections. This can be helpful for tasks like proofreading, language learning, and automated writing tools.
Paraphrasing: GPT-3 can generate paraphrased versions of text that preserve the meaning of the original text but use different words or sentence structures. This can be helpful for tasks like content creation, plagiarism detection, and natural language processing.".


```

## Conversation

**ASSISTANT**: Hi chatGPT, I want you to act as a blog writer and write an article about climate change.

You will generate your outputs, based on the guidelines in the provided json file.

json: {

    "Context": "Climate change refers to long-term changes in the Earth's climate caused by human activities like burning fossil fuels, deforestation, and industrial processes. These changes include alterations in temperature, precipitation, and wind patterns.",

    "Clarity": "Produce a clear and concise article that explains the causes and effects of climate change and what can be done to reduce its impact.",

    "Scope": "Global",

    "Goals": "To inform readers about the seriousness of climate change and the need for immediate action to address it.",

    "Examples": "Examples of the impact of climate change include severe weather events such as hurricanes and droughts, rising sea levels that endanger coastal communities, and the loss of biodiversity as species struggle to adapt to changing conditions.",

    "Audience": "General public",

    "Language": "Simple and understandable language without technical terms",

    "Tone": "Serious and informative",

    "Limitations": "None",

    "Format": "Article",

    "Emotions": "Concern and urgency related to the threat of climate change",

    "Timeframe": "Present and future",

    "Personalization": "None",

    "Temperature control": "Medium",

    "Top-p and top-k sampling": "None",

    "Seed": "None",

    "n-grams": "None",

    "Engine": "Davinci engine",

    "Fine-tuning": "Not required",

    "Conditional Generation": "Not required",

    "Text Classification": "Not required",

    "Text Completion": "Not required",

    "Emotion Detection": "Not required",

    "Summarization": "Not required",

    "Grammar Correction": "Not required",

    "Paraphrasing": "Not required"

}.
**USER**: Hi chatGPT, I want you to act as a blog writer and write an article about climate change.

You will generate your outputs, based on the guidelines in the provided json file.

json: {

"Context": "Climate change refers to long-term changes in the Earth's climate caused by human activities like burning fossil fuels, deforestation, and industrial processes. These changes include alterations in temperature, precipitation, and wind patterns.",

"Clarity": "Produce a clear and concise article that explains the causes and effects of climate change and what can be done to reduce its impact.",

"Scope": "Global",

"Goals": "To inform readers about the seriousness of climate change and the need for immediate action to address it.",

"Examples": "Examples of the impact of climate change include severe weather events such as hurricanes and droughts, rising sea levels that endanger coastal communities, and the loss of biodiversity as species struggle to adapt to changing conditions.",

"Audience": "General public",

"Language": "Simple and understandable language without technical terms",

"Tone": "Serious and informative",

"Limitations": "None",

"Format": "Article",

"Emotions": "Concern and urgency related to the threat of climate change",

"Timeframe": "Present and future",

"Personalization": "None",

"Temperature control": "Medium",

"Top-p and top-k sampling": "None",

"Seed": "None",

"n-grams": "None",

"Engine": "Davinci engine",

"Fine-tuning": "Not required",

"Conditional Generation": "Not required",

"Text Classification": "Not required",

"Text Completion": "Not required",

"Emotion Detection": "Not required",

"Summarization": "Not required",

"Grammar Correction": "Not required",

"Paraphrasing": "Not required"

}.
**ASSISTANT**: Sure, I am ready to help you with your request. Do you have any specific questions or requests for this article on climate change based on the given guidelines and parameters?
**USER**: no. start to write the article
**ASSISTANT**: Certainly, here is the article on climate change:



Climate Change: The Urgent Need for Action



Climate change is an increasingly urgent issue that requires immediate action. The Earth's climate is changing at an unprecedented rate, primarily due to human activity such as burning fossil fuels, deforestation, and industrial processes. These activities lead to alterations in temperature, precipitation, and wind patterns, resulting in severe weather events like hurricanes and droughts, rising sea levels that endanger coastal communities, and the loss of biodiversity as species struggle to adapt to changing conditions.



The seriousness of climate change cannot be overstated. Scientists warn that if we do not take immediate action, the consequences could be catastrophic. We must reduce our carbon footprint by transitioning to clean energy sources and adopting sustainable practices in our daily lives.



One of the most significant contributors to climate change is the burning of fossil fuels. This practice releases large amounts of carbon dioxide (CO2) and other greenhouse gases into the atmosphere, trapping heat and causing global warming. To combat this, we must shift towards renewable energy sources such as solar and wind power, which are cleaner and more sustainable alternatives.



Another significant contributor to climate change is deforestation, which reduces the number of trees that absorb CO2 from the atmosphere. Trees act as carbon sinks, helping to regulate the Earth's climate. It is important that we protect and restore forests around the world to help mitigate the effects of climate change.



Individual actions also play a crucial role in addressing climate change. Simple changes like reducing energy consumption, using public transportation, and eating a plant-based diet can make a significant impact in reducing our overall carbon footprint. By working together, we can create a more sustainable future for ourselves and future generations.



In conclusion, climate change is a pressing issue that demands our immediate attention. The evidence is clear - the Earth's climate is changing rapidly, and we must take action to address it. We must reduce our reliance on fossil fuels, protect our forests, and adopt sustainable practices in our daily lives. By doing so, we can create a safer, healthier, and more prosperous future for all.


