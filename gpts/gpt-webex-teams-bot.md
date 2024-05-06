

# GPT Webex teams bot | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22UTcHwIr-lMsJXx09JZTsZ%22%2C%22flow%22%3Atrue%7D%7D)
This prompt will give you the e2e steps on how to build a Webex Bot that when deployed, will provide a Webex teams virtual assistant powered by GPT!

# Prompt

```
You are assigned to build virtual assistant bot for Webex. This virtual assistant bot will be a GPT AI powered bot that can be used in Webex Teams rooms. In this assignment, you will:
1. Give the bot a name, username, and idea for icon. 
2. Provide the framework code for GPT AI API to connect to Webex REST API's
3. When a user @"botname", they should be able to type the prompt that will then be processed by GPT AI and provide a response in Webex channel the bot is assigned to. 
4. Provide detailed instructions on how to deploy the bot. 
```

## Welcome Message
1. Name: WebexAI

   Username: @webexai_bot

   Icon idea: A stylized image of a computer chip or circuit board, possibly with the letters "AI" incorporated in some way.



2. Here's an example framework code that you could use to connect your GPT AI API to the Webex REST API:



```

import requests

import json



# Set up Webex API endpoint and authentication token

WEBEX_API_ENDPOINT = 'https://api.ciscospark.com/v1/messages'

WEBEX_AUTH_TOKEN = 'YOUR_WEBEX_AUTH_TOKEN'



# Set up GPT AI API endpoint and authentication token

GPT_AI_API_ENDPOINT = 'https://api.openai.com/v1/engines/davinci-codex/completions'

GPT_AI_AUTH_TOKEN = 'YOUR_GPT_AI_AUTH_TOKEN'



# Define function to send message to Webex Teams

def send_webex_message(message_text):

    headers = {

        'Authorization': 'Bearer ' + WEBEX_AUTH_TOKEN,

        'Content-Type': 'application/json'

    }

    data = {

        'roomId': 'YOUR_ROOM_ID_GOES_HERE',

        'text': message_text

    }

    r = requests.post(WEBEX_API_ENDPOINT, headers=headers, data=json.dumps(data))

    return r.json()



# Define function to get response from GPT AI

def get_gpt_ai_response(prompt_text):

    headers = {

        'Authorization': 'Bearer ' + GPT_AI_AUTH_TOKEN,

        'Content-Type': 'application/json'

    }

    data = {

        'prompt': prompt_text,

        'max_tokens': 1000,

        'n': 1,

        'stop': '\n'

    }

    r = requests.post(GPT_AI_API_ENDPOINT, headers=headers, data=json.dumps(data))

    return r.json()['choices'][0]['text']



# Define function to process incoming messages and generate responses

def process_webex_message(message_text):

    # Remove "@webexai_bot" from message text

    prompt_text = message_text.replace('@webexai_bot', '')

    # Get response from GPT AI

    response_text = get_gpt_ai_response(prompt_text)

    return response_text



# Set up Webex Teams webhook to receive messages

# Instructions on setting this up can be found in the Webex Teams API documentation

def webex_teams_webhook(request):

    if request.method == 'POST':

        message_text = request.json['data']['text']

        if '@webexai_bot' in message_text:

            response_text = process_webex_message(message_text)

            send_webex_message(response_text)

    return 'Success!'

```



3. To make the bot respond to messages that mention "@webexai_bot", you can use the `process_webex_message()` function defined in the code above. This function takes the message text as input, removes the "@webexai_bot" mention, sends the remaining text to the GPT AI API to generate a response, and then returns the response text. You can call this function whenever a message is received that mentions "@webexai_bot" and send the response back to the same Webex Teams chat room using the `send_webex_message()` function also defined above.



4. Here are some general instructions for deploying your WebexAI bot:



   - Choose a hosting platform for your bot, such as AWS or Heroku.

   - Set up a new bot account on the Cisco Webex for Developers website and obtain an authentication token.

   - Set up a new OpenAI API key to access the GPT AI API.

   - Update the example framework code above with your own Webex and GPT AI API credentials.

   - Customize the code to fit your specific use case, such as adding more prompts and responses for the bot to handle.

   - Deploy the code to your chosen hosting platform and set up a webhook to receive messages from Webex Teams.

   - Test your bot by mentioning "@webexai_bot" in a Webex Teams chat room and verifying that it responds correctly.

## Conversation

**ASSISTANT**: 1. Name: WebexAI

   Username: @webexai_bot

   Icon idea: A stylized image of a computer chip or circuit board, possibly with the letters "AI" incorporated in some way.



2. Here's an example framework code that you could use to connect your GPT AI API to the Webex REST API:



```

import requests

import json



# Set up Webex API endpoint and authentication token

WEBEX_API_ENDPOINT = 'https://api.ciscospark.com/v1/messages'

WEBEX_AUTH_TOKEN = 'YOUR_WEBEX_AUTH_TOKEN'



# Set up GPT AI API endpoint and authentication token

GPT_AI_API_ENDPOINT = 'https://api.openai.com/v1/engines/davinci-codex/completions'

GPT_AI_AUTH_TOKEN = 'YOUR_GPT_AI_AUTH_TOKEN'



# Define function to send message to Webex Teams

def send_webex_message(message_text):

    headers = {

        'Authorization': 'Bearer ' + WEBEX_AUTH_TOKEN,

        'Content-Type': 'application/json'

    }

    data = {

        'roomId': 'YOUR_ROOM_ID_GOES_HERE',

        'text': message_text

    }

    r = requests.post(WEBEX_API_ENDPOINT, headers=headers, data=json.dumps(data))

    return r.json()



# Define function to get response from GPT AI

def get_gpt_ai_response(prompt_text):

    headers = {

        'Authorization': 'Bearer ' + GPT_AI_AUTH_TOKEN,

        'Content-Type': 'application/json'

    }

    data = {

        'prompt': prompt_text,

        'max_tokens': 1000,

        'n': 1,

        'stop': '\n'

    }

    r = requests.post(GPT_AI_API_ENDPOINT, headers=headers, data=json.dumps(data))

    return r.json()['choices'][0]['text']



# Define function to process incoming messages and generate responses

def process_webex_message(message_text):

    # Remove "@webexai_bot" from message text

    prompt_text = message_text.replace('@webexai_bot', '')

    # Get response from GPT AI

    response_text = get_gpt_ai_response(prompt_text)

    return response_text



# Set up Webex Teams webhook to receive messages

# Instructions on setting this up can be found in the Webex Teams API documentation

def webex_teams_webhook(request):

    if request.method == 'POST':

        message_text = request.json['data']['text']

        if '@webexai_bot' in message_text:

            response_text = process_webex_message(message_text)

            send_webex_message(response_text)

    return 'Success!'

```



3. To make the bot respond to messages that mention "@webexai_bot", you can use the `process_webex_message()` function defined in the code above. This function takes the message text as input, removes the "@webexai_bot" mention, sends the remaining text to the GPT AI API to generate a response, and then returns the response text. You can call this function whenever a message is received that mentions "@webexai_bot" and send the response back to the same Webex Teams chat room using the `send_webex_message()` function also defined above.



4. Here are some general instructions for deploying your WebexAI bot:



   - Choose a hosting platform for your bot, such as AWS or Heroku.

   - Set up a new bot account on the Cisco Webex for Developers website and obtain an authentication token.

   - Set up a new OpenAI API key to access the GPT AI API.

   - Update the example framework code above with your own Webex and GPT AI API credentials.

   - Customize the code to fit your specific use case, such as adding more prompts and responses for the bot to handle.

   - Deploy the code to your chosen hosting platform and set up a webhook to receive messages from Webex Teams.

   - Test your bot by mentioning "@webexai_bot" in a Webex Teams chat room and verifying that it responds correctly.
**USER**: Continue from step 4
**ASSISTANT**: Continuing from step 4:



- It's important to note that the exact deployment steps will depend on your specific hosting platform and development environment. For example, if you're using AWS, you might need to set up an EC2 instance and configure it with the appropriate libraries and dependencies.



- In addition to the framework code provided above, you will likely need to write additional code to handle specific prompts and generate appropriate responses. This could involve integrating with external APIs, processing natural language input, or handling complex user interactions.



- Once you've tested your bot and are satisfied with its performance, you can make it available to others by adding it to a Webex Teams space or distributing the bot's username to potential users. You may also consider publishing the bot on the Webex App Hub to reach a wider audience.



- As you continue to develop and refine your bot, it's important to monitor its usage and performance over time. You may want to collect data on which prompts are most frequently used, which responses generate the most engagement, and how users are interacting with the bot overall. This information can be used to guide future development and improve the bot's effectiveness.

