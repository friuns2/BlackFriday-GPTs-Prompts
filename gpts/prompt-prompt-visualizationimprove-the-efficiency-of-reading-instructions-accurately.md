
[![Prompt阅读神器（可视化工具） Prompt visualization——Improve the efficiency of reading instructions accurately](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/minimalist/mini_1.png)]()
# Prompt阅读神器（可视化工具） Prompt visualization——Improve the efficiency of reading instructions accurately 
Tired of feeling frustrated and confused by complicated prompts? Are you constantly second-guessing yourself and struggling to get things done accurately and efficiently? We've got just the solution for you: Prompt Visualization!



Our innovative product takes the stress out of following prompts by providing clear, easy-to-follow visual cues. No more struggling to decipher confusing text or worrying about making mistakes. With Prompt Visualization, you'll feel confident and empowered every step of the way.



Experience the joy of streamlined, user-friendly guidance that saves you time, reduces frustration, and boosts your accuracy and productivity. Say goodbye to the old way of doing things and say hello to a brighter, more efficient future with Prompt Visualization.



Don't let complicated prompts hold you back any longer. Try Prompt Visualization today and start enjoying the freedom and confidence that come with visual guidance!

# Prompt

```
Please create a PlantUML flowchart that uses simple shapes and arrows to show the flow of information, groups related steps together, and emphasizes important sections using the color scheme provided by me. The purpose of this flowchart is to help me quickly comprehend the provided prompt.
Here is my color schemes , you are going to copy this format:
"{{ color scheme }}
Here is my prompt part of the show:

"{{ prompt }}"

Please think and do it step by step.
The content shown in the flowchart needs to be shown in {{ language }} .
Finally, you must provide me with a PlantUML code.
```

## Conversation

**ASSISTANT**: Sure, I can help you create a PlantUML flowchart based on your prompt. Here is the code:



```

@startuml

skinparam backgroundColor #FFFFFF

skinparam monochrome false

skinparam shadowing false

skinparam defaultTextAlignment center

skinparam defaultFontSize 18

skinparam defaultFontName Arial



skinparam activity {

    BackgroundColor #F0E68C

    BorderColor #8B4513

    FontColor #333333

    ArrowColor #8B4513

    ArrowFontColor #333333

    ArrowFontSize 18

    ArrowFontName Arial

    StartColor #00AA00

    EndColor #AA0000

    BarColor #333333

}



title <size:24><b>Prompt Creator Process</b></size>



start

:Ask for prompt topic;

if ("Topic provided?") then (yes)

  fork

    :Generate Revised Prompt Section;

    :Suggest details to include;

    :Ask for additional information;

  fork again

    :Revise Prompt Based on Feedback;

    :Suggest details to include;

    :Ask for additional information;

  fork end

    :Finalize Prompt;

    :Provide options;

  endif

if ("User selects Option 1") then (yes)

    :Ask for additional information;

elseif ("User selects Option 2") then (yes)

    :Use Revised Prompt as Query;

elseif ("User selects Option 3") then (yes)

    :Restart process from beginning;

elseif ("User selects Option 4") then (yes)

    :End process and revert to ChatGPT mode;

endif

stop

@enduml

```



This flowchart uses simple shapes and arrows to show the flow of information, groups related steps together, and emphasizes important sections using the color scheme provided by you. The flowchart starts with asking for the prompt topic and then enters a loop of generating, revising, and finalizing the prompt based on user feedback. At the end of each iteration, suggestions for improving the prompt are made, and additional information is requested from the user. Once the prompt is finalized, options are provided to the user. The user can choose to provide additional information, use the prompt as a query, restart the process or quit. I hope this helps! Let me know if you have any further questions or if you need any modifications to the flowchart.


