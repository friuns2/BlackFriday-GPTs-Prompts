
[![response chunking](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_2.png)]()
# response chunking 
lets make a prompt to break up responses into smaller "chunks"

i am going to treat it like a set if rules for chatGPT to use after initial input/prompt





token_threshold  = 2000

user_query_token_count = nil

response_token_count = nil

response_chunk_total = nil

response_current_chunk = nil



estimate tokens from user input and place in variable "user_query_token_count " (include initial prompt)

then estimate tokens needed for full response and place in variable "response_token_count "

if the response_token_count is over token_threshold then break full response into smaller "chunks" about the same token count as token_threshold  give or take 100 tokens then post 

in bold font token_threshold , user_query_token_count , response_token_count , response_chunk_total and response_current_chunk  then post the first "chunk" and ait for user to respond with "ok" to move on to the next "chunk"

# Prompt

```
lets make a prompt to break up responses into smaller "chunks"
i am going to treat it like a set if rules for chatGPT to use after initial input/prompt


token_threshold  = 2000
user_query_token_count = nil
response_token_count = nil
response_chunk_total = nil
response_current_chunk = nil

estimate tokens from user input and place in variable "user_query_token_count " (include initial prompt)
then estimate tokens needed for full response and place in variable "response_token_count "
if the response_token_count is over token_threshold then break full response into smaller "chunks" about the same token count as token_threshold  give or take 100 tokens then post 
in bold font token_threshold , user_query_token_count , response_token_count , response_chunk_total and response_current_chunk  then post the first "chunk" and ait for user to respond with "ok" to move on to the next "chunk"
```

## Conversation

**ASSISTANT**: Understood. To summarize, after receiving a user prompt, I will estimate the number of tokens in the prompt and set it as "user_query_token_count". Then, I will estimate the number of tokens needed for the full response and set it as "response_token_count". If "response_token_count" is over "token_threshold", I will break the full response into smaller "chunks" with a similar token count to "token_threshold", and post each chunk one at a time in bold font along with the current values of "token_threshold", "user_query_token_count", "response_token_count", "response_chunk_total", and "response_current_chunk". I will wait for the user to respond with "ok" before moving on to the next chunk.


