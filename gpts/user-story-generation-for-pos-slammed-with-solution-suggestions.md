
[![User Story Generation for POs Slammed with Solution Suggestions](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/illustrative/illus_1.png)]()
# User Story Generation for POs Slammed with Solution Suggestions 
As a product owner or product manager, capturing incoming concepts, solutions, and requests in consistent, shareable language is important. Doing so in our busy day-to-day lives is nearly impossible. That's where ChatGPT can help us by taking incoming flood ideas from HiPPOs, RHiNOs, and Seagull Managers and quickly and easily leveraging these 6 techniques:



1. Sets the stage in the CONTEXT block by describing the task and anticipated result.

2. Provides multiple feature request examples to enrich the model's understanding.

3. Uses Markdown to organize sections and highlight key elements.

4. Uses form brackets to specify placeholders where the model should provide specific information.

5. Choose language, tone, and style that reflect the PM's role and align with Agile product development

6. Use the QUESTION block to keep the model focused on the primary task.



Feedback is welcome, as I'm sure it can be improved.

# Prompt

```
{CONTEXT}
# Formatting Feature Requests as User Stories using ChatGPT

## Incoming Feature Requests
1. Feature request from a Solution-Seeking Seagull Manager on Slack:
   _"I have a problem. I'm allergic to gluten, and I love pizza. When I go into your app, I have no clue which pizzas I can eat. I need a big button or something that says 'GLUTEN-FREE PIZZAS' right when I open the app. And when I click it, the app should just show me all the gluten-free pizzas that I can order. I don't want to see anything else. Can you make that happen?"_
2. Feature request from an Output-Obsessed HiPPO executive via Outlook:
  _ "We need a feature in the app that immediately notifies the user about the progress of their pizza delivery. As soon as a pizza order is placed, the app should give them a detailed timeline showing when the pizza is being prepared, when it's being baked, when it's ready for delivery, and the exact minute it should arrive at their doorstep. This should be visible every time they open the app. I want numbers and graphs - let's quantify this experience."_

## User Story Format Template

Template Instructions: The following template format combines the Mike Cohn User Story Format augmented by a Gherkin-style acceptance criterion. Be generous with the GIVEN preconditions (2 at minimum), but only include a single WHEN and THEN in the acceptance criteria. Adhere to the Markdown formatting.


### User Story [User Story Number ID]:

*   **Summary**: [concise, memorable, human-readable story title]
*   **Story**: 
   **As a** [user type], 
   **I want to** [action], 
   **so that** [outcome]


### Acceptance Criteria:

*   **Scenario**: [concise, human-readable user scenario]
*   **Given**: [Initial context]
*   **and Given**: [Additional Given context]
*   **and Given** [additional Given context statements as needed]
*   **When**: [Event occurs]
*   **Then**: [Expected outcome]

{QUESTION}
Rewrite the 'Incoming Feature Requests' using the 'User Story Format.'

```

## Conversation

**ASSISTANT**: User Story 1:



**Summary**: Gluten-Free Pizzas Button



**Story**: 

As a Solution-Seeking Seagull Manager, 

I want a big button that says 'GLUTEN-FREE PIZZAS' when I open the app, 

so that I can easily see all the gluten-free pizzas that I can order.



**Acceptance Criteria**:



*   **Scenario**: Finding gluten-free pizzas

*   **Given**: I am a Solution-Seeking Seagull Manager

*   **and Given**: I have opened the app

*   **When**: I click on the 'GLUTEN-FREE PIZZAS' button

*   **Then**: The app should display only the gluten-free pizzas that I can order



User Story 2:



**Summary**: Pizza Delivery Progress Notification



**Story**: 

As an Output-Obsessed HiPPO executive, 

I want the app to immediately notify the user about the progress of their pizza delivery, 

so that they can track the entire process in detail.



**Acceptance Criteria**:



*   **Scenario**: Tracking pizza delivery progress

*   **Given**: I am an Output-Obsessed HiPPO executive

*   **and Given**: A pizza order has been placed

*   **When**: I open the app

*   **Then**: The app should display a detailed timeline showing the various stages of pizza preparation, baking, and delivery, along with the exact minute the pizza should arrive at the user's doorstep. The timeline should include numbers and graphs to quantify the delivery experience.


