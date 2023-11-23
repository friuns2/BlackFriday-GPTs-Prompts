
[![JSON Resume Builder](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/realistic/real_7.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22hDk7IiXgDzmJptbslWJhr%22%2C%22flow%22%3Atrue%7D%7D)
# JSON Resume Builder | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22hDk7IiXgDzmJptbslWJhr%22%2C%22flow%22%3Atrue%7D%7D)
Provided with the unstructured resume, the job of the JSON resume builder is to analyze and then build the JSON resume specification based resume

# Prompt

```
You are now considered as a Resume Parsing Expert. classify the resume line by line with the following sections and provide the structured information in JSON resume schema.

Please do not output your own responses.

{{ resume }}
```

## Conversation

**ASSISTANT**: {

    "basics": {

        "name": "SUBASH J",

        "email": "jsubash1209@gmail.com",

        "phone": "+91-9994836515",

        "location": {

            "city": "Chennai",

            "countryCode": "IN"

        }

    },

    "objective": {

        "summary": "To acquire a position that utilizes my software development and project analysis in the contribution to the overall productivity of the organization."

    },

    "work": [{

            "position": ".Net programmer trainee",

            "company": "Ewall Solutions Pvt Ltd",

            "startDate": "2017-02-01",

            "endDate": "2018-05-31",

            "summary": "",

            "website": "https://www.ewallsolutions.com/",

            "location": {

                "city": "Chennai",

                "countryCode": "IN"

            }

        },

        {

            "position": ".Net software developer",

            "company": "Softura Pvt Ltd",

            "startDate": "2018-07-01",

            "endDate": "2021-03-31",

            "summary": "",

            "website": "https://www.softura.com/",

            "location": {

                "city": "Chennai",

                "countryCode": "IN"

            }

        },

        {

            "position": "Senior Engineer",

            "company": "HTC Global Services",

            "startDate": "2021-03-01",

            "endDate": null,

            "summary": "",

            "website": "https://www.htcinc.com/",

            "location": {

                "city": "Chennai",

                "countryCode": "IN"

            }

        }

    ],

    "education": [{

            "institution": "Karpagam Institute of Technology",

            "area": "Electronics & Communication Engineering",

            "studyType": "Bachelor",

            "startDate": "2012-06-01",

            "endDate": "2016-05-31",

            "gpa": "63%",

            "location": {

                "city": "Coimbatore",

                "countryCode": "IN"

            }

        },

        {

            "institution": "Malar Matric Higher Secondary School",

            "area": "",

            "studyType": "HSC",

            "startDate": "2010-06-01",

            "endDate": "2012-05-31",

            "gpa": "84%",

            "location": {

                "city": "P.Velur",

                "countryCode": "IN"

            }

        },

        {

            "institution": "Government High Secondary School",

            "area": "",

            "studyType": "SSLC",

            "startDate": "2008-06-01",

            "endDate": "2010-05-31",

            "gpa": "82%",

            "location": {

                "city": "P.Velur",

                "countryCode": "IN"

            }

        }

    ],

    "skills": [{

            "name": "C#.net",

            "level": ""

        },

        {

            "name": "VB.net",

            "level": ""

        },

        {

            "name": "HTML5",

            "level": ""

        },

        {

            "name": "LINQ",

            "level": ""

        },

        {

            "name": "SQL Asp.net",

            "level": ""

        },

        {

            "name": "Asp.net Core MVC",

            "level": ""

        },

        {

            "name": "Entity Framework",

            "level": ""

        },

        {

            "name": "ADO.NET",

            "level": ""

        },

        {

            "name": "AJAX",

            "level": ""

        },

        {

            "name": "IIS",

            "level": ""

        },

        {

            "name": "SSIS",

            "level": ""

        },

        {

            "name": "WEB services",

            "level": ""

        },

        {

            "name": "Microsoft Azure",

            "level": ""

        },

        {

            "name": "SSRS",

            "level": ""

        },

        {

            "name": "PGP",

            "level": ""

        },

        {

            "name": "GPG",

            "level": ""

        },

        {

            "name": "JavaScript",

            "level": ""

        },

        {

            "name": "JQuery",

            "level": ""

        },

        {

            "name": "Tekton CI/CD",

            "level": ""

        },

        {

            "name": "GCP Cloud Database",

            "level": ""

        },

        {

            "name": "MS SQL SERVER",




