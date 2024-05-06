

# Resume Parser | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22sRWs1OtC-xbO9S9lXxW2c%22%2C%22flow%22%3Atrue%7D%7D)
Input the extracted raw text of resume and the structured JSON will be returned. It covered 'personal information', 'educational information', and 'skill'.

# Prompt

```
You are now considered as a Resume Parsing Expert. Summarize the resume and provide the structured information with the following resume sections in a highly structured JSON format. Education and Skill section could have more than one item. Normalise the skill title to standardise form. Do not include the comments in the output.  The output should only contain personal info, education info, and skill info. please format them in easy-to-read. 

{
    "personal": {
        "name": "",  //str
        "email": [""],  //List of str (May contains more than one emails)
        "contact_number": [""],  //List of str
        "address": [""],  //List of address
        "nationality": "",  //str (follow the country code of "contact number" or guess from "address", it should be standardise format such as 'Malaysia', 'Indonesia', etc)
        "url": [""]  //List of str (May contains more than one url, put all urls here)
},
    "education": [{   
            "school": "",  //str
            "degree": "",  //str (programme name)
            "qualification": "",  //str (derive level of education from "degree",  it should be standardised format such as 'Undergraduate', 'Postgraduate', 'Pre-U', 'Diploma', etc, , please categorise yourself)
            "major": "",  //str
            "minor": "", //str
            "start_date": "",  //str (YYYY-MM-DD)
            "end_date": "",  //str (YYYY-MM-DD)
            "year_of_study": "",  //str
            "grade": "", //str (it is type of score such as cgpa,spm, etc)
            "score": ""  //str (it is the score such as 3.1/4.0, 9A+)
}, ...],  "skill": [{"title": "", "type": "" //either hard or soft skill, please categorise yourself, it should be either "hard" or "soft"
,},...]}

{{ resume }}
```

## Welcome Message
{

    "personal": {

        "name": "Teoh Sin Yee",

        "email": ["teohsinyee.cs@gmail.com"],

        "contact_number": ["+6011-20132175"],

        "address": ["Perak"],

        "nationality": "Malaysia",

        "url": [

            "www.linkedin.com/in/teohsinyee",

            "https://bit.ly/regexpaper",

            "https://bit.ly/SolrSearchEnginePaper",

            "https://bit.ly/guide_2ndary_sch_v2"

        ]

    },

    "education": [

        {

            "school": "Universiti Sains Malaysia",

            "degree": "Bachelor of Computer Sciences (Hons.)",

            "qualification": "Undergraduate",

            "major": "Intelligent Computing (Data Analytics)",

            "minor": "Management",

            "start_date": "2019-09-01",

            "end_date": "2023-08-31",

            "year_of_study": "",

            "grade": "CGPA",

            "score": "3.46/4.00"

        },

        {

            "school": "Penang Matriculation College",

            "degree": "Foundation in Sciences",

            "qualification": "Pre-U",

            "major": "",

            "minor": "",

            "start_date": "2018-05-01",

            "end_date": "2019-03-31",

            "year_of_study": "",

            "grade": "CGPA",

            "score": "3.96/4.00"

        }

    ],

    "skill": [

        {

            "title": "Artificial Intelligence",

            "type": "hard"

        },

        {

            "title": "Natural Language Processing",

            "type": "hard"

        },

        {

            "title": "Deep Learning",

            "type": "hard"

        },

        {

            "title": "Machine Learning App Development",

            "type": "hard"

        },

        {

            "title": "Python",

            "type": "hard"

        },

        {

            "title": "Flask",

            "type": "hard"

        },

        {

            "title": "Django App Development",

            "type": "hard"

        },

        {

            "title": "MySQL",

            "type": "hard"

        },

        {

            "title": "JavaScript",

            "type": "hard"

        },

        {

            "title": "Solr",

            "type": "hard"

        }

    ]

}

## Conversation

**ASSISTANT**: {

    "personal": {

        "name": "Teoh Sin Yee",

        "email": ["teohsinyee.cs@gmail.com"],

        "contact_number": ["+6011-20132175"],

        "address": ["Perak"],

        "nationality": "Malaysia",

        "url": [

            "www.linkedin.com/in/teohsinyee",

            "https://bit.ly/regexpaper",

            "https://bit.ly/SolrSearchEnginePaper",

            "https://bit.ly/guide_2ndary_sch_v2"

        ]

    },

    "education": [

        {

            "school": "Universiti Sains Malaysia",

            "degree": "Bachelor of Computer Sciences (Hons.)",

            "qualification": "Undergraduate",

            "major": "Intelligent Computing (Data Analytics)",

            "minor": "Management",

            "start_date": "2019-09-01",

            "end_date": "2023-08-31",

            "year_of_study": "",

            "grade": "CGPA",

            "score": "3.46/4.00"

        },

        {

            "school": "Penang Matriculation College",

            "degree": "Foundation in Sciences",

            "qualification": "Pre-U",

            "major": "",

            "minor": "",

            "start_date": "2018-05-01",

            "end_date": "2019-03-31",

            "year_of_study": "",

            "grade": "CGPA",

            "score": "3.96/4.00"

        }

    ],

    "skill": [

        {

            "title": "Artificial Intelligence",

            "type": "hard"

        },

        {

            "title": "Natural Language Processing",

            "type": "hard"

        },

        {

            "title": "Deep Learning",

            "type": "hard"

        },

        {

            "title": "Machine Learning App Development",

            "type": "hard"

        },

        {

            "title": "Python",

            "type": "hard"

        },

        {

            "title": "Flask",

            "type": "hard"

        },

        {

            "title": "Django App Development",

            "type": "hard"

        },

        {

            "title": "MySQL",

            "type": "hard"

        },

        {

            "title": "JavaScript",

            "type": "hard"

        },

        {

            "title": "Solr",

            "type": "hard"

        }

    ]

}

