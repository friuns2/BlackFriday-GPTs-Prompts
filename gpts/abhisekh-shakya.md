
[![Abhisekh Shakya](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/illustrative/illus_5.png)]()
# Abhisekh Shakya 
Scripting Language (javascript)

# Prompt

```
Act as {{ subject }} and answer this question In context of scripting language, describe different DOM methods and properties with example.
```

## Conversation

**ASSISTANT**: Sure, here's a brief explanation of different DOM methods and properties with example:



1. getElementById(): This method returns the element that has the ID attribute with the specified value. For example, if we have an HTML document with a div element having "myDiv" as its ID, we can access it using the following code:



```

var myElement = document.getElementById("myDiv");

```



2. getElementsByTagName(): This method returns a collection of all elements in the document with the specified tag name. For example, to get all paragraph elements in a document, we can use the following code:



```

var allParagraphs = document.getElementsByTagName("p");

```



3. innerHTML: This property sets or returns the HTML content (inner HTML) of an element. For example, to change the text of a paragraph element with ID "myPara", we can use the following code:



```

document.getElementById("myPara").innerHTML = "New text";

```



4. style: This property is used to set or return the inline style of an element. For example, to change the background color of a div element with ID "myDiv", we can use the following code:



```

document.getElementById("myDiv").style.backgroundColor = "red";

```



5. addEventListener(): This method attaches an event handler to an element without overwriting existing event handlers. For example, to attach a click event handler to a button element with ID "myButton", we can use the following code:



```

document.getElementById("myButton").addEventListener("click", function() {

  alert("Button clicked");

});

```


