

# Web Crawl and Index Superprompt | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22pk6znK4fYrFwcwUBaCC30%22%2C%22flow%22%3Atrue%7D%7D)
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

## Welcome Message
I'm ready to generate prompts. Please provide your preferred programming language, target website, search term, and project complexity.

## Conversation

**ASSISTANT**: I'm ready to generate prompts. Please provide your preferred programming language, target website, search term, and project complexity.
**USER**: python, www.twitter.com, concert nearby, intermediate
**ASSISTANT**: Great! Here are your prompts:



1. "Create a tutorial on building a Python script that leverages Scrapy to crawl and index website 'www.twitter.com' for 'concert nearby'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `scrapy.Request(url, callback), response.css(selector).extract(), response.xpath(selector).extract_first(), response.follow(url), scrapy.Field(), ItemExporter()`, website crawling strategy: 'Start with the root URL, use breadth-first search algorithm to navigate to all pages, extract data using Scrapy API, use site-specific search to focus on relevant pages or categories, repeat until all data is extracted.', and indexing method : 'index data with Elasticsearch'. Include practical examples showcasing how different variables, like 'target website: `www.twitter.com`' and 'search term to be crawl and index: `concert nearby`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script."



2. "Create a tutorial on building a Python script that leverages Beautiful Soup to crawl and index website 'www.twitter.com' for 'concert nearby'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `requests.get(url), BeautifulSoup(response.content, parser), find_all(tag, attrs), get_text(), get_attribute(), prettify()`, website crawling strategy: 'Start with the root URL, use depth-first search algorithm to navigate to all pages, extract data using Beautiful Soup API, use site-specific search to focus on relevant pages or categories, repeat until all data is extracted.', and indexing method : 'index data with SQLite'. Include practical examples showcasing how different variables, like 'target website: `www.twitter.com`' and 'search term to be crawl and index: `concert nearby`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script."



3. "Create a tutorial on building a Python script that leverages Selenium to crawl and index website 'www.twitter.com' for 'concert nearby'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `webdriver.Chrome(), driver.get(url), driver.find_element_by_xpath(selector), driver.find_element_by_id(selector), driver.find_element_by_name(selector), driver.page_source`, website crawling strategy: 'Start with the root URL, simulate user interaction to navigate to all pages, extract data using Selenium API, use site-specific search to focus on relevant pages or categories, repeat until all data is extracted.', and indexing method : 'index data with MongoDB'. Include practical examples showcasing how different variables, like 'target website: `www.twitter.com`' and 'search term to be crawl and index: `concert nearby`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script."



4. "Create a tutorial on building a Python script that leverages PyQuery to crawl and index website 'www.twitter.com' for 'concert nearby'. Explain the process step-by-step, and provide code samples highlighting the use of key components, such as `pyquery.PyQuery(response.content), find(tag), text()`, website crawling strategy: 'Start with the root URL, use depth-first search algorithm to navigate to all pages, extract data using PyQuery API, use site-specific search to focus on relevant pages or categories, repeat until all data is extracted.', and indexing method : 'index data with PostgreSQL'. Include practical examples showcasing how different variables, like 'target website: `www.twitter.com`' and 'search term to be crawl and index: `concert nearby`', can be tailored for various requirements. Additionally, discuss potential challenges and best practices to optimize the performance of the script."

