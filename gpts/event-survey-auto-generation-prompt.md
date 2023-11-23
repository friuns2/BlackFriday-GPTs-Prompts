
[![Event Survey Auto-Generation Prompt](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Minimalist/i18.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22gqYRMIqE1iEebMFmEyo-3%22%2C%22flow%22%3Atrue%7D%7D)
# Event Survey Auto-Generation Prompt | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22gqYRMIqE1iEebMFmEyo-3%22%2C%22flow%22%3Atrue%7D%7D)
This prompt generates GAS code that automatically creates an event feedback form.

# Prompt

```
Premise
Using Google Apps Script (GAS) to create an event feedback form. The goal is for users to utilize this prompt to easily customize the feedback form for actual events.

Content Details
A GAS script is provided to dynamically generate a Google Forms survey.

Variable Definitions and Goal Setting
Event Title
Event Date
Event Description
These variables are used to customize the form based on user input.

Execution Process
Open the GAS script editor and paste the following script.
Run the promptUserForFormDetails function.
Follow the prompt and enter the required information.
GAS will dynamically generate the Google Form.
User Confirmation
Obtain from the user: Event Title, Event Date, and Event Description.
Ensure you have the necessary permissions when executing the script in the GAS script editor. Confirm that you have permission to Google Drive.
Exception Handling
If the user cancels the input prompt, the script will abort form creation.

Feedback Loop
The generated form's URL will be displayed in the GAS script editor's Logger. This allows users to check the content of the form and edit manually if necessary.

Deliverable
Below is the GAS script to dynamically generate an event feedback form based on user input:

javascript
Copy code
function promptUserForFormDetails() {
  var ui = SpreadsheetApp.getUi();
  
  // Prompt for event title
  var titleResponse = ui.prompt('Enter the Event Title', 'e.g., Web Design Workshop', ui.ButtonSet.OK_CANCEL);
  
  if (titleResponse.getSelectedButton() == ui.Button.OK) {
    // Prompt for event date
    var dateResponse = ui.prompt('Enter the Event Date', 'e.g., October 1, 2023', ui.ButtonSet.OK_CANCEL);

    if (dateResponse.getSelectedButton() == ui.Button.OK) {
      // Prompt for event description
      var descriptionResponse = ui.prompt('Enter the Event Description', 'e.g., In this workshop, we will...', ui.ButtonSet.OK_CANCEL);
      
      if (descriptionResponse.getSelectedButton() == ui.Button.OK) {
        // Create the form
        createCustomForm(titleResponse.getResponseText(), dateResponse.getResponseText(), descriptionResponse.getResponseText());
      }
    }
  }
}

function createCustomForm(title, date, description) {
  var form = FormApp.create(title + " (" + date + ")");
  
  // Add event description
  form.addSectionHeaderItem()
      .setTitle(description);
  
  // Add other form items here. For example:
  form.addMultipleChoiceItem()
      .setTitle('Did you find the event useful?')
      .setChoiceValues(['Extremely useful', 'Very useful', 'Somewhat useful', 'Not very useful', 'Not at all useful']);
  
  form.addParagraphTextItem()
      .setTitle('Please provide any specific feedback or comments');
  
  Logger.log('Form created! Edit URL: ' + form.getEditUrl());
}

User:Hello
```

## Conversation




