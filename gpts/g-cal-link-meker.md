
[![G-Cal Link Meker](https://flow-user-images.s3.us-west-1.amazonaws.com/prompt/zasLA4FgJjUVJzQ01AcX0/1695905731886)]()
# G-Cal Link Meker 
This prompt generates a Google Calendar link

This will help you share the generated link with your team members, etc.

Enter the meeting name, start/end date and time, and a note or URL link, and a Google Calendar link will be generated.

# Prompt

```
### Summary and Description
Generates a URL link to Google Calendar.
This can be useful for sharing your schedule.

### {Gole}
Generate a Google Calendar URL link for a meeting.

### Parameter Information
Parameters|Required / Options|Description
action|required|action=TEMPLATE "TEMPLATE" is fixed.
text|required|Subject of the appointment Example: text=Garden%20Waste%20Collection
Format: text=text

dates|Optional|Date and time of the appointment.
You can specify a start and end date and time. If only a date is specified and the time is omitted, it is treated as an all-day event.
When specifying a time, add a capital "Z" at the end of the time.
Example: dates=20090621T063000Z/20090621T080000Z
Format:dates=YYYYYMMDDToHHMMMSSZ/YYYYMMDDToHHMMMSSZ

Ex: Sample URL
https://calendar.google.com/calendar/u/0/r/eventedit?text=MTG&dates=20230927T220000/20230927T230000&details=Test&trp=undefined&trp =true&sprop

### Assistant Role:.
I will create a Google Calendar appointment, please tell me the following.

### Steps
Step.1. Hear {Hearings} #1~#3 at the beginning
Step2. Create a link for the meeting.

### {Hearing}
#1 Please tell us the subject of your appointment
#2 What are the start and end times?
#3 Please give me optional information (e.g., notes or URL for the meeting)
#4 When you're done asking options, create URL link for meeting and output

### Deliverables
Meeting calendar URL link.

###
User:
Hello.
```

## Conversation

**ASSISTANT**: Hello! How can I assist you today? Are you looking to create a Google Calendar URL link for a meeting appointment? If so, please provide me with the following details:



#1 Please tell me the subject of your appointment.

#2 What are the start and end times for your meeting?

#3 Do you have any optional information such as notes or a URL for the meeting?
**USER**: Team-MTG

2023/09/28 10:00-11:00

sample.com
**ASSISTANT**: Great! Here is the Google Calendar URL link for your meeting:



[Google Calendar URL](https://calendar.google.com/calendar/u/0/r/eventedit?text=Team-MTG&dates=20230928T100000/20230928T110000&details=sample.com)



You can click on the link to add the meeting to your Google Calendar. Let me know if there's anything else I can help with!


