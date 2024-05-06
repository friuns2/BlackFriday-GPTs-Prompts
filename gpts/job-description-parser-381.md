

# Job Description Parser | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22EjClrf-genCCPy6sJ8r8-%22%2C%22flow%22%3Atrue%7D%7D)
The AI based Job Description Parser

# Prompt

```
Given the Job Description, your job is to parse and extract the information in JSON format. Please extract the info based on the following sections.

1. Job Title
2. Occupation Classification
3. Management Level
4. Years Experience Required
5. Organization
6. Location
7. Job Contact Details (Name, Phone Number)
8. Start Date
9. Job Type (e.g. Full Time, Part Time, Casual)
10. Languages Required
11. Skills 
12. Education Level Required
13. Education Accreditation
14. Certifications
15. Remuneration

{{job_description}}
```

## Welcome Message
Welcome User, Please provide the Job description to analyze and extract the information.

## Conversation

**ASSISTANT**: Here is the parsed information in JSON format:



```json

{

  "Job Title": ".NetCore Developer",

  "Occupation Classification": "Software Development",

  "Management Level": "Not specified",

  "Years Experience Required": "3-5 years",

  "Organization": "Seamgen",

  "Location": "Not specified",

  "Job Contact Details": {

    "Name": "Not specified",

    "Phone Number": "Not specified"

  },

  "Start Date": "Not specified",

  "Job Type": "Not specified",

  "Languages Required": "Javascript, Typescript",

  "Skills": "C#, .NetCore, AWS, SQL, Linq-To-SQL, Javascript, Typescript, Angular, React",

  "Education Level Required": "Bachelor’s Degree in Computer Science or Engineering",

  "Education Accreditation": "Not specified",

  "Certifications": "Not specified",

  "Remuneration": "Not specified"

}

```

