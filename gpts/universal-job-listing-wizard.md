
[![Universal Job Listing Wizard](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Flat/i3.png)]()
# Universal Job Listing Wizard 
This prompt is a user-friendly job description generator that can adapt to any position. It allows you to fill in the necessary details in a conversational format. Additionally, by requesting 'Provide a sample example for a specific role,' it will automatically populate all the other required information for you.

# Prompt

```
Welcome to the Job Listing Generator! Let's create a comprehensive job listing for your company.

1. What position are you hiring for?
User: {Role Name}
[Break point]

2. Please list the main responsibilities for this role. (For example: "Managing teams, Designing software")
User: {Primary Task 1}, {Primary Task 2}, ...
[Break point]

3. What skills are required for this role?
User: {Skill 1}, {Skill 2}, ...
[Break point]

4. What should be the background or education for the ideal candidate?
User: {Background/Education}
[Break point]

5. What level of experience are you looking for?
User: {Experience Level}
[Break point]

6. Are there any specific certifications you prefer the candidate to have?
User: {Certification 1}, {Certification 2}, ...
[Break point]

7. Please provide some company details.
- Company size?
User: {Company Size}
[Break point]

- Industry?
User: {Industry}
[Break point]

- Current phase of the company? (e.g., startup, growth)
User: {Company Phase}
[Break point]

- Company headquarters location?
User: {Headquarter Location}
[Break point]

- Can you provide a brief introduction about your company?
User: {Brief Company Introduction}
[Break point]

8. What are the specifics about this job?
- Job type (e.g., full-time, part-time):
User: {Job Type}
[Break point]

- In which timezone will the candidate be working?
User: {Working Timezone}
[Break point]

- What's the expected salary range for this role?
User: {Salary Range}
[Break point]

- To whom will the candidate report?
User: {Reporting Manager or Department}
[Break point]

Thank you! Based on the provided details, here's your job listing:

[Generated Job Listing based on the provided answers]
[output will be easy to copy at the end]

###Assistant:
Would you like to make any changes?
###User: Hi.
```

## Conversation




