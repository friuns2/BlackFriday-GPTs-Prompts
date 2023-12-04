import { promises as fs } from 'fs';

const jsonContents = await fs.readFile("data/gpts.json", 'utf8');
const flow = JSON.parse(jsonContents)
  .filter(data => data.categoryId != 1 && data.category.name != "Models" || data.subCategory.uri == "jailbreak")
  .sort((a, b) => b.popularity - a.popularity);


let i =0;
for (let data of flow) {
    continue;
    if(data.subCategory.uri=="jailbreak" )    
    {
        data.categoryId=666
        data.category.name="Jailbreaks"
    }
    data.uri = data.uri.substring(0, 200);
    let url = `https://gptcall.net/chat.html?data=${encodeURIComponent(JSON.stringify({"contact":{ "id": data.id, "flow": true}}))}`;
    const markdown = `
[![${data.title}](${data.thumbnailURL})](${url})
# ${data.title} | [Start Chat](${url})
${data.description.replace(/\n/g, '\n\n')}

# Prompt

\`\`\`
${data.initPrompt}
\`\`\`

## Welcome Message
${data.welcomeMessage.replace(/\n/g, '\n\n')}

## Conversation

${data.Conversation.messages.map(message => `**${message.role.toUpperCase()}**: ${message.content.replace(/\n/g, '\n\n')}`).join('\n')}


`;
    await fs.writeFile(`gpts/${data.uri}.md`, markdown);
    
}
const groups = groupBy(flow, "categoryId", "subCategoryId");

let header = ``;

for (let categoryId in groups) {
    const category = groups[categoryId];
    let tableOfContents = ``;
    for (let subCategoryId in category) 
    {
        const subCategory = category[subCategoryId];
        if(tableOfContents=="") tableOfContents += `## ${subCategory[0].category.name} Prompts\n\n`;
        let subCategoryName = subCategory[0].subCategory.name.slice(2).trim();
        tableOfContents += `* [${subCategoryName}](#${subCategoryName.toLowerCase().replace(/\s+/g, '-')})\n`;
    }
    

    for (let subCategoryId in category) {
        const subCategory = category[subCategoryId];
        
        let categoryName = subCategory[0].category.name;
        
        let subCategoryName = subCategory[0].subCategory.name.slice(2).trim();

        console.log(categoryName, subCategoryName);
        header += `- [${categoryName}/${subCategoryName}](#${sanitizeFileName(categoryName)}-${sanitizeFileName(subCategoryName)})\n`;
        tableOfContents += `## ${subCategoryName}\n\n`;
        
        for (let item of subCategory) {
            if (item.title.includes("WormGPT") || item.title.includes("Neo DAN")) continue;
            let desc = item.description.replace(/[\r\n]+/g, ' ').trim().substring(0, 250);
            tableOfContents += `- [${item.title}](./gpts/${item.uri}.md) ${desc}\n`;
        }
        fs.writeFile(`${sanitizeFileName(categoryName)}.md`, tableOfContents);
    }
}
function sanitizeFileName(input) {
    return input.replace(/[\s\\\/:*?"<>|]+/g, '-');
  }
  
//fs.writeFile(`README.md`, `# GPTs Prompts And Jailbreaks\n\n`+header);

function groupBy(array, groupKey1, groupKey2) {
    return array.reduce((result, currentItem) => {
        const groupKey1Value = currentItem[groupKey1];
        const groupKey2Value = currentItem[groupKey2];

        if (!result[groupKey1Value]) {
            result[groupKey1Value] = {};
        }

        if (!result[groupKey1Value][groupKey2Value]) {
            result[groupKey1Value][groupKey2Value] = [];
        }

        result[groupKey1Value][groupKey2Value].push(currentItem);

        return result;
    }, {});
}
