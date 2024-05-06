

# Resume Miner | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22LbGneKcEidB5X1DjHMAQz%22%2C%22flow%22%3Atrue%7D%7D)
The resume miner is a technology which can be utilized for extracting the meaning information out of the resume. Given the resume, it will be analyzed and provided with the structured information in JSON which can be utilized by the consumers and drive things based on the mined information.

# Prompt

```
You are tasked to perform the Resume data mining. I will provide you with the and you need to analyze and extract the key information from the resume. As a data miner, your job is to extract the content as JSON. Please include the most important or key information along with the NER and score.

{{ resume }} 
```

## Welcome Message
{

  "Name": "M R. Aneeshran Kochalunil Kunnathil",

  "Address": "Omalloor, P.O. (689647) Pathanamthitta Dist. Kerala, India",

  "Email": "aneeshrmails@gmail.com",

  "Mobile": "0919605378979",

  "Job Title": "Batching Plant Operator",

  "Date of Birth": "12 May 1985",

  "Nationality": "Indian",

  "Religion": "Christian (Orthodox)",

  "Age": "34",

  "Sex": "Male",

  "Passport No": "M9877115",

  "Marital Status": "Single",

  "Languages Known": "English, Hindi, Malayalam & Arabic",

  "Educational Qualification": [

    {

      "Year": "2001",

      "Degree": "SSLC",

      "Board": "Public Board of Examination, Kerala"

    },

    {

      "Year": "2003",

      "Degree": "+2",

      "Board": "Higher Secondary Board of Examination, Kerala, India."

    },

    {

      "Year": "2004",

      "Degree": "Industrial Training Course",

      "Trade": "Diesel Mechanic",

      "Institute": "Kerala ITC"

    }

  ],

  "Computer Skills": "Microsoft Office: Excel, Word, Access, ERP, Power point, etc.",

  "Professional Experience": [

    {

      "Duration": "2 Years",

      "Company Name": "Pink City Engineering &Trading Co.",

      "Designation": "Mechanic",

      "Nature of Work": "V6, V8, V12, Diesel Generator Mechanism & Full servicing."

    },

    {

      "Duration": "5 years",

      "Company Name": "Gulf Precast Concrete Company",

      "Designation": "Batching Plant Operator",

      "Nature of Work": "Hollow Core Concrete Mix, Precast Concrete Mix."

    },

    {

      "Duration": "1 year",

      "Company Name": "Neptune Ready Mix Concrete (R.D.C. Concrete Pvt. Ltd)",

      "Designation": "Batching Plant Operator"

    },

    {

      "Duration": "2.5 years",

      "Company Name": "Alfanar Precast Building System Company Riyadh",

      "Designation": "Batching Plant Operator",

      "Nature of Work": "(Elematic)"

    },

    {

      "Duration": "9 months",

      "Company Name": "Kef Infra Pvt Limited India",

      "Designation": "Batching Plant Operator"

    },

    {

      "Duration": "8 months",

      "Company Name": "Trevi Group Iraq (Mosul dam project)",

      "Designation": "Batching Plant Operator"

    }

  ],

  "Strengths": [

    "Hardworking",

    "Cheerful",

    "Enthusiastic",

    "Innovative",

    "Good communication skills",

    "Positive mental attitude",

    "Good listener",

    "Committed to highest level of Professionalism and excellence",

    "Matured and responsible approach to work",

    "Ability to handle multi task assignments"

  ]

}



Named Entity Recognition (NER) score:

- Location: Kerala, India - 1.0

- Email: aneeshrmails@gmail.com - 1.0

- Mobile number: 0919605378979 - 1.0

- Job Title: Batching Plant Operator - 1.0

- Education: SSLC, +2, Industrial Training Course: Diesel Mechanic - 1.0

- Company Names: Pink City Engineering & Trading Co., Gulf Precast Concrete Company, Neptune Ready Mix Concrete (R.D.C. Concrete Pvt. Ltd), Alfanar Precast Building System Company Riyadh, Kef Infra Pvt Limited India, Trevi Group Iraq - 1.0

- Computer Skills: Microsoft Office - 1.0

- Languages Known: English, Hindi, Malayalam, Arabic - 1.0

## Conversation

**ASSISTANT**: {

  "Name": "M R. Aneeshran Kochalunil Kunnathil",

  "Address": "Omalloor, P.O. (689647) Pathanamthitta Dist. Kerala, India",

  "Email": "aneeshrmails@gmail.com",

  "Mobile": "0919605378979",

  "Job Title": "Batching Plant Operator",

  "Date of Birth": "12 May 1985",

  "Nationality": "Indian",

  "Religion": "Christian (Orthodox)",

  "Age": "34",

  "Sex": "Male",

  "Passport No": "M9877115",

  "Marital Status": "Single",

  "Languages Known": "English, Hindi, Malayalam & Arabic",

  "Educational Qualification": [

    {

      "Year": "2001",

      "Degree": "SSLC",

      "Board": "Public Board of Examination, Kerala"

    },

    {

      "Year": "2003",

      "Degree": "+2",

      "Board": "Higher Secondary Board of Examination, Kerala, India."

    },

    {

      "Year": "2004",

      "Degree": "Industrial Training Course",

      "Trade": "Diesel Mechanic",

      "Institute": "Kerala ITC"

    }

  ],

  "Computer Skills": "Microsoft Office: Excel, Word, Access, ERP, Power point, etc.",

  "Professional Experience": [

    {

      "Duration": "2 Years",

      "Company Name": "Pink City Engineering &Trading Co.",

      "Designation": "Mechanic",

      "Nature of Work": "V6, V8, V12, Diesel Generator Mechanism & Full servicing."

    },

    {

      "Duration": "5 years",

      "Company Name": "Gulf Precast Concrete Company",

      "Designation": "Batching Plant Operator",

      "Nature of Work": "Hollow Core Concrete Mix, Precast Concrete Mix."

    },

    {

      "Duration": "1 year",

      "Company Name": "Neptune Ready Mix Concrete (R.D.C. Concrete Pvt. Ltd)",

      "Designation": "Batching Plant Operator"

    },

    {

      "Duration": "2.5 years",

      "Company Name": "Alfanar Precast Building System Company Riyadh",

      "Designation": "Batching Plant Operator",

      "Nature of Work": "(Elematic)"

    },

    {

      "Duration": "9 months",

      "Company Name": "Kef Infra Pvt Limited India",

      "Designation": "Batching Plant Operator"

    },

    {

      "Duration": "8 months",

      "Company Name": "Trevi Group Iraq (Mosul dam project)",

      "Designation": "Batching Plant Operator"

    }

  ],

  "Strengths": [

    "Hardworking",

    "Cheerful",

    "Enthusiastic",

    "Innovative",

    "Good communication skills",

    "Positive mental attitude",

    "Good listener",

    "Committed to highest level of Professionalism and excellence",

    "Matured and responsible approach to work",

    "Ability to handle multi task assignments"

  ]

}



Named Entity Recognition (NER) score:

- Location: Kerala, India - 1.0

- Email: aneeshrmails@gmail.com - 1.0

- Mobile number: 0919605378979 - 1.0

- Job Title: Batching Plant Operator - 1.0

- Education: SSLC, +2, Industrial Training Course: Diesel Mechanic - 1.0

- Company Names: Pink City Engineering & Trading Co., Gulf Precast Concrete Company, Neptune Ready Mix Concrete (R.D.C. Concrete Pvt. Ltd), Alfanar Precast Building System Company Riyadh, Kef Infra Pvt Limited India, Trevi Group Iraq - 1.0

- Computer Skills: Microsoft Office - 1.0

- Languages Known: English, Hindi, Malayalam, Arabic - 1.0

