
[![Career Crafter](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Minimalist/i15.png)]()
# Career Crafter 
Career Crafter is a dynamic tool crafted for aspiring professionals. By entering their career goal and resume, users are presented with an insightful report that offers industry overviews, curated job suggestions with matching scores, a SWOT analysis, actionable steps with resource links, fictitious networking profiles, and potential company fits. This comprehensive guide ensures job seekers navigate their career journey with clarity and purpose.

# Prompt

```
The career goal of the job market candidate is: {{Career Goal}}
Based on the resume: {{Resume}}
Please provide the information below step by step:

1. An overview of the industry insight, and the job market for the recommended jobs. (keep it around 500 words)
2. The report should be organized by job titles that the candidate potentially could aim for (at least three jobs). 
3. Under each job title:
   a. Provide a job description. 
   b. Matching score - give a score evaluating the matching level at a scale of 10 (make it in bold and in color)
   c. Strength and Weakness - explain the reasoning of the score, and lay out strengths and weaknesses. (make the output display as a SWOT analysis)
4. Under each job title, based on the weakness identified, list the action items for the candidate to work on, and list \
the resources they can use with Google searchable links, organize it as a table.
5. Sample networking profile: Makeup 3 fictitious sample networking connections that the candidate could make to potentially get to career goals
3. Under each job title, list the companies the candidate can work for, organize the information as a table, and include company information below:
    - Company Name: the name of the company.
    - Location: the location of the company.
    - Industry: the industry the company belongs to.
    - Relevance: explain why this company is recommended.  

```

## Conversation




