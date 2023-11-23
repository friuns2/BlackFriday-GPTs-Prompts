
[![Unstructured Data Processor](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_3.png)]()
# Unstructured Data Processor 
The unstructured data processor deals with the processing of the highly unstructured data in textual format to produce the meaningful structured information in JSON.

# Prompt

```
You will be provided with the highly unstructured textual data and your task is to be an expert analyst in understanding the context or business that is being dealt and produce the structured information in JSON. Also make sure to embed the sentiments or emotions along with the NER.

{{ content }}
```

## Conversation

**ASSISTANT**: {

  "customer": {

    "message": "Hi, I’m waiting for my delivery. It was supposed to have arrived three days ago. Can you give me an update?",

    "order_reference_number": "1234567",

    "sentiment": "Negative",

    "ner": [

      {

        "entity": "Delivery",

        "type": "Product"

      },

      {

        "entity": "Three days",

        "type": "Time"

      }

    ]

  },

  "advisor": {

    "message": "Thanks for getting in touch with us. I am sorry for any inconvenience this may have caused. What is your order reference number?",

    "sentiment": "Positive"

  },

  "system": {

    "message": "According to the system that order will be delivered today between 3-5pm.",

    "sentiment": "Neutral",

    "delivery_time": {

      "start": "3pm",

      "end": "5pm"

    }

  },

  "customer": {

    "message": "That’s annoying because I’m out then and how do I know that it will actually arrive.",

    "sentiment": "Negative"

  },

  "advisor": {

    "message": "I am sorry that you feel that way. I will phone the driver to double check and maybe we can leave it with a neighbour. Would that be okay?",

    "sentiment": "Negative",

    "action": "Contacted driver to double-check delivery status and asked if delivery can be left with a neighbor."

  },

  "customer": {

    "message": "Okay, thanks.",

    "sentiment": "Positive"

  }

}


