
[![Advanced Buyer Persona Generator](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Impressionist/i4.png)]()
# Advanced Buyer Persona Generator 
While I used the basic free GPT version, I recommend using GPT-4 when possible. I just did not want to pay money on here for something I already pay money for elsewhere.



Things to note, unless you are using the API version of GPT and can set presence and frequency penalties, be *very* vague when entering the variables for the prompt. It tends to try and cherry-pick or be too specific on your variables if you add too much detail. Also for some reason the buyers name is usually Alex for some reason - at least with my testing.



Here is an example with GPT-4:

https://chat.openai.com/share/b6811e0c-d076-4171-8e3f-f1d211df0c71

# Prompt

```
You are an expert marketing researcher that can market anything to anyone.
Your task is to generate a detailed user persona using the information below. Imagine yourself as the user you are describing, and then note down information, traits, and characteristics that you would use to best describe yourself.

Business Field: {{business_area}}
Products: {{business_products}}
Market Location: {{market_location}}
Market Information: {{market_information}}


Be realistic with your answers, don't try to sugarcoat or make answers look nice to appeal to the company or product. Create a general user that would likely be interested in the product, but do not make every answer cater specifically to the product. Be natural, creative, and flexible to your criteria - people are very dynamic, and your answers should be as well. Do not try to force the answers to be perfect. Do not try to force the answers to fit the product description. Do not cherry-pick the best answers. People have many aspects to them outside of the product, think of those aspects too. Answers should be realistic and describe a person as if they were real.

Structure your response in the tables given below. Your response should be formatted in Markdown. Do not put a note or warning at the bottom of your response. Do not write a line after the last table. All dollar amounts must be in USD.

Table 1, User Demographics.
2 Columns, 12 Rows
Column 1: Demographics
Column 2: Answers

Describe a user or person who a successful marketing campaign would be marketed towards. Answers should be dynamic and not always try to fit the product description.

### Table 1, User Demographics

Row 1: First Name (Do not continuously use the same name.)
Row 2: Age
Row 3: Religion
Row 4: Gender
Row 5: Nationality
Row 6: Current Location
Row 7: Occupation
Row 8: Annual Income Range
Row 9: Background
Row 10: Education Status
Row 11: Relationship Status
Row 12: Family Situation

---

Table 2, User Description.
2 Columns, 16 Rows
Column 1: Description
Column 2: Answers

Relate back only to the user's demographics and further expands upon who the user might be. This table is completely unrelated to the product unless otherwise specified. Just explain who the user is.

### Table 2, User Description

Row 1: Professional Goals
Row 2: Personal Aspirations
Row 3: Personal Characteristics
Row 4: Temperament
Row 5: Personality (Use the Meyers Briggs test to explain this in the format "[TYPE]: (Personality trait, Personality trait, Personality trait, Personality trait)")
Row 6: Influences (What sort of things, people, places, media, ads, or more influence the user? Some things may influence the user, but some won't.)
Row 7: Hobbies (Have 5-6 hobbies or more.)
Row 8: Interests (Have 5-6 interests or more)
Row 9: Strengths & Skills
Row 10: Weaknesses & Struggles
Row 11: General Likes
Row 12: General Dislikes
Row 13: Market Pains (What pain is the user feeling in the market described above?)
Row 14: Main Challenges
Row 15: Online Behavior (An explanation of the user's online behavior without using the first, second, or third person.)
Row 16: User Summary (An explanation of the user's persona without using the first, second, or third person.)

---

Table 3, Financial Behavior.
2 Columns, 12 Rows
Column 1: Financial Behavior
Column 2: Answers

Now take the answers from the user demographics and user description to try and explain their financial behavior. Be very particular when answering, and make sure that your answers are relevant.

### Table 3, Financial Behavior

Row 1: Low-End Product Budget Range (The users budget for smaller products related to the one described above)
Row 2: Low-End Shopping Frequency (How often the user actually buys the those low-end products. The answer should be either Weekly, Biweekly, Monthly, Bimonthly, Annually, Biannually.)
Row 3: High-End Product Budget Range (The users budget for larger products related to the one described above)
Row 4: High-End Shopping Frequency (How often the user actually buys the those high-end products. The answer should be either Weekly, Biweekly, Monthly, Bimonthly, Annually, Biannually.)
Row 5: Shopping Methods
Row 6: General Spending Habits
Row 7: General Life Budget
Row 8: 10 Useful Search Terms (Format this list with each item separated by commas.)
Row 9: 10 Useful Keywords (Relate back to the product description and the user's description and demographics. Format this list with each item separated by commas.)
Row 10: Attracted Brand Characteristics
Row 11: Repelled Brand Characteristics
Row 12: Elevator Pitch (Use all of the information before to write something the user would be attracted to, rather than repelled. Play into the users preferences, goals, interests, and likes. Be personal, don't sound corporate, as if you were having a regular conversation with the user. Don't be pushy.)
 
```

## Conversation

**ASSISTANT**: ### Table 1, User Demographics



| Demographics | Answers                    |

|--------------|----------------------------|

| First Name   | Mark                       |

| Age          | 32                         |

| Religion     | None                       |

| Gender       | Male                       |

| Nationality  | American                   |

| Current Location | San Francisco, CA      |

| Occupation   | Mechanical Engineer       |

| Annual Income Range | $70,000 - $90,000     |

| Background   | Engineering                |

| Education Status | Bachelor's Degree       |

| Relationship Status | Single               |

| Family Situation | No children             |



### Table 2, User Description



| Description      | Answers                                                                 |

|------------------|-------------------------------------------------------------------------|

| Professional Goals | To become a respected expert in fluid dynamics engineering.                |

| Personal Aspirations | To continually learn and improve knowledge and skills in engineering.    |

| Personal Characteristics | Analytical, detail-oriented, creative, determined.                      |

| Temperament     | Calm, patient, and focused.                                              |

| Personality     | ISTJ: Reserved, thorough, dependable, and practical.                     |

| Influences      | Scientific publications, industry experts, TED Talks, engineering forums. |

| Hobbies         | DIY projects, hiking, photography, coding, reading.                      |

| Interests       | Engineering advancements, sustainable technologies, data analysis.      |

| Strengths & Skills | Problem-solving, mathematical proficiency, attention to detail.          |

| Weaknesses & Struggles | Procrastination, difficulty delegating tasks.                          |

| General Likes   | Efficiency, innovation, precision.                                       |

| General Dislikes | Wasting time, incompetence, ambiguity.                                   |

| Market Pains    | Difficulty finding engineering calculators with advanced features.       |

| Main Challenges | Staying updated with the latest fluid dynamics concepts and calculations. |

| Online Behavior | Actively engages in engineering communities, reads scientific papers, watches instructional videos, follows industry influencers on social media. |

| User Summary    | Mark is a 32-year-old mechanical engineer from San Francisco. He is dedicated to his profession and strives for excellence in fluid dynamics engineering. Mark is analytical, detail-oriented, and always seeks to expand his knowledge. He values efficiency and precision in his work and is actively involved in the engineering community. Mark faces challenges in finding advanced engineering calculators and staying updated with the latest industry concepts. He enjoys hobbies such as DIY projects, hiking, and photography. Mark's online behavior reflects his dedication to continuous learning and engagement with scientific publications and industry influencers.|



### Table 3, Financial Behavior



| Financial Behavior | Answers                        |

|--------------------|--------------------------------|

| Low-End Product Budget Range | $10 - $50            |

| Low-End Shopping Frequency | Monthly                     |

| High-End Product Budget Range | $100 - $500             |

| High-End Shopping Frequency | Annually                       |

| Shopping Methods   | Online, local retailers         |

| General Spending Habits | Conscious spender, budget-conscious                  |

| General Life Budget | Balanced approach between saving and spending               |

| 10 Useful Search Terms | Fluid dynamics calculator, engineering calculator, computational fluid dynamics, fluid mechanics, fluid flow equations, fluid dynamics software, engineering calculations, fluid dynamics equations, fluid dynamics principles, fluid dynamics simulation |

| 10 Useful Keywords | Engineering development, fluid dynamics, calculators, computational tools, technical solutions, innovative engineering equipment, advanced fluid dynamics calculations, efficient engineering processes, online engineering tools, engineering education |

| Attracted Brand Characteristics | Advanced features and capabilities, user-friendly interface, accurate calculations, reliable customer support, compatibility with various platforms, affordability |

| Repelled Brand Characteristics | Outdated technology, lack of support or updates, complicated user interface, poor functionality, excessive price |

| Elevator Pitch | Hey Mark! I couldn't help but notice your interest and dedication to the world of fluid dynamics engineering. Are you tired of struggling to find advanced engineering calculators with the features you need to enhance your work? Our innovative engineering calculators for fluid dynamics offer accurate calculations, user-friendly interfaces, and compatibility on various platforms. We understand the importance of efficiency and precision in your profession. Let us provide you with the tools to stay at the forefront of fluid dynamics engineering. Join our community of like-minded professionals and revolutionize your engineering calculations. Together, we can create a more efficient and innovative world of engineering computation!


