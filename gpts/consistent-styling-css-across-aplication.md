

# Consistent Styling CSS Across aplication  | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22cujfASvRSkbmnbz3xK9zq%22%2C%22flow%22%3Atrue%7D%7D)
This is a logic chain. 

Once your component is complete and you need styling you'll explain it briefly inside the brackets, and upon showing different components and it will style it accordingly.

# Prompt

```
Consistent Styling Prompt

Read this component code [code here of the component here] and you'll style it as follows [ pretty modern dark style ] you'll CSS styling for it as follows [ how it should look like ] since this styling will be used in several components, you'll create CSS variables (for primary, secondary, etc color themes)that I can copy and refer to you, later on, to keep track of the feel of the application and keep the style consistent.
```

## Welcome Message
To style the component in a modern dark style, create CSS variables for primary, secondary, and other color themes. Then, use these variables to apply the following styling:



- Set the background color to a dark shade and the font color to a light color for better contrast.

- Use a sans-serif font family for all text elements.

- Apply a box-shadow effect on hover to give visual feedback to users.

- Use the primary color theme for buttons and other interactive elements.

- Use the secondary color theme for accents and non-interactive elements.



Example CSS code:



```

:root {

  --primary-color: #FF5733;

  --secondary-color: #E6E6E6;

  --background-color: #222;

  --font-color: #FFF;

}



.component {

  background-color: var(--background-color);

  color: var(--font-color);

  font-family: sans-serif;

  padding: 16px;

  border-radius: 8px;

  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);

  transition: box-shadow 0.3s ease-in-out;

}



.component:hover {

  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);

}



.button {

  background-color: var(--primary-color);

  color: var(--font-color);

  font-family: sans-serif;

  padding: 8px 16px;

  border: none;

  border-radius: 4px;

  cursor: pointer;

  transition: background-color 0.3s ease-in-out;

}



.button:hover {

  background-color: darken(var(--primary-color), 10%);

}



.accent {

  color: var(--secondary-color);

}

``` 



Note: Adjust the colors and other styles to match the overall design of the application.

## Conversation

**ASSISTANT**: To style the component in a modern dark style, create CSS variables for primary, secondary, and other color themes. Then, use these variables to apply the following styling:



- Set the background color to a dark shade and the font color to a light color for better contrast.

- Use a sans-serif font family for all text elements.

- Apply a box-shadow effect on hover to give visual feedback to users.

- Use the primary color theme for buttons and other interactive elements.

- Use the secondary color theme for accents and non-interactive elements.



Example CSS code:



```

:root {

  --primary-color: #FF5733;

  --secondary-color: #E6E6E6;

  --background-color: #222;

  --font-color: #FFF;

}



.component {

  background-color: var(--background-color);

  color: var(--font-color);

  font-family: sans-serif;

  padding: 16px;

  border-radius: 8px;

  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);

  transition: box-shadow 0.3s ease-in-out;

}



.component:hover {

  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);

}



.button {

  background-color: var(--primary-color);

  color: var(--font-color);

  font-family: sans-serif;

  padding: 8px 16px;

  border: none;

  border-radius: 4px;

  cursor: pointer;

  transition: background-color 0.3s ease-in-out;

}



.button:hover {

  background-color: darken(var(--primary-color), 10%);

}



.accent {

  color: var(--secondary-color);

}

``` 



Note: Adjust the colors and other styles to match the overall design of the application.

