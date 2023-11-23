
[![Resume Prompt Generator](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/realistic/real_1.png)]()
# Resume Prompt Generator 
A super helpful resume prompt generator that will help you in enhancing your prompt skills and utilize the resume prompt generator for building an awesome resume.

# Prompt

```
Consider the sections Personal, Summary or Objective, Experience,  Education, Certifications, Skills, Awards & Accomplishments, Hobbies, Extracurricular Activities & Projects, Voluntary Work, Languages and generate prompts in JSON format. For this task, you need to consider yourself as a prompt engineer and help the people in building or generating the promotes they ask for based on the specified topics.

{{ topic }}
```

## Conversation

**ASSISTANT**: Here are some prompts in JSON format for each section of an ATS-friendly resume:



Personal:

```

{

    "prompt": "What is your full name?",

    "type": "text"

},

{

    "prompt": "What is your current location?",

    "type": "text"

},

{

    "prompt": "What is your email address?",

    "type": "email"

},

{

    "prompt": "What is your phone number?",

    "type": "tel"

}

```



Summary or Objective:

```

{

    "prompt": "What is your career objective or summary?",

    "type": "textarea"

}

```



Experience:

```

{

    "prompt": "What is your most recent work experience?",

    "type": "textarea"

},

{

    "prompt": "What are your specific responsibilities and achievements in this role?",

    "type": "textarea"

}

```



Education:

```

{

    "prompt": "What is your highest degree achieved?",

    "type": "text"

},

{

    "prompt": "What is the name of the institution you attended?",

    "type": "text"

},

{

    "prompt": "What was your field of study?",

    "type": "text"

},

{

    "prompt": "What was your graduation date?",

    "type": "date"

}

```



Certifications:

```

{

    "prompt": "What certifications do you possess?",

    "type": "textarea"

}

```



Skills:

```

{

    "prompt": "What technical skills do you have?",

    "type": "textarea"

},

{

    "prompt": "What soft skills do you possess?",

    "type": "textarea"

}

```



Awards & Accomplishments:

```

{

    "prompt": "Have you received any awards or recognition?",

    "type": "textarea"

}

```



Hobbies:

```

{

    "prompt": "What are your hobbies or interests?",

    "type": "textarea"

}

```



Extracurricular Activities & Projects:

```

{

    "prompt": "What extracurricular activities have you participated in?",

    "type": "textarea"

},

{

    "prompt": "Have you completed any personal projects? If so, please describe them.",

    "type": "textarea"

}

```



Voluntary Work:

```

{

    "prompt": "Have you done any volunteer work? If so, please describe your experience.",

    "type": "textarea"

}

```



Languages:

```

{

    "prompt": "What languages are you proficient in?",

    "type": "textarea"

}

```


