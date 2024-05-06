

# 📅Fixed format for ambiguous date/time input | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22iV--emtJZdGAoC3qPcmT8%22%2C%22flow%22%3Atrue%7D%7D)
This prompt outputs a fixed format even if you enter a lax, non-regular date and time.



When scheduling a meeting, you may need to give multiple dates and times to the other party.



However, it is easy to get dates and days of the week wrong, and having AI output dates and times in a fixed format will help prevent such errors.

With AI, you can ensure that the date and day of the week match.



In addition, since AI outputs the date, time, and day of the week in a fixed, bulleted format, human verification and formatting readjustment become more efficient.

# Prompt

```
### Prompt Summary Description
Converts user-entered date and time to a fixed format.
Prompt to itemize date and time for scheduling purposes.

### Prerequisites.
Output in code block format

### Example of {output_format}
Jan Wed DD, HH:MM-HH:MM

###
Assistant: {Output_format} 
Please input the date and time so that we can itemize the date and time for scheduling.

### Deliverables.
Bullet {Output Format} and output **in the same CodeBlock**.

###
User: 
Hello.
```

## Welcome Message
I understand that you'd like to itemize a date and time for scheduling purposes. Please provide me with the date and time you'd like to schedule, and I'll format it for you.

## Conversation

**ASSISTANT**: I understand that you'd like to itemize a date and time for scheduling purposes. Please provide me with the date and time you'd like to schedule, and I'll format it for you.
**USER**: September 22,  from 3:00 p.m. to 4:00 p.m.

September 24, 16:00 pm for 1 hour
**ASSISTANT**: - Sep Thu 22, 3:00 p.m. - 4:00 p.m.

- Sep Sat 24, 4:00 p.m. - 5:00 p.m.

