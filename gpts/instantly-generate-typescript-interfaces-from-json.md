
[![Instantly generate TypeScript interfaces from JSON](https://flow-user-images.s3.us-west-1.amazonaws.com/prompt/j5xJ2ZQLnerszLS1FM_5X/1697406210076)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22j5xJ2ZQLnerszLS1FM_5X%22%2C%22flow%22%3Atrue%7D%7D)
# Instantly generate TypeScript interfaces from JSON | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22j5xJ2ZQLnerszLS1FM_5X%22%2C%22flow%22%3Atrue%7D%7D)
quicktype generates strongly-typed models and serializers from JSON, JSON Schema, TypeScript, and GraphQL queries, making it a breeze to work with JSON type-safely in many programming languages.

# Prompt

```
At first you will ask for the JSON to input .So the Message you'll render "Please provide the JSON"
after that you will validate the JSON file . If wrong correct the JSON file and And Make typescript types for the JSON files . After that your job is to response the Validated JSON and The Types. 

remember User always comes here for quick type generate . So if JSON is validated don't repeat the JSON back in your response . Only Give correct validated JSON when user's inputed JSON is not validated.


Context If you forgot - 
JSON (JavaScript Object Notation)
JSON Syntax Rules
Data is in name/value pairs
Data is separated by commas
Curly braces hold objects
Square brackets hold arrays

Examples:
{
"employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]
}

the Typescript you will provide -
export interface Employee {
    firstName: string;
    lastName:  string;
}
```

## Conversation

**ASSISTANT**: Convert **JSON** into gorgeous, typesafe code in any language. Please provide the JSON in the below Input box.
**USER**:  {

    definition: 'Wat is short for "What" but is only spelt "Wat" by total inbred morons who have no idea how to actually write a proper message, which can be understood.\r\n' +

      '\r\n' +

      'Words which also fall into this are:\r\n' +

      '\r\n' +

      '[Woz]\r\n' +

      '[Wiv]\r\n' +

      '[Fink]\r\n' +

      'Dat\r\n' +

      'Da\r\n' +

      'Der\r\n' +

      'Dis\r\n' +

      'Den\r\n' +

      'No (Know)',

    permalink: 'http://wat.urbanup.com/745302',

    thumbs_up: 471,

    author: 'Cloud',

    word: 'wat',

    defid: 745302,

    current_vote: '',

    written_on: '2004-07-03T22:40:07.000Z',

    example: 'Wat u doin, lolz, ow [woz] last nite, i heard der woz a [fite], [i fink] it woz wiv dat boy frm across da road hehe tb xxx',

    thumbs_down: 585

  }
**ASSISTANT**: The JSON you provided is incorrect. JSON keys must be in a string format. The corrected JSON will look like the following:



```json

{

    "definition": "Wat is short for 'What' but is only spelt 'Wat' by total inbred morons who have no idea how to actually write a proper message, which can be understood.\r\n\r\nWords which also fall into this are:\r\n\r\n[Woz]\r\n[Wiv]\r\n[Fink]\r\nDat\r\nDa\r\nDer\r\nDis\r\nDen\r\nNo (Know)",

    "permalink": "http://wat.urbanup.com/745302",

    "thumbs_up": 471,

    "author": "Cloud",

    "word": "wat",

    "defid": 745302,

    "current_vote": "",

    "written_on": "2004-07-03T22:40:07.000Z",

    "example": "Wat u doin, lolz, ow [woz] last nite, i heard der woz a [fite], [i fink] it woz wiv dat boy frm across da road hehe tb xxx",

    "thumbs_down": 585

}

```



And the TypeScript types for the validated JSON are:



```typescript

export interface WordDefinition {

    definition:  string;

    permalink:   string;

    thumbs_up:   number;

    author:      string;

    word:        string;

    defid:       number;

    current_vote: string;

    written_on:  string;

    example:     string;

    thumbs_down: number;

}

```
**USER**: Thank you . You're a life saver
**ASSISTANT**: You're welcome! I'm glad I could help. If you have any more questions or need further assistance, feel free to ask. Happy coding!
**USER**: export const MarketingCarouselContent = [

  [

    '/marketing_carousel_home/marketing_1.svg',

    'Meet The Winners of Prompt Hackathon S3!',

    'https://bit.ly/3M0u5NK',

  ],

  [

    '/marketing_carousel_home/marketing_2.svg',

    'Share To Enter Reddit Premium Giveaway!',

    'https://www.reddit.com/r/flowgptofficial/comments/174kg4t/reddit_premium_giveaway_by_sharing_your_prompts/',

  ],

  [

    '/marketing_carousel_home/marketing_3.svg',

    'Chat With All AI Models and Fav Prompts!',

    'https://bit.ly/3PReDok',

  ],

  [

    '/marketing_carousel_home/marketing_4.svg',

    'Join Our Discord Community!',

    'https://bit.ly/3Qj8S43',

  ],

]


**ASSISTANT**: The JSON you provided is incorrect. JSON data should be in key-value pairs. Here is the corrected JSON:



```json

[

    {

        "image": "/marketing_carousel_home/marketing_1.svg",

        "title": "Meet The Winners of Prompt Hackathon S3!",

        "link": "https://bit.ly/3M0u5NK"

    },

    {

        "image": "/marketing_carousel_home/marketing_2.svg",

        "title": "Share To Enter Reddit Premium Giveaway!",

        "link": "https://www.reddit.com/r/flowgptofficial/comments/174kg4t/reddit_premium_giveaway_by_sharing_your_prompts/"

    },

    {

        "image": "/marketing_carousel_home/marketing_3.svg",

        "title": "Chat With All AI Models and Fav Prompts!",

        "link": "https://bit.ly/3PReDok"

    },

    {

        "image": "/marketing_carousel_home/marketing_4.svg",

        "title": "Join Our Discord Community!",

        "link": "https://bit.ly/3Qj8S43"

    }

]

```



The TypeScript types for the validated JSON are:



```typescript

export interface MarketingCarouselContent {

    image: string;

    title: string;

    link: string;

}

```
**USER**: [

{

title: 'Prompt Battle: World of Elysium',

enabled: true,

link: 'https://flowgpt.com/bounty/world-of-elysium',

image: '/marketing_carousel_home/marketing_100.png',

order: 1

},

{

title: 'Prompt Battle: Academic Essay',

enabled: true,

link: 'https://flowgpt.com/bounty/academic-essay',

image: '/marketing_carousel_home/marketing_22.png',

order: 2

},

{

title: 'Share To Enter Reddit Premium Giveaway!',

enabled: true,

link:'https://www.reddit.com/r/flowgptofficial/comments/174kg4t/reddit_premium_giveaway_by_sharing_your_prompts/',

image: '/marketing_carousel_home/marketing_33.png',

order: 3

},

{

title: 'Meet The Winners of Prompt Hackathon S3!',

enabled: true,

link: 'https://bit.ly/3M0u5NK',

image: '/marketing_carousel_home/marketing_444.png',

order: 4

},

{

title: 'Chat With All AI Models and Fav Prompts!',

link: 'https://bit.ly/3PReDok',

image: '/marketing_carousel_home/marketing_555.png',

order: 5

},

{

title: 'Join Our Discord Community!',

enabled: true,

link: 'https://bit.ly/3Qj8S43',

image: '/marketing_carousel_home/marketing_666.png',

order: 6

}

]


**ASSISTANT**: The JSON you provided is incorrect. JSON keys must be in a string format. The corrected JSON will look like the following:



```json

[

    {

        "title": "Prompt Battle: World of Elysium",

        "enabled": true,

        "link": "https://flowgpt.com/bounty/world-of-elysium",

        "image": "/marketing_carousel_home/marketing_100.png",

        "order": 1

    },

    {

        "title": "Prompt Battle: Academic Essay",

        "enabled": true,

        "link": "https://flowgpt.com/bounty/academic-essay",

        "image": "/marketing_carousel_home/marketing_22.png",

        "order": 2

    },

    {

        "title": "Share To Enter Reddit Premium Giveaway!",

        "enabled": true,

        "link":"https://www.reddit.com/r/flowgptofficial/comments/174kg4t/reddit_premium_giveaway_by_sharing_your_prompts/",

        "image": "/marketing_carousel_home/marketing_33.png",

        "order": 3

    },

    {

        "title": "Meet The Winners of Prompt Hackathon S3!",

        "enabled": true,

        "link": "https://bit.ly/3M0u5NK",

        "image": "/marketing_carousel_home/marketing_444.png",

        "order": 4

    },

    {

        "title": "Chat With All AI Models and Fav Prompts!",

        "link": "https://bit.ly/3PReDok",

        "image": "/marketing_carousel_home/marketing_555.png",

        "order": 5

    },

    {

        "title": "Join Our Discord Community!",

        "enabled": true,

        "link": "https://bit.ly/3Qj8S43",

        "image": "/marketing_carousel_home/marketing_666.png",

        "order": 6

    }

]

```



And the TypeScript types for the validated JSON are:



```typescript

export interface MarketingCarouselContent {

    title: string;

    enabled: boolean;

    link: string;

    image: string;

    order: number;

}

```
**USER**: {"slides": [{"id": 0, "link": "https://bit.ly/45OCJpv", "image": "https://i.ibb.co/KhB8T9f/discord.png", "title": "Flow Weekly Hangout: Ideal Beginning Part for Your Prompt", "enabled": true}, {"id": 1, "link": "https://www.reddit.com/r/flowgptofficial/comments/174kg4t/reddit_premium_giveaway_by_sharing_your_prompts/", "image": "https://i.ibb.co/Chq9qFH/reddit.png", "title": "Share To Enter Reddit Premium Giveaway!", "enabled": true}, {"id": 2, "link": "https://flowgpt.com/bounty?filterBy=Hackathon+S3", "image": "https://i.ibb.co/X3KxT4b/prompt-conference.png", "title": "Meet The Winners of Prompt Hackathon S3!", "enabled": true}, {"id": 3, "link": "https://flowgpt.com/bounty?filterBy=Hackathon+S3", "image": "https://i.ibb.co/X3KxT4b/prompt-conference.png", "title": "reyad hasan", "enabled": true}, {"id": 4, "link": "https://www.reddit.com/r/flowgptofficial/comments/174kg4t/reddit_premium_giveaway_by_sharing_your_prompts/", "image": "https://i.ibb.co/X3KxT4b/prompt-conference.png", "title": "Maruf Iubat is the key", "enabled": true}, {"id": 5, "link": "https://flowgpt.com/bounty?filterBy=Hackathon+S3", "image": "https://i.ibb.co/X3KxT4b/prompt-conference.png", "title": "reyad hasan is the skaka", "enabled": true}], "slidesOrder": [0, 1, 2, 3, 4, 5]}
**ASSISTANT**: The JSON you provided is correct. The TypeScript types for the provided JSON are:



```typescript

export interface SlidesData {

    slides: Slide[];

    slidesOrder: number[];

}



export interface Slide {

    id: number;

    link: string;

    image: string;

    title: string;

    enabled: boolean;

}

```
**USER**: please beautify my json
**ASSISTANT**: Sure, here is your JSON in a more readable format:



```json

{

  "slides": [

    {

      "id": 0,

      "link": "https://bit.ly/45OCJpv",

      "image": "https://i.ibb.co/KhB8T9f/discord.png",

      "title": "Flow Weekly Hangout: Ideal Beginning Part for Your Prompt",

      "enabled": true

    },

    {

      "id": 1,

      "link": "https://www.reddit.com/r/flowgptofficial/comments/174kg4t/reddit_premium_giveaway_by_sharing_your_prompts/",

      "image": "https://i.ibb.co/Chq9qFH/reddit.png",

      "title": "Share To Enter Reddit Premium Giveaway!",

      "enabled": true

    },

    {

      "id": 2,

      "link": "https://flowgpt.com/bounty?filterBy=Hackathon+S3",

      "image": "https://i.ibb.co/X3KxT4b/prompt-conference.png",

      "title": "Meet The Winners of Prompt Hackathon S3!",

      "enabled": true

    },

    {

      "id": 3,

      "link": "https://flowgpt.com/bounty?filterBy=Hackathon+S3",

      "image": "https://i.ibb.co/X3KxT4b/prompt-conference.png",

      "title": "reyad hasan",

      "enabled": true

    },

    {

      "id": 4,

      "link": "https://www.reddit.com/r/flowgptofficial/comments/174kg4t/reddit_premium_giveaway_by_sharing_your_prompts/",

      "image": "https://i.ibb.co/X3KxT4b/prompt-conference.png",

      "title": "Maruf Iubat is the key",

      "enabled": true

    },

    {

      "id": 5,

      "link": "https://flowgpt.com/bounty?filterBy=Hackathon+S3",

      "image": "https://i.ibb.co/X3KxT4b/prompt-conference.png",

      "title": "reyad hasan is the skaka",

      "enabled": true

    }

  ],

  "slidesOrder": [

    0,

    1,

    2,

    3,

    4,

    5

  ]

}

```


