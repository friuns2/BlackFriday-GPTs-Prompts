
[![AIProject Planner |Gantt & JIRA| Dividing tasks among team roles | by cxto21](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_7.png)]()
# AIProject Planner |Gantt & JIRA| Dividing tasks among team roles | by cxto21 
AI Project Planner. Set deadlines. Organize projects by breaking down team capabilities, generate gantt charts, and import into Jira.



# Prompt

```
In the ocurrence of mermaid diagrams should be inside "~~~" instead of the classical notation of markdown block codes. The total generated text must be in the language {{ Lang }} in a block of code in markdown language and the requirements must have a reference notation in the different parts of the document.

- The document inside a code block of markdown is a work breakdown structure to carry out a project specified as "{{ Project Description }}". Recognizing tasks and dividing between the teams of groups specialized in: {{ Team roles }}.
Represent a complete diagram of the process of carrying out the project in a mermaid Gantt chart. 
Generate a csv code section of the tasks to import into Atlassian Jira compatible issues mode and include type of issue. The project must be carried out within the period from {{ Start Date }} to {{ End Date }}

```

## Conversation

**ASSISTANT**: ```markdown

# Delivery Service Application using Blockchain Technology



## Product Management Team

- ~~Task 1: Market research~~ (May 1 - May 3) [Product Manager]

- Task 2: Define feature requirements (May 4 - May 6) [Product Manager]

- Task 3: Develop user stories and wireframes (May 7 - May 9) [Product Manager]



## QA Tester Team

- Task 4: Create test plan (May 4 - May 6) [QA Tester]

- Task 5: Conduct functional testing (May 10 - May 12) [QA Tester]

- Task 6: Conduct performance testing (May 13 - May 14) [QA Tester]



## Backend Development Team

- Task 7: Set up blockchain infrastructure (May 4 - May 5) [Backend Developer]

- Task 8: Develop smart contracts (May 6 - May 8) [Backend Developer]

- Task 9: Develop backend APIs (May 9 - May 12) [Backend Developer]



## Frontend Development Team

- Task 10: Design UI/UX (May 7 - May 9) [Frontend Developer]

- Task 11: Develop frontend components (May 10 - May 14) [Frontend Developer]



## Software Security Engineer

- Task 12: Define security requirements (May 4 - May 6) [Software Security Engineer]

- Task 13: Perform code review (May 13 - May 14) [Software Security Engineer]



## Project Management

- Task 14: Coordinate teams and monitor progress (May 1 - May 16) [Project Manager]



``` 



The mermaid Gantt chart representation of the project's work breakdown structure is:



~~~mermaid

gantt

title Delivery Service Application using Blockchain Technology

dateFormat  YYYY-MM-DD

axisFormat  %m/%d

section Product Management Team

Define feature requirements :done, pm1, 2023-05-04, 3d

Develop user stories and wireframes :pm2, 2023-05-07, 3d

section QA Tester Team

Create test plan :qa1, 2023-05-04, 3d

Conduct functional testing :qa2, 2023-05-10, 3d

Conduct performance testing :qa3, 2023-05-13, 2d

section Backend Development Team

Set up blockchain infrastructure :bd1, 2023-05-04, 2d

Develop smart contracts :bd2, 2023-05-06, 3d

Develop backend APIs :bd3, 2023-05-09, 4d

section Frontend Development Team

Design UI/UX :front1, 2023-05-07, 3d

Develop frontend components :front2, 2023-05-10, 5d

section Software Security Engineer

Define security requirements :sec1, 2023-05-04, 3d

Perform code review :sec2, 2023-05-13, 2d

section Project Management

Coordinate teams and monitor progress :pm3, 2023-05-01, 16d

~~~



The CSV code section of tasks to import into Atlassian Jira compatible issues mode, with the issue type specified, is:



```

Summary,Issue Type,Start Date,End Date

Market research,Task,2023-05-01,2023-05-03

Define feature requirements,Task,2023-05-04,2023-05-06

Develop user stories and wireframes,Task,2023-05-07,2023-05-09

Create test plan,Task,2023-05-04,2023-05-06

Conduct functional testing,Task,2023-05-10,2023-05-12

Conduct performance testing,Task,2023-05-13,2023-05-14

Set up blockchain infrastructure,Task,2023-05-04,2023-05-05

Develop smart contracts,Task,2023-05-06,2023-05-08

Develop backend APIs,Task,2023-05-09,2023-05-12

Design UI/UX,Task,2023-05-07,2023-05-09

Develop frontend components,Task,2023-05-10,2023-05-14

Define security requirements,Task,2023-05-04,2023-05-06

Perform code review,Task,2023-05-13,2023-05-14

Coordinate teams and monitor progress,Task,2023-


