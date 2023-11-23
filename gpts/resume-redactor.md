
[![Resume Redactor ](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/minimalist/mini_8.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22EN7-sbupAWnxPx0BOOuCY%22%2C%22flow%22%3Atrue%7D%7D)
# Resume Redactor  | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22EN7-sbupAWnxPx0BOOuCY%22%2C%22flow%22%3Atrue%7D%7D)
The Resume Redactor deals with the masking of sensitive personally identifiable information. The Masked information will be represented with XXX

# Prompt

```
You are specified with the Resume and your job is to act as Redactor. You need to analyze the resume and make sure to mask all the sensitive and personally identifiable information. All personally identifiable information needs to be fully masked.  Do not include any response beyond the masked resume text in XXX with the dedicated sections in JSON.

Here's the resume that you need to look for

{{ resume }}
```

## Conversation

**ASSISTANT**: {

  "name": "XXX",

  "email": "XXX",

  "phone": "XXX",

  "address": "XXX",

  "work_experience": [

    {

      "company": "Citco Fund Services (Singapore) Pte Ltd",

      "position": "Fund Accountant",

      "start_date": "Jan 2016",

      "end_date": "Present",

      "responsibilities": [

        "Calculation of estimate and final NAVs on a daily, weekly and monthly basis",

        "Preparation of cash and position reconciliation reports",

        "Daily pre-production tasks such as price checks, interest accruals and fees booking",

        "Maintaining day-to-day relationships with investment managers, brokers and auditors",

        "Communicating with the reconciliations team to ensure consistent and high-quality standards when delivering NAV packages",

        "Undertaking fund migrations from Citco Toronto and Citco Dublin Office",

        "Familiar with various pricing valuation models e.g. Independent Price Verification, External Valuer",

        "Investigation and resolution of breaks",

        "Training of new fund accountants in the team",

        "Assist in reviewing estimate and final NAV packs"

      ]

    },

    {

      "company": "Norgas Carriers Private Limited",

      "position": "Accountant",

      "start_date": "Nov 2014",

      "end_date": "Apr 2015",

      "responsibilities": [

        "Processing invoices from suppliers and scheduling payment remittances",

        "Assisted in collecting outstanding debts from debtors",

        "Involved in the year end closing of accounts",

        "Liaised with external auditors during interim and final audit",

        "Monthly bank reconciliation",

        "Perform intercompany journal entries and reconciliation"

      ]

    },

    {

      "company": "Singapore Armed Forces",

      "position": "Operation Specialist/ NSF Battery Sergeant Major (2nd Sergeant, 24th Battalion Singapore Artillery)",

      "start_date": "Jul 2013",

      "end_date": "July 2014",

      "responsibilities": [

        "In charge of the training management and administration matters, ensuring smooth running and operation of the battalion",

        "Responsible for the welfare, discipline and regimentation of 60 fellow NSFs",

        "Rallied with superiors to keep a lookout for troubled soldiers, acted as the first level of feedback for peers"

      ]

    }

  ],

  "education": [

    {

      "institution": "Royal Melbourne Institute of Technology (RMIT)",

      "degree": "Bachelor of Business (Accountancy)",

      "start_date": "Jul 2014",

      "end_date": "Oct 2015",

      "gpa": "3.1 / 4"

    },

    {

      "institution": "Temasek Polytechnic",

      "degree": "Diploma in Accounting and Finance",

      "start_date": "Apr 2009",

      "end_date": "Apr 2012",

      "gpa": null

    },

    {

      "institution": "Ngee Ann Secondary School",

      "degree": "GCE ‘O’ Levels Certificate",

      "start_date": "Jan 2005",

      "end_date": "Nov 2008",

      "gpa": null

    }

  ],

  "skills": [

    "Trained in accounting softwares, Aexeo, Agresso Business World, Sage AccPac and MYOB",

    "Proficient in Microsoft Excel, PowerPoint and Word",

    "Competent in Financial and Economic Databases (Bloomberg, Thomson Reuters)",

    "Languages spoken: English, Chinese, Cantonese",

    "Languages written: English, Chinese"

  ]

}


