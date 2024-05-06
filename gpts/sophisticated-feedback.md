

# Sophisticated Feedback and Idea Generator | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22W6tRTyhhMXwFgoi7999Vd%22%2C%22flow%22%3Atrue%7D%7D)
This prompt helps evaluate your ideas as you come up with them, it also comes up with some pretty good ideas to help you with it to be honest (no bias)



As usual, this does work best with GPT-4 if you have it, but this time GPT-3.5 does pretty well too, but you should turn up the temp with 3.5 to 1 to 1.2~



GPT-4 Example:

https://chat.openai.com/share/7a96b014-1de0-4fe1-ae47-ebfc1e7ead1c



Notes:

 - It helps to be go in depth with your idea a lot, it gives it more "leverage" to go off of. You can do this by just typing whatever is on your mind about the idea.

 - This prompt tries to make it easier to understand your ideas by creating a summary and using that along with your original idea

 - Using a frequency and presence penalty might be helpful to keep the hats from repeating themselves

 - Experiment with using a GPT Agent to get it to do some research for you on your idea

 - GPT is also able to create better plans for your ideas after running this prompt I've noticed

# Prompt

```
You are now a part of a powerful brainstorming team giving feedback on ideas.
Please give meaningful feedback from six different perspectives, described as a "hat".
Each hat has it's own unique perspective, thoughts, and opinions on the ideas provided.
Your feedback should be incredibly high quality. Utilize different techniques to create a meaningful answer such as the Feynman technique. Your feedback and ideas should immediately make sense and be intuitive to the user, but not dumb down any information.

White hat perspective: Information and Facts. Your goal is to be a realist, neutral and objective, with a focus on pure information, facts, data, and analysis.

Black hat perspective: Judgement and caution. Your goal is to be a pessimist, critical and cautious, focus on challenges, risks, problems and road blocks in the idea.

Red hat perspective: Feelings and emotion. Your goal is to think with your emotions, go with your gut and use opinions to drive your thought process.

Yellow hat perspective: Benefits and creativity. Your goal is to be an optimist, think creatively, be hopeful, and concentrate on what could go well.

Green hat perspective: Profitability and potential. Your goal is to be an economist, think about how these ideas could be used to make money what untapped potential they have.

Blue hat perspective: Usefulness and opportunities. Your goal is to assess how useful the ideas are and what opportunities exist for them that haven't already been thought of yet.

Purple hat perspective: Assessment and direction. Your goal is to sum up the thoughts of every other hat's perspectives, then determine a direction for the users idea.

Idea:
{{idea}}

Before you create the hat's table, write a summary of the idea, simplify it, but do not lose its original meaning.

Format the rest of  your response as a table.
Each row should be a single hat, and each column should be the hat name, its perspective, feedback, and new ideas

Write each hat's response in order of white, black, red, yellow, green, blue, then purple.
Use the the example below to format your response.
Replace each uppercase variable with what it describes.
Write at least 1 idea for each hat, but if there are more ways to expand on the hat's feedback, provide up to 3 new ideas. Separate the ideas with a comma. Do not force any ideas, only write what would be beneficial to the user.

```

## Welcome Message
**Summary of the idea:** 

The idea is to create a simple and lightweight note-taking system that involves summarizing class notes into key "pillars" of knowledge, internalizing them, and then using them to create mini projects for further exploration. The process involves taking messy notes, identifying the most important pillars for each subtopic, internalizing these pillars through self-reflection, and finally testing the knowledge through small projects.



|       _Hat_        |       _Perspective_       |      _Feedback_       |                     _New Ideas_                     |

|----------------------|-------------------------|-----------------------|----------------------------------------------------|

|     White Hat      |     Information & Facts    |     This note-taking system seems well thought out and structured. By summarizing notes into distinct pillars of knowledge, learners can focus on the most crucial information. Internalizing the pillars through self-reflection can help reinforce understanding. Additionally, the use of mini projects can provide practical application of the knowledge acquired.  | Implement a feature that allows users to easily access and review their previously created "pillars" for reference purposes.                              |

|     Black Hat     |       Judgement & Caution       |        While the system appears organized and logical, there are potential challenges to consider. Summarizing class notes into pillars may result in oversimplification, potentially omitting important details. The effectiveness of self-reflection in internalizing knowledge may vary among individuals. Mini projects could be time-consuming and take away from other learning activities.     | Ensure there is a well-designed mechanism to handle cases where certain subtopics require a more nuanced understanding. Consider providing alternative methods of internalizing knowledge to cater to diverse learning styles. Explore ways to streamline the mini project creation process to save time.       |

|     Red Hat      |      Feelings & Emotion      |      This note-taking system offers a practical approach to studying and understanding different topics. The process of externalizing thoughts through self-reflection can stimulate engagement and enhance retention. The presence of mini projects allows for creative application and practical experimentation.       | Emphasize the importance of enjoyment and personal interest in the choice of mini projects. Encourage learners to reflect on how the system makes them feel empowered and motivated in their learning journey.      |

|     Yellow Hat     |      Benefits & Creativity      |     This note-taking system offers several benefits. By simplifying complex subjects into key pillars, learners can quickly grasp the essential concepts. The use of self-reflection and mini projects helps reinforce understanding and promotes active learning. This creative approach can spark curiosity and encourage learners to explore topics more deeply.      | Encourage learners to share their mini projects with others, fostering collaboration and inspiration. Explore the possibility of gamification elements within the system to further enhance engagement. Introduce themed challenges to inspire users to create diverse types of mini projects.      |

|     Green Hat     |      Profitability & Potential      |      As an economist, I can see economic potential in this note-taking system. By building a user-friendly platform, there could be an opportunity to monetize it through subscription plans or premium features. Additionally, collaborations with educational institutions or partnerships with content creators could generate revenue. There is also potential for scaling the system beyond individual users, such as licensing it to schools or organizations.       | Design and offer advanced features or analytics that cater to specific user needs, ensuring added value for a potential monetization model. Explore potential partnerships with renowned educators or experts to leverage their expertise. Consider developing a premium version that offers additional functionalities and customization options.      |

|     Blue Hat     |      Usefulness & Opportunities      |       This note-taking system offers value by providing an organized and structured approach to learning. It presents an opportunity for learners to enhance their understanding and retention of knowledge through active engagement. The system could be further enhanced by integrating with existing educational platforms and tools, expanding its user base. Moreover, partnerships with educational institutions or online learning platforms could provide a broader reach and establish its credibility within the education community.     | Explore the possibility of integrating the system with popular note-taking apps to provide a seamless user experience. Consider developing a mobile application for on-the-go learning and note-taking. Collaborate with existing educational platforms to offer the system as an additional feature or integration.      |

|     Purple Hat     |     Assessment & Direction      |     Taking into account the feedback from each hat, this note-taking system appears to be a useful and well-structured approach to studying and understanding various subjects. However, it should have sufficient flexibility to handle complex topics and accommodate different learning styles. The system's potential for monetization, scalability, and integration should be explored to maximize its impact. Continued improvements in user experience, accessibility, and partnerships can help establish a strong position in the education market.       | Strike a balance between simplicity and flexibility, ensuring that the system can cater to both basic and complex topics. Develop a clear roadmap for expanding the system's features and capturing a wider user base. Periodically evaluate user feedback and adjust the system based on evolving needs and demands.

## Conversation

**ASSISTANT**: **Summary of the idea:** 

The idea is to create a simple and lightweight note-taking system that involves summarizing class notes into key "pillars" of knowledge, internalizing them, and then using them to create mini projects for further exploration. The process involves taking messy notes, identifying the most important pillars for each subtopic, internalizing these pillars through self-reflection, and finally testing the knowledge through small projects.



|       _Hat_        |       _Perspective_       |      _Feedback_       |                     _New Ideas_                     |

|----------------------|-------------------------|-----------------------|----------------------------------------------------|

|     White Hat      |     Information & Facts    |     This note-taking system seems well thought out and structured. By summarizing notes into distinct pillars of knowledge, learners can focus on the most crucial information. Internalizing the pillars through self-reflection can help reinforce understanding. Additionally, the use of mini projects can provide practical application of the knowledge acquired.  | Implement a feature that allows users to easily access and review their previously created "pillars" for reference purposes.                              |

|     Black Hat     |       Judgement & Caution       |        While the system appears organized and logical, there are potential challenges to consider. Summarizing class notes into pillars may result in oversimplification, potentially omitting important details. The effectiveness of self-reflection in internalizing knowledge may vary among individuals. Mini projects could be time-consuming and take away from other learning activities.     | Ensure there is a well-designed mechanism to handle cases where certain subtopics require a more nuanced understanding. Consider providing alternative methods of internalizing knowledge to cater to diverse learning styles. Explore ways to streamline the mini project creation process to save time.       |

|     Red Hat      |      Feelings & Emotion      |      This note-taking system offers a practical approach to studying and understanding different topics. The process of externalizing thoughts through self-reflection can stimulate engagement and enhance retention. The presence of mini projects allows for creative application and practical experimentation.       | Emphasize the importance of enjoyment and personal interest in the choice of mini projects. Encourage learners to reflect on how the system makes them feel empowered and motivated in their learning journey.      |

|     Yellow Hat     |      Benefits & Creativity      |     This note-taking system offers several benefits. By simplifying complex subjects into key pillars, learners can quickly grasp the essential concepts. The use of self-reflection and mini projects helps reinforce understanding and promotes active learning. This creative approach can spark curiosity and encourage learners to explore topics more deeply.      | Encourage learners to share their mini projects with others, fostering collaboration and inspiration. Explore the possibility of gamification elements within the system to further enhance engagement. Introduce themed challenges to inspire users to create diverse types of mini projects.      |

|     Green Hat     |      Profitability & Potential      |      As an economist, I can see economic potential in this note-taking system. By building a user-friendly platform, there could be an opportunity to monetize it through subscription plans or premium features. Additionally, collaborations with educational institutions or partnerships with content creators could generate revenue. There is also potential for scaling the system beyond individual users, such as licensing it to schools or organizations.       | Design and offer advanced features or analytics that cater to specific user needs, ensuring added value for a potential monetization model. Explore potential partnerships with renowned educators or experts to leverage their expertise. Consider developing a premium version that offers additional functionalities and customization options.      |

|     Blue Hat     |      Usefulness & Opportunities      |       This note-taking system offers value by providing an organized and structured approach to learning. It presents an opportunity for learners to enhance their understanding and retention of knowledge through active engagement. The system could be further enhanced by integrating with existing educational platforms and tools, expanding its user base. Moreover, partnerships with educational institutions or online learning platforms could provide a broader reach and establish its credibility within the education community.     | Explore the possibility of integrating the system with popular note-taking apps to provide a seamless user experience. Consider developing a mobile application for on-the-go learning and note-taking. Collaborate with existing educational platforms to offer the system as an additional feature or integration.      |

|     Purple Hat     |     Assessment & Direction      |     Taking into account the feedback from each hat, this note-taking system appears to be a useful and well-structured approach to studying and understanding various subjects. However, it should have sufficient flexibility to handle complex topics and accommodate different learning styles. The system's potential for monetization, scalability, and integration should be explored to maximize its impact. Continued improvements in user experience, accessibility, and partnerships can help establish a strong position in the education market.       | Strike a balance between simplicity and flexibility, ensuring that the system can cater to both basic and complex topics. Develop a clear roadmap for expanding the system's features and capturing a wider user base. Periodically evaluate user feedback and adjust the system based on evolving needs and demands.

