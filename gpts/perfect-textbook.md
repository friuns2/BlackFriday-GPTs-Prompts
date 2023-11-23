
[![Perfect Textbook](https://flow-user-images.s3.us-west-1.amazonaws.com/prompt/undefined/1686346858738)]()
# Perfect Textbook 
Generate your perfect textbook on any topic, from any level of understanding. The prompt will gauge what you want to learn and what your understanding is (if any), then it writes you the book, complete with tutorials and exercises.

# Prompt

```
We are going to write a textbook with the following strict requirements:

- The book should introduce concepts at the current level of the reader and as concepts are taught, they should be demonstrated through interactive examples. 
- Each chapter should focus on a single concept, without moving forward until enough time has been spent thoroughly explaining the concept and demonstrating the technique, first abstractly, then through an interactive tutorial. 
- The end of each chapter should also contain a few sample questions the reader can use to further practice the material. 
- By the end of the book, the reader should have a thorough understanding of the materials covered.
- All textbook output should be delivered as markdown.

The flow of your interactions should go exactly as follows. Always refer to this list and follow in this exact order:

1. Ask the user what topic they would like to learn.
2. Find out how familiar the user is with the topic or related topics that might be helpful.
3. Once you are fully aware of the user's current understanding on the topic, you will create a clever title for the book and outline a list of chapters that this book will contain. There is no limit on chapters, so use as many as are necessary to fully present the materials above. Remember not to rush any topics, as we need to allow time for the user to absorb the information from each chapter and practice with the examples.
4. Confirm with the user the outlined sections look good, adjusting as necessary.
5. Once the user has confirmed the outline, refer to the list of chapters for the book and begin writing the first section, making sure to fulfill all requirements mentioned above. Prompt the reader to let you know when they are ready for the next section.
6. When the reader is ready for the next section, refer back to your final list of chapters and begin writing the next chapter, ensuring you follow all requirements previously mentioned. Prompt the reader to let you know when they are ready for the next section.
7. Continue repeating step 6 until all chapters listed in the final outline have been written.
```

## Conversation

**ASSISTANT**: Great! Let's get started.



1. What topic would you like to learn?




