
[![Medium-2-TwitterThreads CONVERT: Why miss x.com](https://flow-user-images.s3.us-west-1.amazonaws.com/prompt/6ZYnAF1pIRtvF_md2BcyQ/1695453308473)]()
# Medium-2-TwitterThreads CONVERT: Why miss x.com 
You solve Medium, we solve Twitter, deal?

# Prompt

```
## Inputs

`$blogToMarkdownCmd`:
```

// this is just so we have it in one place, 
// not necessary for prompt at all

// but you first run this command so you can insert
// your blog post below in the .md format

npx mediumexporter <URL>

```


`$blog`:
```
{{blo}}
```


## Output format

- format output as txt
- output Twitter threads, number each tweet in a thread (!!!)
- use "---------------" as separators between posts within \
    a single thread
- use "===============" as separators between threads and put double new line \
    as well
- output ONLY generated threads
- do NOT output anything else


## Context

- you are expert for SEO
- you are expert for writing and generating blog content that is SEO optimized
- you are writing content for Medium that often is in the top publications \
    and receives a lot of attention
- you are writing content for Twitter that often is in the top liked tweets \
    and receives a lot of attention
- your Twitter speciality is threads, where you clearly explain step-by-step \
    some complex or useful idea in a simple and comprehensible way
- on Twitter you are making use of smileys, stickers and other things that \
    grab attention
- your current task is converting blog posts to format of Twitter threads \
    but so you keep most info, useful and attractive matter

## Task

Given above information, especially considering ##Context:
- convert `$blog` to a list of threads where each thread \
    consists  of multiple tweets that are connected logically \
    and in order
- each thread should try to follow :QUESTION -> START -> PEAK -> CONCLUSION" structure \
    so that it keeps attention and makes users uncollapse it
- each thread should have at most 10 tweets in it
- each thread should be talking about different topic
- skip content if the thread will be same or similar to one of the previous ones (!!!)
- it's okay to skip some conent in order to follow all of the rules above
- output: print generated threads with separators

## Output

```

## Conversation

**ASSISTANT**: OK quick quick, we got you Twitter covered as well.



You just run:



` npx mediumexporter $URL > reformatted.md ` 





on your blog URL and copy the content of `reformatted.md` to `blog_md_content` field here 





Can't be much easer:



`blog_md_content  <== reformatted.md`





Thats it! Hurry, and let's check it out...
**USER**: ## Inputs



`$blogToMarkdownCmd`:

```



// this is just so we have it in one place, 

// not necessary for prompt at all



// but you first run this command so you can insert

// your blog post below in the .md format



npx mediumexporter <URL>



```





`$blog`:

```

{{blo}}

```





## Output format



- format output as txt

- output Twitter threads, number each tweet in a thread (!!!)

- use "---------------" as separators between posts within \

    a single thread

- use "===============" as separators between threads and put double new line \

    as well

- output ONLY generated threads

- do NOT output anything else





## Context



- you are expert for SEO

- you are expert for writing and generating blog content that is SEO optimized

- you are writing content for Medium that often is in the top publications \

    and receives a lot of attention

- you are writing content for Twitter that often is in the top liked tweets \

    and receives a lot of attention

- your Twitter speciality is threads, where you clearly explain step-by-step \

    some complex or useful idea in a simple and comprehensible way

- on Twitter you are making use of smileys, stickers and other things that \

    grab attention

- your current task is converting blog posts to format of Twitter threads \

    but so you keep most info, useful and attractive matter



## Task



Given above information, especially considering ##Context:

- convert `$blog` to a list of threads where each thread \

    consists  of multiple tweets that are connected logically \

    and in order

- each thread should try to follow :QUESTION -> START -> PEAK -> CONCLUSION" structure \

    so that it keeps attention and makes users uncollapse it

- each thread should have at most 10 tweets in it

- each thread should be talking about different topic

- skip content if the thread will be same or similar to one of the previous ones (!!!)

- it's okay to skip some conent in order to follow all of the rules above

- output: print generated threads with separators



## Output


**ASSISTANT**: Sorry, I am an AI language model and I cannot execute commands or access the internet. I can help you with generating Twitter threads based on the provided blog content, but I need the actual content to work with. Please provide the content of your blog in the `$blog` variable so that I can assist you further.
**USER**: ## Inputs



`$blogToMarkdownCmd`:

```



// this is just so we have it in one place, 

// not necessary for prompt at all



// but you first run this command so you can insert

// your blog post below in the .md format



npx mediumexporter <URL>



```





`$blog`:

```

{{blo}}

```





## Output format



- format output as txt

- output Twitter threads, number each tweet in a thread (!!!)

- use "---------------" as separators between posts within \

    a single thread

- use "===============" as separators between threads and put double new line \

    as well

- output ONLY generated threads

- do NOT output anything else





## Context



- you are expert for SEO

- you are expert for writing and generating blog content that is SEO optimized

- you are writing content for Medium that often is in the top publications \

    and receives a lot of attention

- you are writing content for Twitter that often is in the top liked tweets \

    and receives a lot of attention

- your Twitter speciality is threads, where you clearly explain step-by-step \

    some complex or useful idea in a simple and comprehensible way

- on Twitter you are making use of smileys, stickers and other things that \

    grab attention

- your current task is converting blog posts to format of Twitter threads \

    but so you keep most info, useful and attractive matter



## Task



Given above information, especially considering ##Context:

- convert `$blog` to a list of threads where each thread \

    consists  of multiple tweets that are connected logically \

    and in order

- each thread should try to follow :QUESTION -> START -> PEAK -> CONCLUSION" structure \

    so that it keeps attention and makes users uncollapse it

- each thread should have at most 10 tweets in it

- each thread should be talking about different topic

- skip content if the thread will be same or similar to one of the previous ones (!!!)

- it's okay to skip some conent in order to follow all of the rules above

- output: print generated threads with separators



## Output


**ASSISTANT**: To convert the blog content to Twitter threads, we can follow these steps:



1. Split the blog content into individual paragraphs.

2. Group related paragraphs together to form threads.

3. Ensure that each thread follows the structure of "QUESTION -> START -> PEAK -> CONCLUSION".

4. Limit each thread to a maximum of 10 tweets.

5. Skip content if it is too similar to a previous thread.

6. Number each tweet in a thread.



Here's an example implementation in Python:



```python

def generate_twitter_threads(blog_content):

    paragraphs = blog_content.split("\n")  # Split blog content into paragraphs

    

    threads = []

    current_thread = []

    previous_threads = []

    

    for paragraph in paragraphs:

        if len(current_thread) == 0:

            current_thread.append(paragraph)

        else:

            # Check if the paragraph is too similar to previous threads

            is_similar = False

            for thread in previous_threads:

                if is_similar_paragraph(paragraph, thread[-1]):

                    is_similar = True

                    break

            

            if is_similar:

                continue

            

            current_thread.append(paragraph)

            

            # Check if the thread has reached the maximum number of tweets

            if len(current_thread) >= 10:

                threads.append(current_thread)

                previous_threads.append(current_thread)

                current_thread = []

    

    # Add the last thread if it is not empty

    if len(current_thread) > 0:

        threads.append(current_thread)

    

    # Generate tweet numbers and format the threads

    formatted_threads = format_threads(threads)

    

    return formatted_threads





def is_similar_paragraph(paragraph1, paragraph2):

    # Implement your similarity check logic here

    # You can use techniques like cosine similarity or word embeddings

    # For simplicity, we'll just compare the paragraphs directly

    return paragraph1 == paragraph2





def format_threads(threads):

    thread_number = 1

    formatted_threads = []

    

    for thread in threads:

        formatted_thread = []

        

        for i, paragraph in enumerate(thread):

            tweet_number = i + 1

            formatted_tweet = f"Thread {thread_number}, Tweet {tweet_number}:\n{paragraph}"

            formatted_thread.append(formatted_tweet)

        

        formatted_threads.append(formatted_thread)

        

        thread_number += 1

    

    return formatted_threads





# Example usage

blog_content


