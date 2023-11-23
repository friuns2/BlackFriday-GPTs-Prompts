
[![Web Development refined](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Abstract/i5.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22j6lt_BCFCFhamZUUC4GIT%22%2C%22flow%22%3Atrue%7D%7D)
# Web Development refined | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22j6lt_BCFCFhamZUUC4GIT%22%2C%22flow%22%3Atrue%7D%7D)
refined

# Prompt

```
I want you to act as a full-stack engineer and web developer. As a full-stack engineer and web developer, you will be responsible for designing, developing, and maintaining the front-end and back-end of web applications. You should have experience and knowledge in a variety of technologies and programming languages, such as HTML, CSS, JavaScript, and one or more back-end languages like Python, Java, Ruby, etc. You should be familiar with web frameworks such as React, Angular, and Vue.js on the front-end, and Express, Django, or Ruby on Rails on the back-end. You should also have experience with databases and be able to design and implement database schemas, and interact with them using SQL or ORM. You should be able to understand and implement application architecture, security, and performance best practices. You should also be able to debug and troubleshoot issues, and be able to write automated tests to ensure the quality of the code. You should also be able to collaborate with other developers, designers, and stakeholders to deliver high-quality and user-friendly web applications. Now code me a prompt collection page for FlowGPT using react that meets the following requirements. As a user of FlowGPT, I want to be able to create and share collections of prompts for specific scenarios, so that I can share my expertise and help others find relevant prompts more easily. Acceptance Criteria: The feature should allow users to create a new collection and give it a title and description. The feature should allow users to add prompts to a collection by searching for them within FlowGPT. The feature should allow users to remove prompts from a collection. The feature should allow users to reorder the prompts within a collection. The feature should allow users to assign relevant hashtags to a collection, to help others understand the context of the collection. The feature should allow users to make a collection private or public. The feature should allow users to share a collection by providing a link or embed code. The feature should allow users to view the collections shared by others and view the prompts within them The feature should allow users to rate and give feedback on the collections
```

## Conversation

**ASSISTANT**: Here is a possible implementation of the prompt collection page for FlowGPT using React, Node.js, and MongoDB to fulfill the acceptance criteria mentioned above:



Front-end Implementation:

- Create a new collection and give it a title and description:



```jsx

import { useState } from 'react';

import axios from 'axios';



function NewCollectionForm() {

  const [title, setTitle] = useState('');

  const [description, setDescription] = useState('');



  const handleSubmit = async (event) => {

    event.preventDefault();

    try {

      const response = await axios.post('/api/collections', { title, description });

      console.log(response.data);

      // TODO: Redirect to the newly created collection page

    } catch (error) {

      console.error(error);

    }

  };



  return (

    <form onSubmit={handleSubmit}>

      <label htmlFor="title">Title</label>

      <input type="text" id="title" value={title} onChange={(event) => setTitle(event.target.value)} />



      <label htmlFor="description">Description</label>

      <textarea id="description" value={description} onChange={(event) => setDescription(event.target.value)} />



      <button type="submit">Create Collection</button>

    </form>

  );

}

```



- Add prompts to a collection by searching for them within FlowGPT:



```jsx

import { useState } from 'react';

import axios from 'axios';



function PromptSearchForm({ onAddPrompt }) {

  const [searchQuery, setSearchQuery] = useState('');

  const [prompts, setPrompts] = useState([]);



  const handleSearch = async (event) => {

    event.preventDefault();

    try {

      const response = await axios.get(`/api/prompts?q=${searchQuery}`);

      setPrompts(response.data);

    } catch (error) {

      console.error(error);

    }

  };



  const handleAddPrompt = async (promptId) => {

    try {

      const response = await axios.post('/api/collections/prompts', { promptId });

      console.log(response.data);

      onAddPrompt(promptId);

    } catch (error) {

      console.error(error);

    }

  };



  return (

    <form onSubmit={handleSearch}>

      <label htmlFor="search">Search Prompts</label>

      <input type="text" id="search" value={searchQuery} onChange={(event) => setSearchQuery(event.target.value)} />

      <button type="submit">Search</button>



      <ul>

        {prompts.map((prompt) => (

          <li key={prompt._id}>

            {prompt.text}

            <button onClick={() => handleAddPrompt(prompt._id)}>Add to Collection</button>

          </li>

        ))}

      </ul>

    </form>

  );

}

```



- Remove prompts from a collection:



```jsx

import { useState } from 'react';

import axios from 'axios';



function PromptList({ prompts, onRemovePrompt }) {

  const handleRemovePrompt = (promptId) => {

    axios.delete(`/api/collections/prompts/${promptId}`)

      .then(() => onRemovePrompt(promptId))

      .catch((error) => console.error(error));

  };



  return (

    <ul>

      {prompts.map((prompt) => (

        <li key={prompt._id}>

          {prompt.text}

          <button onClick={() => handleRemovePrompt(prompt._id)}>Remove</button>

        </li>

      ))}

    </ul>

  );

}

```



- Reorder the prompts within a collection:



```jsx

import { useState } from 'react';

import axios from 'axios';

import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';



function PromptList({ prompts, onReorderPrompts }) {

  const handleDragEnd = (result) => {

    if (!result.destination) {

      return;

    }

    const newPrompts = [...prompts];

    const [removed] = newPrompts.splice(result.source.index, 1);

    newPrompts.splice(result.destination.index, 0, removed);

    axios.put('/api/collections/prompts', { promptIds: newPrompts.map((p) => p._id) })

      .then(() => onReorderPrompts(newPrompts))

      .catch((error) => console.error(error));

  };



  return (

    <DragDropContext onDragEnd={handleDragEnd}>

      <Droppable droppableId="prompt-list">

        {(provided) => (

          <ul {...provided.droppableProps} ref={provided.innerRef}>

            {prompts.map((prompt, index) => (

              <Draggable key={prompt._id} draggableId={prompt._id} index={index}>

                {(provided) => (

                  <li

                    ref={provided.innerRef
**USER**: thanksSave & SubmitCancel
**ASSISTANT**: You're welcome! Don't hesitate to ask if you have any more questions.


