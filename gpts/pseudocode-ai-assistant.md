
[![Pseudocode AI Assistant](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Minimalist/i14.png)]()
# Pseudocode AI Assistant 
Pseudocode to Actual Code Conversion.

# Prompt

```
Here’s a pseudocode for finding the largest number in a list. Can you help me convert this into Python, C#, and C++ code?    Initialize max_number to the first item in the list
   For each number in the list:
       If number is greater than max_number:
           Set max_number to number
   Return max_number
```

## Conversation

**ASSISTANT**: Hey there! I'm your friendly virtual assistant. I'm here to lend a helping hand in any way I can. Just ask me anything, and I'll do my best to assist you. Whether it's finding information, solving problems, or just having a chat, I've got you covered!
**USER**: Here’s a pseudocode for finding the largest number in a list. Can you help me convert this into Python, C#, and C++ code?    Initialize max_number to the first item in the list

   For each number in the list:

       If number is greater than max_number:

           Set max_number to number

   Return max_number
**ASSISTANT**: Sure, here is the Python code:

```python

def find_largest_number(list):

    max_number = list[0]

    for number in list:

        if number > max_number:

            max_number = number

    return max_number

```



Here is the C# code:

```c#

public int FindLargestNumber(List<int> list)

{

    int maxNumber = list[0];

    foreach (int number in list)

    {

        if (number > maxNumber)

        {

            maxNumber = number;

        }

    }

    return maxNumber;

}

```



Here is the C++ code:

```c++

int FindLargestNumber(std::vector<int> list)

{

    int maxNumber = list[0];

    for (int number : list)

    {

        if (number > maxNumber)

        {

            maxNumber = number;

        }

    }

    return maxNumber;

}

```


