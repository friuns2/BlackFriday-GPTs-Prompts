
[![Skill Extractor](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/futuristic/futu_1.png)]()
# Skill Extractor 
A super helpful skill extractor that is primarily used for the extraction of the candidate's resume skills with the score. 

# Prompt

```
Extract the skills with score from the specified resume in JSON format. Do not include any response other than the JSON format.

{{ resume }}
```

## Conversation

**ASSISTANT**: {

  "Skills": {

    "FHIR": 1,

    "Rest API": 1,

    "Java": 1,

    "Git": 1,

    "Linux": 2,

    "Agile Methodologies": 1,

    "CCDA": 1,

    "BCDA": 1,

    "Mirth": 3,

    "Javascript": 1,

    "React": 1,

    "Groovy": 2,

    "Spring": 3,

    "MongoDB": 3,

    "SQL": 1,

    "JUnit": 1,

    "Oauth2": 1,

    "PACS": 2,

    "Python": 2,

    "HL7": 2,

    "Microservices": 1,

    "Jenkins": 1

  }

}


