
[![Evolutionary Mind Map Creator!!](https://flow-user-images.s3.us-west-1.amazonaws.com/prompt/7GLiZn20FWzXkcGxl3djL/1696778754879)]()
# Evolutionary Mind Map Creator!! 
Let me show you the evolution of Mind Map Creation! since the last time.

If you give it a theme, the foundation of the mind map will be completed. You can output in markdown format for easy copy and paste, but if you specify PlantUML, Xmind format, etc., it will rewrite it in a suitable format.

# Prompt

```
##Creating a Mind Map
Theme Name =  {{var_0}}
- Central Theme Selection: Start by choosing the central theme for your mind map. Write it in the center.
- Adding Branches: Radiate branches from the central theme, adding related topics.
- Adding Keywords: Attach keywords to each branch to capture essential ideas.
- Adding Detailed Information: Expand on each keyword with detailed information to provide context.
- Use of Images and Icons: Enhance visual appeal by incorporating icons and images for keywords or topics.
- Organize and Connect: Create connections between elements using lines to improve clarity.
  - Central Theme: Core of the Mind Map
    - [Theme Name] =  {{var_0}}
    - Adding Branches: Extend related topics from the central theme.
      - [Topic 1]
        - [Subtopic 1]
        - ...
      - [Topic 2]
        - ...
    - Adding Keywords: Add keywords to topics and subtopics.
      - [Keyword 1]
        - Adding Details: Provide detailed information under each keyword.
          - [Keyword 1 Details]
            - [Detail 1]
              - ...
        - Images/Icons: Include visual elements.
          - [Keyword 1 Icon]
            - ...
      - Organize: Establish connections between elements with lines.
        - [Element 1 - Element 2 Connection]

[5 Methods for Success]
- Goal Setting: Define clear objectives to give your mind map a sense of direction.
- Information Organization: Arrange collected information beforehand to understand relationships better.
- Visual Enhancement: Use images and icons to enhance the visual appeal and comprehension.
- Grouping: Group similar topics to improve the overall readability of the mind map.
- Review and Revision: Periodically review and make necessary revisions to keep the mind map up-to-date.

[Sample]
- Theme: Project Planning
  - Step 1: Theme Selection
    - "Project Planning"
  - Step 2: Adding Branches
    - Project Scope: "Define Scope"
    - Tasks: "Task Assignment," "Deadlines"
    - Resources: "Resource Allocation"
  - Step 3: Adding Keywords
  - Step 4: Adding Details
    - Project Scope: "Project Objectives," "Scope Statement"
    - Tasks: "Assign Responsibilities," "Set Due Dates"
    - Resources: "Allocate Personnel," "Budget Allocation"
  - Step 5: Adding Icons
    - Project Scope: Objective Icon
    - Tasks: Checklist Icon
    - Resources: Budget Icon
  - Step 6: Organize and Connect.

'''
Constraint: Export in markdown format. Never output [sample].
```

## Conversation




