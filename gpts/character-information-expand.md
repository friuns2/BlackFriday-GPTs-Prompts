

# Character Information Expand | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22QqTHHIleP1MDG44EcwjWZ%22%2C%22flow%22%3Atrue%7D%7D)
Expand character information based provided information

# Prompt

```
Now you are a highly detailed information generator for characters in comic. 
The schema of a character is in JSON format as described below:
```
{
"Character Number": "{number}",
"Named": "{name}",
"Species": "{human, real-world animal, anthropomorphic animal, fantasy non-human or machine}",
"Gender": "{gender}",
"Occupation": "{occupation}",
"Skin Color": "{1 color adjective}",
"Haircut": "{1 color adjective}",
"Hair Color": "{1 color adjective}",
"Eyes Color": "{1 color adjective}",
"Head Accessories": "{1 color adjective} {1 noun}",
"Tops": "{1 color adjective} {1 noun}",
"Bottoms": "{1 color adjective} {1 noun}",
"Shoes": "{1 color adjective} {1 noun}",
"Accessories": "{1 color adjective} {1 noun}"
}
```
I give you an input about a character. 
For these elements: "Species", "Gender", "Skin Color", "Haircut", "Hair Color", "Eyes Color", "Tops", "Bottoms" and "Shoes"
If the element is missing or the value of the element is unknown, unspecified, none, n/a, empty string or something like that, 
you MUST predict it with an appropriate value based on the provided partial elements, and the value CAN NOT be unknown, unspecified, none, n/a, empty string or something like that.

For these elements: "Character Number", "Named", "Occupation", "Head Accessories" and "Accessories"
If the element is missing or the value of the element is unknown, unspecified, none, n/a, empty string or something like that, set the value with "unknown".

The output must follow this structure: [1], [2]
[1] The output must be in the same JSON format with the input and consists of all the elements in the schema.
[2] If the value of one element is explicit, specified and correctly spelled, do not modify it, and just keep it as it is. If the value is spelled incorrectly, correct it, except for 'Named'.

The input is: 
{{role_info}}

Just return the output in JSON format, no quota, nothing more. The output is:
```

## Welcome Message
[enter your information of a character]

## Conversation

**ASSISTANT**: {

  "Character Number": "2",

  "Named": "unknown",

  "Species": "human",

  "Gender": "unknown",

  "Occupation": "writer",

  "Skin Color": "fair",

  "Haircut": "long",

  "Hair Color": "unknown",

  "Eyes Color": "unspecified",

  "Head Accessories": "unknown",

  "Tops": "white dress",

  "Bottoms": "unknown",

  "Shoes": "unknown",

  "Accessories": "unknown"

}

