
[![Write any component of any size in React step-by-step](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_6.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22E7xTh1x0uTShh0fAIR_Nn%22%2C%22flow%22%3Atrue%7D%7D)
# Write any component of any size in React step-by-step | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22E7xTh1x0uTShh0fAIR_Nn%22%2C%22flow%22%3Atrue%7D%7D)
This prompt creates Pseudocode as micro prompts for chatGPT itself to replace by real code. 

All you need is to COPY/ PASTE the comments it gives in another chat and tell it to replace this with real code and it does much more effectively, preventing hallucination.

# Prompt

```
I've created a component called [component or task] you'll write detailed step-by-step micro prompts, as comments, for each block of code to be exchanged for real syntax code later:

The comments should look more or less like as follows, but with info and content related to each [component or task] and in the correct order necessary for its development:

// Briefly explain the purpose and functionality of the [component or task].
// Import libraries and other components IF necessary.
// Define the types/interface for the component IF in Typescript.
// Declare any constants or hooks holding data necessary for the functionality of the [component or task].
// Write the main logic for the [component or task], including any conditionals or loops IF necessary.
// Write any sub-functions if necessary for the main logic, including parameters and return values of the [component or task].
// Return the final JSX for the [component or task] IF there is one.
// Export the [component or task] for use in other parts of the application.

Make sure each comment is concise and serves as a short prompt for code to be added later. 

Remember, you are ONLY providing comments DO NOT write actual code in the comments, HOWEVER since you'll be dealing with logic keep in mind DRY, KISS & YAGNI principles and best practices in React.
```

## Conversation

**ASSISTANT**: // Briefly explain the purpose and functionality of the [component or task].

// This component [or task] is responsible for [brief explanation of what it does].



// Import libraries and other components IF necessary.

// Import any necessary libraries or components needed for this component [or task].



// Define the types/interface for the component IF in Typescript.

// Declare TypeScript interfaces/types for the props and/or state (if needed) of the component/task.



// Declare any constants or hooks holding data necessary for the functionality of the [component or task].

// Declare any necessary constants or hooks to hold data or function callbacks that the component/task will use.



// Write the main logic for the [component or task], including any conditionals or loops IF necessary.

// Write the main functionality of the component/task, including any necessary conditional or loop statements.



// Write any sub-functions if necessary for the main logic, including parameters and return values of the [component or task].

// Write any supporting sub-functions with their respective parameters and return values if they are necessary for the main logic.



// Return the final JSX for the [component or task] IF there is one.

// Return the final JSX that will be rendered by the component, if applicable.



// Export the [component or task] for use in other parts of the application.

// Export the component or module so that it can be used in other parts of the application.


