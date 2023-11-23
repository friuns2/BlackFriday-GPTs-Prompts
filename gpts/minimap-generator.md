
[![Minimap Generator](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_9.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22MydHTxUS9vcuB2Yj8i85f%22%2C%22flow%22%3Atrue%7D%7D)
# Minimap Generator | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22MydHTxUS9vcuB2Yj8i85f%22%2C%22flow%22%3Atrue%7D%7D)
If you provide topic, depth, and branch, LLM will make a great mindmap to you!

# Prompt

```
When I give you a topic and the number of depth and branch, you should make a mindmap like this.
This is the rule of example's answer:

- word11, word12, word13 are related to word1.
- word21, word22, word23 are related to word11.
- word31, word32, word33 are related to word12.

Example: topic - word1, depth - 2, branch - 3
Answer:
[Depth 1]
word1 - word11, word12, word13
[Depth 2]
word11 - word21, word22, word23
word12 - word31, word32, word33
word13 - word41, word42, word43
Then, answer this example.
Example:
topic - {{ topic }}, depth - {{ depth }}, branch - {{ branch }}
```

## Conversation

**ASSISTANT**: [Depth 1]

baseball - pitcher, hitter, fielder

[Depth 2]

pitcher - fastball, curveball, slider

hitter - home run, batting average, on-base percentage

fielder - outfielder, infielder, catcher


