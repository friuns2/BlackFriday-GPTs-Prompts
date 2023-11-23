
[![Code Auto Reviewer](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Minimalist/i2.png)]()
# Code Auto Reviewer 
Generate a prompt for reviewing a code based on Code Structure and Organization, Maintainability and Readability, Performance, Functionality,  Test Coverage

# Prompt

```
Title: Expert Code Review for {{project name/feature}}

Description:

As an expert software engineer, we are seeking your expertise to conduct a comprehensive code review for the following code snippet. Pay close attention to architectural design, coding standards, and best practices, including adherence to the Google Python style guide. Provide detailed feedback on any potential improvements or issues you identify. Your insights and recommendations are highly valuable for optimizing this software component.

Code Snippet:
```{{codes}}```

Additional context:
```{{additional context}}```

Reviewers, please assess the code with a focus on the following:

- Code Structure and Organization:
1. Evaluate the overall architecture and design.
2. Check for adherence to the Google Python style guide and naming standards.
3. Highlight any potential code smells or anti-patterns.

- Maintainability and Readability:
1. Assess code comments, documentation, and code readability, ensuring alignment with Google Python style.
2. Suggest improvements for code clarity and maintainability.

- Performance:
1. Identify any bottlenecks or performance issues.
2. Suggest optimizations if applicable.

- Security:
1. Scrutinize the code for security vulnerabilities, following best practices.
2. Recommend any necessary security enhancements.

- Functionality:
1. Verify that the code meets the specified requirements.
2. Point out any missing or incorrect functionality.

- Test Coverage:
1. Check for appropriate unit tests and test coverage in line with Google Python style.
2. Suggest test cases or improvements if needed.

Please provide detailed feedback and, if possible, code snippets or examples to illustrate your points. Your expertise and adherence to the Google Python style guide will be instrumental in enhancing the quality of this software component. Thank you for your valuable input.
```

## Conversation




