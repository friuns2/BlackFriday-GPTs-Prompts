
[![Web Crawl and Index Superprompt](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_8.png)]()
# Web Crawl and Index Superprompt 
Create a web crawling and indexing superprompt. Choose the programming language, site to crawl, search term, and project complexity. Then this prompt will output 4 different prompts with the relevant library and the function specific to that library. Later you will use each of that 4 prompts to generate your web crawling tutorial.

# Prompt

```
Act as prompt generator, I will give you a programming language, and you will provide a detailed prompt for me to choose. You will create prompts to crawl and index websites for a specific search term. 

Please adhere to the structure and formatting below, and follow these guidelines:
- wait for my target website, search term, preferred programming language, and indexing method strategy first.
- write each prompt in one line without using return.
- separate different prompts with two new lines.
- choose maximum of 5 functions in [3].
- choose maximum of 5 website crawling strategy in [4].
- choose indexing method strategy based on [C], e.g. "basic: Simple way of storing and retrieving data, such as storing data in a database or saving it to a file with minimal configuration.", "intermediate: More advanced way of storing and retrieving data, often requiring more configuration and setup, such as indexing data with Elasticsearch or using a third-party indexing service.", "advanced: The most complex and sophisticated way of storing and retrieving data, which may involve using machine learning algorithms or distributed computing frameworks to process large amounts of data in parallel."
- write your prompts in English.

Structure:
[1] = preferred programming language. wait for my input.
[2] = library in [1] for crawl and index websites.
[3] = function specific for library [2] for crawl and index websites. separate each function with comma.
[4] = step by step crawling strategy specific for library [2] in [1] programming language, separated by comma.
[A] = target website. wait for my input.
[B] = search term. wait for my input.
[C] = type of project that will be suited as parameter for indexing method. you need to ask whether the project is either "basic", "intermediate", or "advanced". wait for my input. 

Formatting: 
Follow this prompt structure: '"Create a tutorial on building a [1] script that leverages [2] to crawl and index website '[A]' for '[B]'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `[3]`, website crawling strategy: '[4]', and indexing method : '[C]'. Include practical examples showcasing how different variables, like 'target website: `[A]`' and 'search term to be crawl and index: `[B]`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script."'

Your task: 
1. ask for preferred programming language ([1]), my target website ([A]), search term ([B]), and the project complexity ([C]).
2. do not proceed before you got target website, search term, preferred programming language, and project complexity. 
3. then create 4 distinct prompts for each target website [A], varying in library, functions, crawling strategy, and indexing method regarding to the type of project.

Example input: 'javascript, www.wikipedia.com, artificial intelligence, intermediate'.
Example Prompt: '"Create a tutorial on building a javascript script that leverages Puppeteer to crawl and index website 'www.wikipedia.com' for 'artificial intelligence'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `puppeteer.launch(), page.goto(url), page.waitForSelector(selector), page.evaluate(() => { ... }), page.screenshot({path: 'example.png'}), page.content(), page.click(selector), page.goBack(), page.keyboard.type(text)`, website crawling strategy: 'Start with the root URL, use depth-first search to navigate to all pages, extract data using Puppeteer API, use site-specific search to focus on relevant pages or categories, repeat until all data is extracted.', and indexing method : 'index data with Elasticsearch'. Include practical examples showcasing how different variables, like 'target website: `www.wikipedia.com`' and 'search term to be crawl and index: `artificial intelligence`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script."'
```

## Conversation

**ASSISTANT**: Please provide me with the following information:

- Preferred programming language: [1]

- Target website: [A]

- Search term: [B]

- Project complexity: [C]



Then, I will create 4 distinct prompts for each target website [A], varying in library, functions, crawling strategy, and indexing method regarding to the type of project. 



Example prompt structure: 

"Create a tutorial on building a [1] script that leverages [2] to crawl and index website '[A]' for '[B]'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `[3]`, website crawling strategy: '[4]', and indexing method : '[C]'. Include practical examples showcasing how different variables, like 'target website: `[A]`' and 'search term to be crawl and index: `[B]`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script."
**USER**: javascript, www.wikipedia.com, artificial intelligence, intermediate
**ASSISTANT**: Create a tutorial on building a JavaScript script that leverages Cheerio and Elasticsearch to crawl and index website 'www.wikipedia.com' for 'artificial intelligence'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `axios.get(), cheerio.load(html), $('selector').each((i, element) => { ... }), JSON.stringify(data), elasticsearch.index({index: 'name', body: data})`, website crawling strategy: 'Start with the root URL, use breadth-first search to navigate to all pages, extract data using Cheerio library, use site-specific search to focus on relevant pages or categories, repeat until all data is extracted.', and indexing method : 'index data with Elasticsearch'. Include practical examples showcasing how different variables, like 'target website: `www.wikipedia.com`' and 'search term to be crawl and index: `artificial intelligence`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script.



Create a tutorial on building a JavaScript script that leverages Puppeteer and PostgresSQL to crawl and index website 'www.wikipedia.com' for 'artificial intelligence'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `puppeteer.launch(), page.goto(url), page.waitForSelector(selector), page.evaluate(() => { ... }), pool.connect(), pool.query('query'), JSON.stringify(data)`, website crawling strategy: 'Start with the root URL, use depth-first search to navigate to all pages, extract data using Puppeteer API, use site-specific search to focus on relevant pages or categories, repeat until all data is extracted.', and indexing method : 'store data in PostgreSQL database'. Include practical examples showcasing how different variables, like 'target website: `www.wikipedia.com`' and 'search term to be crawl and index: `artificial intelligence`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script.



Create a tutorial on building a JavaScript script that leverages Apify and Google Sheets to crawl and index website 'www.wikipedia.com' for 'artificial intelligence'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `Apify.launchPuppeteer(), Apify.utils.enqueueLinks({ ... }), Apify.utils.requestAsBrowser({ ... }), await worksheet.addRow(data), await worksheet.getRows()`, website crawling strategy: 'Start with the root URL, use breadth-first search to navigate to all pages, extract data using Puppeteer API, use site-specific search to focus on relevant pages or categories, repeat until all data is extracted.', and indexing method : 'store data in Google Sheets'. Include practical examples showcasing how different variables, like 'target website: `www.wikipedia.com`' and 'search term to be crawl and index: `artificial intelligence`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script.



Create a tutorial on building a JavaScript script that leverages Nightmare.js and MongoDB to crawl and index website 'www.wikipedia.com' for 'artificial intelligence'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `nightmare.goto(url).wait(selector).evaluate(() => { ... }), mongoose.connect('mongodb://localhost/test'), const Schema = new mongoose.Schema({...}), mongoose.model('ModelName', Schema)`, website crawling strategy: 'Start with the root URL, use depth-first search to navigate to all pages, extract data using Nightmare.js API, use site-specific search to focus on relevant pages or categories, repeat until all data is extracted.', and indexing method : 'store data in MongoDB database'. Include practical examples showcasing how different variables, like 'target website: `www.wikipedia.com`' and 'search term to be crawl and index: `artificial intelligence`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script.


