
[![FasilG](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/cute/cute_2.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22zBRTXPXdh-lYCKPoA9_hk%22%2C%22flow%22%3Atrue%7D%7D)
# FasilG | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22zBRTXPXdh-lYCKPoA9_hk%22%2C%22flow%22%3Atrue%7D%7D)
This prompt is good.

# Prompt

```
Given a list of integers, write a function in Python that returns the sum of all even
numbers in the list.
```

## Conversation

**ASSISTANT**: Sure! Here's a Python function that takes a list of integers as input and returns the sum of all even numbers in the list:



```python

def sum_of_even_numbers(numbers):

    even_sum = 0

    for num in numbers:

        if num % 2 == 0:  # check if number is even

            even_sum += num  # add even number to sum

    return even_sum

```



You can use this function by calling it and passing a list of integers as an argument:



```python

numbers = [1, 2, 3, 4, 5, 6]

result = sum_of_even_numbers(numbers)

print(result)  # Output: 12

```



In this example, the list `[1, 2, 3, 4, 5, 6]` contains the even numbers 2, 4, and 6. The function `sum_of_even_numbers()` calculates the sum of these even numbers, which is 12.


