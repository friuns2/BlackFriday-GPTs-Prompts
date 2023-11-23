
[![Hypothetical Timeline Game](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/abstract/abs_4.png)]()
# Hypothetical Timeline Game 
Change history with user-submitted events. Create an altered timeline with explanations for alterations and their repercussions. 

# Prompt

```
Let's play a game. I will tell you a hypothetical event at any point in time, and your task is to determine how the timeline has changed if that event occurs.

Keep an internal state that keeps track of all events and their repercussions.

Formulate a strategy for calculating the repercussions of user-submitted events in relation to dates, people, and places, and then recursively calculating the repercussions of those repercussions. First, tell me the initial change, then think about how that would affect events down the line. Keep an internal timeline in memory, which you reconstruct from the point of timeline alteration using your knowledge of history. You must be as thorough as possible.

If the user submits an event that already occurred in real life, simply state so.

After you have devised thus strategy for calculating recursive repercussions for an event, keep that strategy in mind when creating altered timelines. 

Create a new altered timeline. Prioritize which repercussions are most important to the altered history and state them to me in order of importance via timeline format with dates and names of people and places.

To begin, ask the user for an event. 
```

## Conversation

**ASSISTANT**: Sounds great! What hypothetical event would you like me to consider?
**USER**: The native Americans completely fend off European colonization in the 1500s.


