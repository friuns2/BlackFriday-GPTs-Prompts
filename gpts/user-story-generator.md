
[![User Story Generator](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/futuristic/futu_9.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22P5ks4eimpP6WVPZSUEX1s%22%2C%22flow%22%3Atrue%7D%7D)
# User Story Generator | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22P5ks4eimpP6WVPZSUEX1s%22%2C%22flow%22%3Atrue%7D%7D)
Prompt a complete output of user story scenarios, acceptance conditions, test cases



# Prompt

```
You are an expert in Agile methodology and your task is to elaborate a user story in detail, which includes: 

- Step 1: Enhance the description of the user story.
- Step 2: Thoroughly describe between three to five scenarios where the user story may occur, - encompassing both positive and negative cases.
- Step 3: Based on the user scenarios designed in Step 2, formulate 10 to 20 acceptance criteria.
- Step 4: Derive test cases from the acceptance criteria created in Step 3, set their priorities (high/medium/low), and define the expected outcomes.
- Stay consistent with the format I have requested, explanations are not necessary.

Here's a user story for your consideration: The user story is -"{{story}}".

Please use the following format to structure the output:
"""
### User Story: 

### Scenarios: 

Detail: 

Positive Aspects:

- ...
...

Negative Aspects:

- ...
...

### Acceptance Criteria: 

- ...
...

### Test cases:

- [Priority] ...
...
"""
```

## Conversation

**ASSISTANT**: ### User Story: 



As a user, I want to be able to register and log in using my mobile phone number so that I can access the application easily without the need for a separate username and password.



### Scenarios: 



Detail: 



Positive Aspects:



- The user enters a valid mobile phone number and receives a verification code to complete the registration process successfully.

- The user logs in using the registered mobile phone number and the correct verification code, gaining access to their account.

- The user can reset their password using their registered mobile phone number.



Negative Aspects:



- The user enters an invalid mobile phone number and receives an error message, preventing them from continuing with the registration process.

- The user enters an incorrect verification code during the login process and is denied access to their account.

- The user tries to reset their password without providing a registered mobile phone number and receives an error message.



### Acceptance Criteria: 



- The user should be able to register using a valid mobile phone number and receive a verification code.

- The user should be able to log in using the registered mobile phone number and the correct verification code.

- The user should be able to reset their password using their registered mobile phone number.

- The system should reject an invalid mobile phone number during the registration process.

- The system should reject an incorrect verification code during the login process.

- The system should reject a password reset request without a registered mobile phone number.



### Test cases:



- [High] User enters a valid mobile phone number and receives a verification code.

- [High] User enters the correct verification code and successfully logs in.

- [High] User enters a registered mobile phone number and successfully resets their password.

- [Medium] User enters an invalid mobile phone number and receives an error message during registration.

- [Medium] User enters an incorrect verification code and is denied login access.

- [Medium] User tries to reset their password without providing a registered mobile phone number and receives an error message.

- [Low] User tries to register without providing a mobile phone number and receives an error message.

- [Low] User tries to log in without providing a mobile phone number and receives an error message.

- [Low] User tries to reset their password without providing a mobile phone number and receives an error message.

- [Low] User enters an incorrect verification code multiple times and gets locked out of their account.


