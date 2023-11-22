import { promises as fs } from 'fs';




const jsonContents = await fs.readFile("data/gpts.json", 'utf8');
const flow = JSON.parse(jsonContents).filter(data => data.uri.length <= 200 && !data.nsfw).slice(0, 1000);
//files

let i =0;
for (let data of flow) {
    
    let url = "https://gptcall.net/chat.html?data="+encodeURIComponent(JSON.stringify({"contact":{ "id": data.id, "flow": true}}));
    const markdown = `
[![Vortex](${data.coverURL})](${url})
# ${data.title} [Start Chat](${url})
${data.description.replace(/\n/g, '\n\n')}


**Tagline:** ${data.User.tagline}

## Tags

${data.Tag.map(tag => `- ${tag.name}`).join('\n')}

# Prompt

\`\`\`
${data.initPrompt}
\`\`\`

## Conversation

${data.Conversation.messages.map(message => `**${message.role.toUpperCase()}**: ${message.content.replace(/\n/g, '\n\n')}`).join('\n')}


`;
    await fs.writeFile(`gpts/${data.uri}.md`, markdown);
    
}






//categories

const groups = groupBy(flow, "categoryId");

let header = "# List of GPTs Prompts for free use (ChatGPT Plus subscription bypass.)\n\n";

for (let groupId of Object.getOwnPropertyNames(groups)) {
    let name = groups[groupId][0].category.name;

    console.log(name);

    // Append category links to readmeContent, renaming 'Others' to 'readme'
    header += `- [${name}](./${name.replace(/\s+/g, '-')}.md)\n`;
}
await fs.writeFile(`README.md`, header);

for (let groupId of Object.getOwnPropertyNames(groups)) {
    let name = groups[groupId][0].category.name;

    let readmeContent = `${header}\n\n# ${name}\n\n`;

    for (let item of groups[groupId]) {
        let desc = item.description.replace(/[\r\n]+/g, ' ').trim().substring(0, 550);
        readmeContent += `- [${item.title}](./gpts/${item.uri}.md) ${desc}\n`;
    }

    await fs.writeFile(`${name.replace(/\s+/g, '-')}.md`, readmeContent);

}



function groupBy(array, key) {
    return array.reduce((result, currentItem) => {
        const groupKey = currentItem[key];
        if (!result[groupKey]) {
            result[groupKey] = [];
        }
        result[groupKey].push(currentItem);
        return result;
    }, {});
}
