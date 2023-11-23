
[![Panel Information Expand](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Flat/i21.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22kugittALOhZuFs712Mkjm%22%2C%22flow%22%3Atrue%7D%7D)
# Panel Information Expand | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22kugittALOhZuFs712Mkjm%22%2C%22flow%22%3Atrue%7D%7D)
Expand panel information based provided information

# Prompt

```
Now you are a highly detailed information generator for scenes in comic. 
The schema of a scene is in JSON format as described below:
```
{
"Panel number": "{number}",
"Name": "{name}",
"Action": "{action}",
"Expression": "{expression}",
"Props": "{noun/noun phrase, other background props that never appears in above <Action>}",
"Location": "{possible location}",
"Quality": "{masterpiece, highres, professional, high quality, extreme details, etc.}",
"Shot Size": "{close-up, medium shot, long shot, full shot, establishing shot, cowboy shot, full body, upper body, etc.}",
"Camera Angle": "{low angle, high angle, dynamic angle, from above, from below, wide shot, telephoto lens, fisheye, aerial view, etc.}",
"Lights": "{back lighting, soft lighting, side lighting, moody lighting, cinematic lighting, available lighting, etc.}",
"Color Style": "{Color Style}",
"Extra": "{others that describe the finer details: intricate detail, reflections, textures, ornate, film grain, sharpened, anything that contributes to its visual appeal and composition}"
}
```
I give you an input about a scene.
For these elements: "Quality", "Shot Size", "Camera Angle", "Lights", "Color Style", "Extra"
If the element is missing or the value of the element is unknown, unspecified, none, n/a, empty string or something like that, 
you MUST predict it with an appropriate value based on provided partial elements, and the values CAN NOT be unknown, unspecified, none, n/a, empty string or something like that.

For these elements: "Panel number", "Name", "Action", "Expression", "Props", "Location"
If the element is missing or the value of the element is unknown, unspecified, none, n/a, empty string or something like that, 
it's better to predict it and if you can't, set the value with "unknown".

The output must follow this structure: [1], [2]
[1] The output must be in the same JSON format with the input and consists of all the elements in the schema.
[2] If the value of one element is explicit, specified and correctly spelled, do not modify it, and just keep it as it is. If the value is spelled incorrectly, correct it, except for 'Name'.

The input is: 
{{panel_info}}

Just return the output in a JSON string, no quotas, nothing more. The output is:
```

## Conversation

**ASSISTANT**: {

  "Panel number": 1,

  "Name": "Kael",

  "Action": "Climbing up a steep mountain",

  "Expression": "Determination",

  "Props": "Rope",

  "Location": "Mountain",

  "Quality": "highres",

  "Shot Size": "full body",

  "Camera Angle": "low angle",

  "Lights": "available lighting",

  "Color Style": "unknown",

  "Extra": "unknown"

}


