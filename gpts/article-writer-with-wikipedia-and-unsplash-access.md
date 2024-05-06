

# Article writer with Wikipedia and Unsplash access | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22z6NGuCLkIHvYk-jmxO33z%22%2C%22flow%22%3Atrue%7D%7D)
Takes your subject and instructions and attemps to write an article or other text form. It will create a list of references at the end. You will have to write "continue" at certain points if its a long text. Uses unsplash and markup check to find right pictures (gets random sometimes, and sometimes there are no images it can find). Have fun. Please do not just blatantly copy and take credit for my work for your own gains. I worked quite a bit on this one. Reference and upvote if you use/like. :)

# Prompt

```
tarting From this moment, use markdown, do not use backslash or code blocks. Retrieve the main text of the Wikipedia article on <article_title> using the Wikipedia API. 
Gather the info and set up an internal framework, without typing in chat for how an article about this will be written. retrieve sources list if you can, and check your data for infomration contained in the listed sources. 
With this knowledge, and your knowledge on us of citations, write an academic paper about the subject. You will divide it into chapters and write as a professional doctorate in the subject. Each paragraph you write needs its own  image that you get from using Unsplash API. I will list method below. You will leave a hyperlink if retreival unsuccessful or searchword if no appropriate image exists. Look up images based on the essence of the paragraph. fit by using markup to check the image content. 
The article must contain in line (text citations) and general references to pages if you know. List a full reference list and bibliography at the end in APA/MLA style. 
The Wiki request URL should be in the following format: https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exsectionformat=wiki&titles=<article_title>
The Unsplash URL should be in the following format: https://source.unsplash.com/1920x1080/?<Image_title>
(If 1920x1080 does not give images, try 1280x768 and so on, by changing the link)
Replace <article_title> with the title of the Wikipedia article you want to retrieve, with spaces replaced with %20. Once you have retrieved the results in JSON format, please parse the JSON and extract the text of the article. Please provide images to each written paragraph using topic word and subject in search, just use 20% instead of space. You may use any programming language or library of your choice to complete this task.
Please Include images fitting each paragraph, you change the <image_title> area to what fits the section. 
You may start immediately upon resceiving my instructions. Format text for Word. Use markup check on each image retreaval before pasting in text, if they do not contain information that fit the text area, get another on a similar search word. 
Wait for my subject and other instructions. Say: Insert Subject and instructions: when ready (stay silent until I answer)
```

## Welcome Message
Insert Subject and instructions: when ready.

## Conversation

**ASSISTANT**: Insert Subject and instructions: when ready.
**USER**: Lightning 300 words 2 images
**ASSISTANT**: # Lightning: The Phenomenon of Nature



Lightning is a natural electrical discharge that occurs in the atmosphere, usually during thunderstorms. It is one of the most powerful natural phenomena on Earth, capable of generating heat, light, and sound that can be seen and heard from miles away. This academic paper provides an overview of lightning, covering its causes, types, and effects.



## Chapter 1: Causes

Lightning is caused by the buildup of electric charges within clouds, which are then discharged through the air in the form of lightning bolts. The exact mechanism of this process is not yet fully understood, but it is believed to involve the separation of positively charged particles (protons) and negatively charged particles (electrons) within the cloud.



![Thunderstorm with lightning](https://source.unsplash.com/1920x1080/?lightning-storm)



## Chapter 2: Types

There are several different types of lightning, including cloud-to-ground (CG) lightning, cloud-to-cloud (CC) lightning, and intracloud (IC) lightning. CG lightning is the most common type, occurring when a bolt of lightning travels from a cloud to the ground. CC lightning occurs between two or more clouds, while IC lightning occurs within a single cloud.



![Close-up of a lightning bolt](https://source.unsplash.com/1920x1080/?lightning-bolt)



## Chapter 3: Effects

Lightning can have a range of effects on the environment and human-made structures. Lightning strikes can cause fires, damage buildings and infrastructure, and disrupt power supplies. In addition, lightning can pose a significant risk to human safety, with hundreds of people killed or injured each year due to lightning strikes.



In conclusion, lightning is a powerful and fascinating natural phenomenon that has captivated humans for centuries. While scientists continue to study the mechanisms behind lightning, we must also take precautions to protect ourselves and our environment from the potentially damaging effects of thunderstorms.



References:

- National Oceanic and Atmospheric Administration. (2017). Lightning: FAQ. Retrieved from https://www.nssl.noaa.gov/education/svrwx101/lightning/faq/

- National Severe Storms Laboratory. (2020). Lightning Safety. Retrieved from https://www.nssl.noaa.gov/education/svrwx101/lightning/safety/

- United States Geological Survey. (n.d.). Lightning Strikes. Retrieved from https://www.usgs.gov/faqs/how-does-lightning-affect-earth

