
[![PII Detector](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/realistic/real_7.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%225vTkikwg4IxFQ-lIymc0M%22%2C%22flow%22%3Atrue%7D%7D)
# PII Detector | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%225vTkikwg4IxFQ-lIymc0M%22%2C%22flow%22%3Atrue%7D%7D)
Personally Identifiable Information Detector. A super useful app which will analyze and let you know all the PII information.

# Prompt

```
You will be specified with the content which consists of the personally identifiable information and personal health information. Your job is to classify the PII and PHI information and produce the response in JSON format.

{{ content }}
```

## Conversation

**ASSISTANT**: {

  "PII": [

    {

      "Name": "David Johnson",

      "Social Security Number": "123-45-6789",

      "Medicare Number": "12349082673",

      "Address": "Maine",

      "Credit Card Number": "4095-2609-9393-4932",

      "Passport Number": "191280342",

      "Phone Number": "(212) 555-1234"

    },

    {

      "Name": "Kate",

      "Social Security Number": "078-05-1126",

      "Driver License Number": "1234567A"

    }

  ],

  "PHI": [],

  "Other Information": [

    {

      "Crypto Wallet ID": "16Yeky6GMjeNkAiNcBY7ZhrLoMSgg1BoyZ",

      "Visited Website": "microsoft.com",

      "Email Address": "test@presidio.site",

      "IP Address": "192.168.0.1",

      "International Bank Account Number": "IL150120690000003111111",

      "Bank Account Number": "954567876544"

    }

  ]

}


