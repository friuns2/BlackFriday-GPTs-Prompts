

# SchemaGPT for app structure planning [GPT-4] | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22y_CAdOcNNWjvuqecmvkui%22%2C%22flow%22%3Atrue%7D%7D)
The idea of this prompt is to build a swagger-like schema. It can be used on development early stages to get an example structure of app.

The prompt can be modified to include more info for each endpoint.



GPT-4 response is much better and does the job. GPT-3.5 is quite inaccurate.



Try other prompt for GPT-4 model:

```

Act as swagger-like application. Build structure for a web app based on business logic input.

Schema:

{METHOD} {PATH}

Auth: {IS AUTH REQUIRED}

Headers: {UNIQUE HEADERS}

Body: {BODY IF METHOD SUPPORTS}

Description: {DESCRIPTION}



Input: API for a Facebook-like app

```

# Prompt

```
I'd like you to assist in building a schema for a web app based on the business logic input.\nSchema:\n{METHOD} {PATH}\nAuth: {IS AUTH REQUIRED}\nHeaders: {UNIQUE HEADERS}\nBody: {BODY IF METHOD SUPPORTS}\nDescription: {DESCRIPTION}\n\nInput: api for messaging app
```

## Welcome Message
Sure, here's an example schema for a messaging app API:



Schema:

POST /messages

Auth: Required

Headers:

- Authorization: Bearer {access_token}

- Content-Type: application/json

Body:

- recipient_id: string

- message_text: string

Description: Send a new message to a user identified by recipient_id.



GET /conversations

Auth: Required

Headers:

- Authorization: Bearer {access_token}

Body: N/A

Description: Get a list of conversations for the authenticated user.



GET /conversations/{conversation_id}/messages

Auth: Required

Headers:

- Authorization: Bearer {access_token}

Body: N/A

Description: Get all messages for a specific conversation.



PUT /conversations/{conversation_id}/messages/{message_id}

Auth: Required

Headers:

- Authorization: Bearer {access_token}

- Content-Type: application/json

Body:

- message_text: string

Description: Update an existing message in a specific conversation.



DELETE /conversations/{conversation_id}/messages/{message_id}

Auth: Required

Headers:

- Authorization: Bearer {access_token}

Body: N/A

Description: Delete an existing message in a specific conversation.



Note that this is just an example schema and should be adapted to fit your specific requirements. Additionally, you will need to implement appropriate authentication mechanisms and obtain any necessary permissions and credentials from your messaging service provider.

## Conversation

**ASSISTANT**: Sure, here's an example schema for a messaging app API:



Schema:

POST /messages

Auth: Required

Headers:

- Authorization: Bearer {access_token}

- Content-Type: application/json

Body:

- recipient_id: string

- message_text: string

Description: Send a new message to a user identified by recipient_id.



GET /conversations

Auth: Required

Headers:

- Authorization: Bearer {access_token}

Body: N/A

Description: Get a list of conversations for the authenticated user.



GET /conversations/{conversation_id}/messages

Auth: Required

Headers:

- Authorization: Bearer {access_token}

Body: N/A

Description: Get all messages for a specific conversation.



PUT /conversations/{conversation_id}/messages/{message_id}

Auth: Required

Headers:

- Authorization: Bearer {access_token}

- Content-Type: application/json

Body:

- message_text: string

Description: Update an existing message in a specific conversation.



DELETE /conversations/{conversation_id}/messages/{message_id}

Auth: Required

Headers:

- Authorization: Bearer {access_token}

Body: N/A

Description: Delete an existing message in a specific conversation.



Note that this is just an example schema and should be adapted to fit your specific requirements. Additionally, you will need to implement appropriate authentication mechanisms and obtain any necessary permissions and credentials from your messaging service provider.

