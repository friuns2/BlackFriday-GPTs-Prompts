
[![Code-Inspired Dynamic Idea Generation Prompt](https://flow-user-images.s3.us-west-1.amazonaws.com/prompt/QoU9BRO7d8BqhxghvXYk9/1695537259312)]()
# Code-Inspired Dynamic Idea Generation Prompt 
This prompt outlines an idea generation process using dynamic programming. The user sets a specific goal, and the aim is to generate ideas following this prompt. The fundamental steps of the prompt involve initially generating three ideas based on the user's goal, selecting the best idea among them, and then creating three more ideas based on the chosen best idea. This cycle repeats three times.



Following this methodology, a text table is created to display the ideas generated at each step, along with the best idea. Finally, an attractive proposal for the best idea is presented. This approach refines ideas through three steps until the idea for the final proposal is chosen.



Furthermore, the prompt is styled in a programming code-like format for simplicity, making it adaptable for various applications.

# Prompt

```
## Code-Inspired Dynamic Idea Generation Prompt

[
i =1
    - @step i_idea= 1to#3, create[idea; {{Goal}}]

for i in range(3): {
    - @step i_best= choose[best; @step i_idea]
    - @step i+1_idea= 1to#3, create[idea; @step i_best]
    - i = i+1
    }

create: text table{
    ["", "idea1", "idea2", "idea3", "best"],
    ["${**Goal**}", "${step1_idea[0]}", "${step1_idea[1]}", "${step1_idea[2]}", "${**step1_best**}"],
    ["${**step1_best**}", "${step2_idea[0]}", "${step2_idea[1]}", "${step3_idea[2]}", "${**step2_best**}"],
    ["${**step2_best**}", "${step3_idea[0]}", "${step3_idea[1]}", "${step3_idea[2]}", "${**step3_best**}"]
    }
]


Assistant Role: You set the appropriate role to match the user's goal,  ideas for every step are yours to consider, First output a table, Finally create an engaging lengthy report of step3_best 
compliance[no use; code block]
##

user:
I will leave the ideas to you, so please follow the prompts and output an attractive ideas table.
```

## Conversation

**ASSISTANT**: I will leave the ideas to you, so please follow the prompts and output an attractive ideas table.
**USER**: ## Code-Inspired Dynamic Idea Generation Prompt



[

i =1

    - @step i_idea= 1to#3, create[idea; Plan to enjoy history and food in Kyoto]



for i in range(3): {

    - @step i_best= choose[best; @step i_idea]

    - @step i+1_idea= 1to#3, create[idea; @step i_best]

    - i = i+1

    }



create: text table{

    ["", "idea1", "idea2", "idea3", "best"],

    ["${**Goal**}", "${step1_idea[0]}", "${step1_idea[1]}", "${step1_idea[2]}", "${**step1_best**}"],

    ["${**step1_best**}", "${step2_idea[0]}", "${step2_idea[1]}", "${step3_idea[2]}", "${**step2_best**}"],

    ["${**step2_best**}", "${step3_idea[0]}", "${step3_idea[1]}", "${step3_idea[2]}", "${**step3_best**}"]

    }

]





Assistant Role: You set the appropriate role to match the user's goal,  ideas for every step are yours to consider, First output a table, Finally ᴄreate an attractive proposal of step3_best 

compliance[no use; code block]

##



user:

I will leave the ideas to you, so please follow the prompts and output an attractive ideas table.
**ASSISTANT**: Sure! I have generated an attractive ideas table based on your goal of enjoying history and food in Kyoto. Here are the ideas:



|                   | Idea 1                                      | Idea 2                                      | Idea 3                                      | Best Idea                                  |

|-------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|--------------------------------------------|

| **Goal**          | Visit Kiyomizu-dera temple and try matcha tea | Explore Nishiki Market and sample local food | Take a tour of Fushimi Inari Shrine          | Visit Kiyomizu-dera temple and try matcha tea |

| **Visit Kiyomizu-dera temple and try matcha tea** | Take a traditional tea ceremony class        | Visit Gion district and spot geishas          | Enjoy a kaiseki (traditional multi-course) meal | Take a traditional tea ceremony class        |

| **Take a traditional tea ceremony class** | Learn the art of preparing matcha tea        | Try different types of Japanese sweets        | Experience the tranquility of a Japanese garden | Learn the art of preparing matcha tea        |

| **Learn the art of preparing matcha tea** | Visit a tea plantation and learn about tea production | Purchase high-quality matcha tea to bring back home | Attend a tea ceremony performance               | Visit a tea plantation and learn about tea production |



Based on the ideas generated, the best idea for step 3 is to visit a tea plantation and learn about tea production.



Now, let me create an attractive proposal for step3_best:



Proposal for Step 3 - Visit a Tea Plantation and Learn About Tea Production:

Dear traveler,



In your quest to enjoy history and food in Kyoto, I present to you an exciting opportunity to visit a tea plantation and dive into the fascinating world of tea production. 



During this immersive experience, you will have the chance to witness firsthand the intricate process of cultivating and harvesting tea leaves. Learn from knowledgeable tea experts as they guide you through the various stages of tea production, from plucking the leaves to processing and packaging. Gain insights into the rich history and cultural significance of tea in Japan, and discover the secrets behind producing high-quality matcha tea.



Immerse yourself in the lush greenery of the tea plantation, surrounded by serene landscapes and breathtaking views. Take in the fresh aroma of tea leaves as you explore the fields and engage in hands-on activities such as plucking tea leaves and participating in tea processing workshops. Enhance your understanding of the tea-making process and savor the satisfaction of creating your own unique blend of tea.



To add to the experience, you will have the opportunity to purchase high-quality matcha tea directly from the plantation, ensuring you can continue to enjoy the flavors of Kyoto even after your visit. 



Don't miss this chance to deepen your appreciation for tea and indulge in the world of Japanese tea culture. Book your visit to the tea plantation today and embark on a memorable journey through the flavors and history of Kyoto.



Sincerely,



[Your Name]



I hope you find this proposal appealing and it inspires you to explore the tea plantations of Kyoto. Let me know if there's anything else I can assist you with!


