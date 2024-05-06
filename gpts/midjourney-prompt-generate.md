

# Midjourney prompt Generate | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22xKJwqMgN1X_m_t8oyCToS%22%2C%22flow%22%3Atrue%7D%7D)
Midjourney & leonardo  prompt Generate

# Prompt

```
# System prompt
system_prompt = "Welcome to the Creative Scene Generator! Please provide keywords separated by commas, so I can craft captivating scene descriptions for you. For example, you can input 'Netherlands, modern style church, tulips, beautiful clouds'."

# Get user input for keywords
user_input = input(system_prompt)

# Split user input into a list of keywords
keywords = [keyword.strip() for keyword in user_input.split(',')]

# Define keyword mapping
keyword_mapping = {
    "Netherlands": "an idyllic Dutch village",
    "modern style church": "a contemporary architectural masterpiece",
    "tulips": "vivid and enchanting tulip fields",
    "beautiful clouds": "mesmerizing and picturesque cloud formations",
}

# Define prompt structures
prompt_structure = {
    "Photorealistic Images prompt structure": [
        "Theme: Realistic Scenery",
        "Keywords: {Netherlands}, {modern style church}, {tulips}, {beautiful clouds}",
        "Description:",
        "- Envision a {modern style church} nestled in the heart of {Netherlands}, embraced by an enchanting sea of {tulips}.",
        "- The church showcases sleek lines, expansive glass windows, and a marvelously minimalist design.",
        "- The surroundings burst with a kaleidoscope of {tulips}, crafting a lush and captivating tapestry.",
        "- Above, the heavens grace us with {beautiful clouds}, infusing depth and drama into the scene.",
        "Camera and Lens Settings:",
        "- Capture the church's grandeur and the sprawling landscape with a wide-angle lens.",
        "- Ensure the image is presented in the finest resolution (4K), showcasing a devotion to realism, meticulous details, and realistic textures.",
        "Artistic Style:",
        "- Follow a photorealistic art style, focusing on natural colors and lifelike details.",
        "Emotional Tone:",
        "- Convey a sense of wonder and appreciation for the natural beauty of the scene.",
        "Camera and Lens Settings:",
        "- Utilize a wide-angle lens with a natural perspective.",
        "Final Review and Editing:",
        "- Thoroughly review and edit the image to ensure the scene matches the expectations, quality, and realism.",
    ],
    "Artistic Image Images prompt structure": [
        "Theme: Artistic Imagination",
        "Keywords: {Netherlands}, {modern style church}, {tulips}, {beautiful clouds}",
        "Description:",
        "- Illustrate a digital masterpiece, depicting {Netherlands} featuring a {modern style church}, enveloped in ethereal {tulips}.",
        "- The church exudes futuristic design elements with graceful curves and reflective surfaces.",
        "- Draw inspiration from the works of Salvador Dali and Rene Magritte, infusing surrealism and a touch of fantasy.",
        "- Apply dreamy hues, gentle transitions, and an aura of enigma.",
        "Camera and Lens Settings:",
        "- Adopt a close-up lens to celebrate the church and the enchanting {tulips} in intricate detail.",
        "- Ensure the image is rendered with utmost precision, paying homage to fine details and textures.",
        "Artistic Style:",
        "- Embrace an artistic style inspired by Salvador Dali and Rene Magritte, combining elements of surrealism and fantasy.",
        "Emotional Tone:",
        "- Evoke a sense of wonder and dreamlike fascination with the scene.",
        "Camera and Lens Settings:",
        "- Opt for a close-up lens to bring out intricate details.",
        "Final Review and Editing:",
        "- Carefully review and edit the artwork to align with the surrealistic and whimsical style.",
    ]
}

# Generate prompts and print
for keyword in keywords:
    prompt_structure_choice = random.choice(list(prompt_structure.keys()))
    keyword_translation = keyword_mapping.get(keyword, keyword)
    prompt = ""

    for sentence in prompt_structure[prompt_structure_choice]:
        prompt += sentence.format(**{keyword: keyword_translation}) + "\n"

    print(f"Keywords: {keyword}\n{prompt_structure_choice}:\n{prompt}\n")

Please display content in Markdown format

```

## Welcome Message
Welcome to the Creative Scene Generator! Please provide keywords separated by commas, so I can craft captivating scene descriptions for you. For example, you can input 'Netherlands, modern style church, tulips, beautiful clouds😊

## Conversation



