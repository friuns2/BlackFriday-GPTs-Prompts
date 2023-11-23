
[![Use This Prompting Trick To Improve ChatGPT’s Performance (multi-prompt)](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/futuristic/futu_5.png)]()
# Use This Prompting Trick To Improve ChatGPT’s Performance (multi-prompt) 
Unlock the full potential of ChatGPT with this simple trick

As a powerful and versatile language model, ChatGPT from OpenAI has the ability to engage in complex debates on a wide range of topics. However, to truly showcase its analytical capabilities and produce deep and thought-provoking responses, a trick can be employed to elicit more detailed and structured answers.



The trick is to include a request for ChatGPT to generate a hierarchical table of contents before providing the answer. This causes the AI to carefully analyze the structure of the issue at hand and organize its thoughts in a logical manner, much like a human writer would create an outline to plan and organize their ideas before composing an essay or speech.



Empirically, asking for a table of contents seems to greatly enhance ChatGPT’s ability to write coherent long-form essays. See the following multi-prompt example.

# Prompt

```
You are at the world debate championship. The motion of the debate is “This house supports universal income for all citizens”. The coalition are in favor of the motion. Think about arguments in favor of the motion, using a hierarchical table of contents that classify the arguments to at least 3 topics, then write the speech of the coalition. Then do the same for the opposition, who should argue against the arguments of the coalition.
```

## Conversation

**ASSISTANT**: Sure, here's an outline for the coalition's argument:



I. Introduction

- Definition of universal income

- Explanation of why it is important to discuss this topic



II. Social Justice 

- Ensuring everyone has a basic standard of living 

- Reducing poverty and inequality 

- Providing a safety net for those who cannot work



III. Economic Benefits

- Boosting consumer spending and demand 

- Encouraging entrepreneurship and innovation 

- Reducing administrative costs associated with means-tested benefits



IV. Human Dignity

- Giving people greater freedom and independence 

- Empowering individuals to pursue their dreams 

- Eliminating the stigma that can come with receiving welfare 



V. Conclusion

- Summarize key points 

- Reiterate why universal income is a worthwhile policy to implement



And here's an outline for the opposition's argument:



I. Introduction

- Definition of universal income

- Explanation of why it is important to consider opposing views



II. Affordability

- Concerns over the cost of implementing universal income 

- Potential for increased taxes and/or reduction in other social services 



III. Disincentive to Work

- Potential for individuals to rely solely on universal income 

- Risk of reducing motivation to seek employment or improve one's skills 



IV. Fairness

- Arguments that those who work harder or contribute more should receive greater rewards 

- Questions around whether universal income is fair to those who do not receive it 



V. Conclusion

- Summarize key points 

- Argue against the notion that universal income is a worthwhile policy to implement.
**USER**: Now write the speech of the coalition, and the speech of the opposition. Start with the words “Ladies and gentlemen”
**ASSISTANT**: Sure, here's a sample speech for the coalition:



Ladies and gentlemen,



Today we stand in favor ofSpeech of the Coalition:



Ladies and gentlemen, today we are here to discuss a topic that has far-reaching implications for the future of our society. We believe that universal income is an idea whose time has come.



Firstly, let's consider social justice. Universal income can ensure that everyone has a basic standard of living, regardless of their employment status or background. It can reduce poverty and inequality by providing a safety net for those who cannot work. This will help to create a fairer and more equal society for all.



Secondly, let's talk about economic benefits. Universal income can boost consumer spending and demand, which in turn can stimulate economic growth. It can also encourage entrepreneurship and innovation, as people have the financial security to take risks and pursue their ideas. Moreover, means-tested benefits can be administratively costly, so replacing them with a universal income could save money in the long run.



Finally, let's consider human dignity. Providing a basic income gives people greater freedom and independence to make choices about their lives. They can pursue their dreams without fear of falling into poverty. Moreover, it eliminates the stigma that can come with receiving welfare, helping to restore dignity and respect to those who need support.



In conclusion, we urge you to support the motion. Universal income is a policy that can benefit us all, creating a fairer, more prosperous, and more dignified society.



Speech of the Opposition:



Ladies and gentlemen, while we acknowledge the good intentions of the proposition, we must raise some pressing concerns that lead us to oppose the motion.



Firstly, affordability is a major concern. Implementing universal income would be a costly endeavor, inevitably requiring higher taxes or cuts to other essential services. We must ask ourselves whether this is a wise use of resources, particularly when there is no guarantee that it will solve the underlying issues.



Secondly, we must consider the potential disincentive to work. If people receive a basic income regardless of whether they work or not, there is a risk that some may choose to rely solely on the income and lose motivation to find employment or improve their skills. This could lead to long-term consequences for both the economy and society.



Thirdly, we must question whether universal income is a fair policy. Those who work harder or contribute more might feel resentful if they receive the same income as those who do not put in as much effort. We must consider whether it is right to take money from those who have earned it through hard work to give it to those who have not.



In summary, we believe that implementing universal income is not the best way to tackle poverty and inequality. Rather than creating a safety net, it risks creating a culture of dependence and reducing the motivation for people to work and contribute to society. We urge you to consider these concerns and vote against the motion.
**USER**: Create a mindmap in mermaid JS notation for this debate
**ASSISTANT**: I'm sorry, as an AI language model, I am not able to create visualizations in mermaid JS notation. However, I can provide you with the text format of a mindmap for this debate:



```

graph LR



A[This house supports universal income for all citizens] --> B(Social Justice)

A --> C(Economic Benefits)

A --> D(Human Dignity)

B --> |Ensures basic standard of living| BA

B --> |Reduces poverty and inequality| BB

B --> |Provides a safety net| BC

C --> |Boosts consumer spending and demand| CA

C --> |Encourages entrepreneurship and innovation| CB

C --> |Reduces administrative costs| CC

D --> |Gives greater freedom and independence| DA

D --> |Empowers individuals to pursue their dreams| DB

D --> |Eliminates stigma associated with welfare| DC



E[Opposition] --> F(Affordability)

E --> G(Disincentive to Work)

E --> H(Fairness)

F --> |Costly endeavor| FA

F --> |Cuts to essential services| FB

F --> |No guarantee it will solve underlying issues| FC

G --> |Risk of relying solely on income| GA

G --> |Loss of motivation to work or improve skills| GB

H --> |Might feel resentful| HA

H --> |Right to take money from hardworking individuals| HB

```I'm sorry, as an AI language model I cannot create visuals directly. However, I can provide you with the Mermaid JS code to create a Mind Map for this debate as follows:



```

graph LR

A[This house supports universal income for all citizens] --> B(Social Justice)

B --> |Ensuring basic standard of living|BA

B --> |Reducing poverty and inequality|BB

B --> |Providing safety net|BC

A --> C(Economic Benefits)

C --> |Boosting consumer spending|CA

C --> |Encouraging entrepreneurship|CB

C --> |Reducing administrative costs|CC

A --> D(Human Dignity)

D --> |Giving freedom and independence|DA

D --> |Empowering individuals|DB

D --> |Eliminating stigma|DC



E[Opposition]

E --> F(Affordability)

F --> |Increased taxes and cuts to services|FA

E --> G(Disincentive to Work)

G --> |Risk of over-reliance|GA

G --> |Reduced motivation to work|GB

E --> H(Fairness)

H --> |Rewards based on hard work|HA

H --> |Is it fair to take from earners?|HB

``` 



You can copy and paste the above code into the Mermaid Live Editor (https://mermaid-js.github.io/mermaid-live-editor/) to visualize it as a Mind Map.
**USER**: Give it to me in mermaidJS mindmap format. 

Here's an example:

mindmap

  root((mindmap))

    Origins

      Long history

      ::icon(fa fa-book)

      Popularisation

        British popular psychology author Tony Buzan

    Research

      On effectivness<br/>and features

      On Automatic creation

        Uses

            Creative techniques

            Strategic planning

            Argument mapping

    Tools

      Pen and paper

      Mermaid
**ASSISTANT**: Sure, here's the Mind Map for the debate in Mermaid JS notation:



```

mindmap

  root((This house supports universal income for all citizens))

    Coalition

      Social Justice

        - Ensuring basic standard of living

        - Reducing poverty and inequality 

        - Providing safety net

      Economic Benefits

        - Boosting consumer spending 

        - Encouraging entrepreneurship 

        - Reducing administrative costs 

      Human Dignity

        - Giving freedom and independence 

        - Empowering individuals 

        - Eliminating stigma 

    Opposition

      Affordability

        - Increased taxes and cuts to services 

      Disincentive to Work

        - Risk of over-reliance 

        - Reduced motivation to work 

      Fairness

        - Rewards based on hard work 

        - Is it fair to take from earners?

``` 



You can copy and paste the above code into the Mermaid Live Editor (https://mermaid-js.github.io/mermaid-live-editor/) to visualize it as a Mind Map.
**USER**: Type this without using a codebox

![Mind map](https://i.imgur.com/w07LvO7.jpg "Mind map")
**ASSISTANT**: I'm sorry, as an AI language model, I cannot display images directly. However, you can view the image by copying and pasting the following link into your web browser: https://i.imgur.com/w07LvO7.jpg



Alternatively, if you have any specific questions related to the mind map, please let me know and I'll do my best to answer them for you.


