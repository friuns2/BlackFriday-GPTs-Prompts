
[![Job description Parser](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/realistic/real_7.png)]()
# Job description Parser 
The Job description parser is an innovative one responsible for parsing and extracting the meaningful information.

# Prompt

```
You will be provider with the job description and you are required to analyze and parse it. Following are the mandatory requirements that you must extract from the specific job description. Provide the response in a JSON format.

Job Title
Location
Skills
Education Level Required
Occupation Classification
Hirer Contact Details
Education Accreditation
Management Level
Job Type
Certifications
Years Experience Required
Languages Required
Remuneration
Organization

{{ job-description }}
```

## Conversation

**ASSISTANT**: {

  "Job Title": "Angular Developer",

  "Location": null,

  "Skills": [

    "Angular",

    "Typescript",

    "Fullstack development",

    "CSS",

    "HTML",

    "Enterprise software development",

    "UX design",

    "GIT",

    "Stylus",

    "Less",

    "Java",

    "JavaScript",

    "Business Process Management (BPM)",

    "e2e and unit testing",

    "Kafka",

    "Mongo"

  ],

  "Education Level Required": "Bachelor's degree in Computer Science, Engineering, or any other related field, or equivalent training or work experience",

  "Occupation Classification": null,

  "Hirer Contact Details": null,

  "Education Accreditation": null,

  "Management Level": null,

  "Job Type": null,

  "Certifications": null,

  "Years Experience Required": "2+ years of experience with complex Angular applications with Typescript, 3+ years of Fullstack experience, 3+ experience in Enterprise software development",

  "Languages Required": null,

  "Remuneration": null,

  "Organization": null

}


